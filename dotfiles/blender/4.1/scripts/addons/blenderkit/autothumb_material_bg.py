# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


import json
import logging
import os
import sys
from pathlib import Path

import bpy

from blenderkit import append_link, bg_blender, bg_utils, daemon_lib, utils


BLENDERKIT_EXPORT_DATA = sys.argv[-2]
BLENDERKIT_EXPORT_API_KEY = sys.argv[-1]
bk_logger = logging.getLogger(__name__)


def render_thumbnails():
    bpy.ops.render.render(write_still=True, animation=False)


def unhide_collection(cname):
    collection = bpy.context.scene.collection.children[cname]
    collection.hide_viewport = False
    collection.hide_render = False
    collection.hide_select = False


if __name__ == "__main__":
    try:
        bg_blender.progress("preparing thumbnail scene")
        with open(BLENDERKIT_EXPORT_DATA, "r", encoding="utf-8") as s:
            data = json.load(s)
            # append_material(file_name, matname = None, link = False, fake_user = True)

        thumbnail_use_gpu = data.get("thumbnail_use_gpu")
        if data.get("do_download"):
            # need to save the file, so that asset doesn't get downloaded into addon directory
            temp_blend_path = os.path.join(data["tempdir"], "temp.blend")

            # if this isn't here, blender crashes.
            if bpy.app.version >= (3, 0, 0):
                bpy.context.preferences.filepaths.file_preview_type = "NONE"

            bpy.ops.wm.save_as_mainfile(filepath=temp_blend_path)

            asset_data = data["asset_data"]
            has_url, asset_data = daemon_lib.get_download_url(
                asset_data, utils.get_scene_id(), BLENDERKIT_EXPORT_API_KEY
            )
            if not has_url:
                bg_blender.progress(
                    "couldn't download asset for thumnbail re-rendering"
                )
                exit()
            # download first, or rather make sure if it's already downloaded
            bg_blender.progress("downloading asset")
            fpath = bg_utils.download_asset_file(
                asset_data, api_key=BLENDERKIT_EXPORT_API_KEY
            )
            data["filepath"] = fpath

        mat = append_link.append_material(
            file_name=data["filepath"],
            matname=data["asset_name"],
            link=True,
            fake_user=False,
        )

        s = bpy.context.scene

        colmapdict = {
            "BALL": "Ball",
            "BALL_COMPLEX": "Ball complex",
            "FLUID": "Fluid",
            "CLOTH": "Cloth",
            "HAIR": "Hair",
        }
        unhide_collection(colmapdict[data["thumbnail_type"]])
        if data["thumbnail_background"]:
            unhide_collection("Background")
            bpy.data.materials["bg checker colorable"].node_tree.nodes[
                "input_level"
            ].outputs["Value"].default_value = data["thumbnail_background_lightness"]
        tscale = data["thumbnail_scale"]
        scaler = bpy.context.view_layer.objects["scaler"]
        scaler.scale = (tscale, tscale, tscale)
        utils.activate(scaler)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

        bpy.context.view_layer.update()

        for ob in bpy.context.visible_objects:
            if ob.name[:15] == "MaterialPreview":
                utils.activate(ob)
                if bpy.app.version >= (3, 3, 0):
                    bpy.ops.object.transform_apply(
                        location=False, rotation=False, scale=True, isolate_users=True
                    )
                else:
                    bpy.ops.object.transform_apply(
                        location=False, rotation=False, scale=True
                    )
                bpy.ops.object.transform_apply(
                    location=False, rotation=False, scale=True
                )

                ob.material_slots[0].material = mat
                ob.data.use_auto_texspace = False
                ob.data.texspace_size.x = 1  # / tscale
                ob.data.texspace_size.y = 1  # / tscale
                ob.data.texspace_size.z = 1  # / tscale
                if data["adaptive_subdivision"] == True:
                    ob.cycles.use_adaptive_subdivision = True

                else:
                    ob.cycles.use_adaptive_subdivision = False
                ts = data["texture_size_meters"]
                if data["thumbnail_type"] in ["BALL", "BALL_COMPLEX", "CLOTH"]:
                    utils.automap(
                        ob.name,
                        tex_size=ts / tscale,
                        just_scale=True,
                        bg_exception=True,
                    )
        bpy.context.view_layer.update()

        s.cycles.volume_step_size = tscale * 0.1

        if thumbnail_use_gpu is True:
            bpy.context.scene.cycles.device = "GPU"
            compute_device_type = data.get("cycles_compute_device_type")
            if compute_device_type is not None:
                # DOCS:https://github.com/dfelinto/blender/blob/master/intern/cycles/blender/addon/properties.py
                bpy.context.preferences.addons[
                    "cycles"
                ].preferences.compute_device_type = compute_device_type
                bpy.context.preferences.addons["cycles"].preferences.refresh_devices()

        s.cycles.samples = data["thumbnail_samples"]
        bpy.context.view_layer.cycles.use_denoising = data["thumbnail_denoising"]

        # import blender's HDR here
        hdr_path = Path("datafiles/studiolights/world/interior.exr")
        bpath = Path(bpy.utils.resource_path("LOCAL"))
        ipath = bpath / hdr_path
        ipath = str(ipath)

        # this  stuff is for mac and possibly linux. For blender // means relative path.
        # for Mac, // means start of absolute path
        if ipath.startswith("//"):
            ipath = ipath[1:]

        img = bpy.data.images["interior.exr"]
        img.filepath = ipath
        img.reload()

        bpy.context.scene.render.resolution_x = int(data["thumbnail_resolution"])
        bpy.context.scene.render.resolution_y = int(data["thumbnail_resolution"])

        bpy.context.scene.render.filepath = data["thumbnail_path"]
        bg_blender.progress("rendering thumbnail")
        # bpy.ops.wm.save_as_mainfile(filepath='C:/tmp/test.blend')
        # fal
        render_thumbnails()
        if data.get("upload_after_render") and data.get("asset_data"):
            bg_blender.progress("uploading thumbnail")
            file = {
                "type": "thumbnail",
                "index": 0,
                "file_path": data["thumbnail_path"] + ".png",
            }
            upload_data = {
                "name": data["asset_data"]["name"],
                "token": BLENDERKIT_EXPORT_API_KEY,
                "id": data["asset_data"]["id"],
            }
            bg_utils.upload_file(upload_data, file)
        bg_blender.progress("background autothumbnailer finished successfully")

    except Exception as e:
        bk_logger.fatal(f"{e}")
        import traceback

        traceback.print_exc()

        sys.exit(1)
