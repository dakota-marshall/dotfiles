# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Sky-Lab",
    "author" : "Blender Labs", 
    "description" : "Create Beautiful, Volumetric Skies in Minutes!",
    "blender" : (3, 4, 1),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "Lighting" 
}


import bpy
import bpy.utils.previews
import os


addon_keymaps = {}
_icons = None


def property_exists(prop_path, glob, loc):
    try:
        eval(prop_path, glob, loc)
        return True
    except:
        return False


class SNA_OT_Add_Skylab_B88F2(bpy.types.Operator):
    bl_idname = "sna.add_skylab_b88f2"
    bl_label = "Add Sky-Lab"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.view_settings.exposure = -3.5
        bpy.context.scene.cycles.volume_max_steps = 10
        bpy.context.scene.cycles.volume_bounces = 10
        if (property_exists("bpy.data.worlds", globals(), locals()) and 'Sky-Lab-Atmosphere' in bpy.data.worlds):
            bpy.context.scene.world = bpy.data.worlds['Sky-Lab-Atmosphere']
            before_data = list(bpy.data.objects)
            bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Another Atmosphere.blend') + r'\Object', filename='ViewDisObj', link=False)
            new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
            appended_BC1AE = None if not new_data else new_data[0]
        else:
            before_data = list(bpy.data.worlds)
            bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Another Atmosphere.blend') + r'\World', filename='Sky-Lab-Atmosphere', link=False)
            new_data = list(filter(lambda d: not d in before_data, list(bpy.data.worlds)))
            appended_8101A = None if not new_data else new_data[0]
            bpy.context.scene.world = appended_8101A
            before_data = list(bpy.data.objects)
            bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Another Atmosphere.blend') + r'\Object', filename='ViewDisObj', link=False)
            new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
            appended_C096D = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Add_Clouds_4C6F2(bpy.types.Operator):
    bl_idname = "sna.add_clouds_4c6f2"
    bl_label = "Add Clouds"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (property_exists("bpy.data.objects", globals(), locals()) and 'Sky-Lab-Clouds' in bpy.data.objects):
            pass
        else:
            if (property_exists("bpy.data.node_groups", globals(), locals()) and 'Clouds' in bpy.data.node_groups):
                bpy.data.node_groups.remove(tree=bpy.data.node_groups['Clouds'], do_unlink=True, do_id_user=True, do_ui_user=True, )
                if (property_exists("bpy.data.materials", globals(), locals()) and 'Sky-Lab-Clouds' in bpy.data.materials):
                    bpy.data.materials.remove(material=bpy.data.materials['Sky-Lab-Clouds'], do_unlink=True, do_id_user=True, do_ui_user=True, )
                    before_data = list(bpy.data.objects)
                    bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Another Atmosphere.blend') + r'\Object', filename='Sky-Lab-Clouds', link=False)
                    new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
                    appended_C6235 = None if not new_data else new_data[0]
                else:
                    before_data = list(bpy.data.objects)
                    bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Another Atmosphere.blend') + r'\Object', filename='Sky-Lab-Clouds', link=False)
                    new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
                    appended_16B2B = None if not new_data else new_data[0]
            else:
                if (property_exists("bpy.data.materials", globals(), locals()) and 'Sky-Lab-Clouds' in bpy.data.materials):
                    bpy.data.materials.remove(material=bpy.data.materials['Sky-Lab-Clouds'], do_unlink=True, do_id_user=True, do_ui_user=True, )
                    before_data = list(bpy.data.objects)
                    bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Another Atmosphere.blend') + r'\Object', filename='Sky-Lab-Clouds', link=False)
                    new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
                    appended_4BCBB = None if not new_data else new_data[0]
                else:
                    before_data = list(bpy.data.objects)
                    bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Another Atmosphere.blend') + r'\Object', filename='Sky-Lab-Clouds', link=False)
                    new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
                    appended_187F8 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_SKYLAB_508F7(bpy.types.Panel):
    bl_label = 'Sky-Lab'
    bl_idname = 'SNA_PT_SKYLAB_508F7'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Sky-Lab'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        op = layout.operator('sna.add_skylab_b88f2', text='Import Atmosphere', icon_value=735, emboss=True, depress=False)
        op = layout.operator('sna.add_clouds_4c6f2', text='Import Clouds', icon_value=653, emboss=True, depress=False)
        op = layout.operator('wm.url_open', text='Documentation', icon_value=52, emboss=True, depress=False)
        op.url = 'https://sites.google.com/view/blender-labs/sky-lab/sky-lab-docs?authuser=0'
        layout.separator(factor=0.5)
        layout.prop_search(bpy.context.scene, 'world', bpy.data, 'worlds', text='Active World', icon='NONE')


class SNA_PT_CLOUDS_34F65(bpy.types.Panel):
    bl_label = 'Clouds'
    bl_idname = 'SNA_PT_CLOUDS_34F65'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 2
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_SKYLAB_508F7'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_3B56A = layout.box()
        box_3B56A.alert = False
        box_3B56A.enabled = True
        box_3B56A.active = True
        box_3B56A.use_property_split = False
        box_3B56A.use_property_decorate = False
        box_3B56A.alignment = 'Expand'.upper()
        box_3B56A.scale_x = 1.0
        box_3B56A.scale_y = 1.0
        if not True: box_3B56A.operator_context = "EXEC_DEFAULT"
        box_3B56A.label(text='Layers:', icon_value=491)
        box_3B56A.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[1], 'default_value', text='Layer 1', icon_value=0, emboss=True)
        box_3B56A.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[2], 'default_value', text='Layer 2', icon_value=0, emboss=True)
        box_3B56A.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[3], 'default_value', text='Layer 3', icon_value=0, emboss=True)
        box_3B56A.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[4], 'default_value', text='Layer 4', icon_value=0, emboss=True)
        box_3B56A.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[5], 'default_value', text='Layer 5', icon_value=0, emboss=True)
        box_3B56A.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[6], 'default_value', text='Layer 6', icon_value=0, emboss=True)
        box_7496E = layout.box()
        box_7496E.alert = False
        box_7496E.enabled = True
        box_7496E.active = True
        box_7496E.use_property_split = False
        box_7496E.use_property_decorate = False
        box_7496E.alignment = 'Expand'.upper()
        box_7496E.scale_x = 1.0
        box_7496E.scale_y = 1.0
        if not True: box_7496E.operator_context = "EXEC_DEFAULT"
        box_7496E.label(text='Basic Controls', icon_value=376)
        box_7496E.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['RGB'].outputs[0], 'default_value', text='Color', icon_value=0, emboss=True)
        box_7496E.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[8], 'default_value', text='Density', icon_value=0, emboss=True)
        box_7496E.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[9], 'default_value', text='Seed', icon_value=0, emboss=True)
        box_8EF34 = layout.box()
        box_8EF34.alert = False
        box_8EF34.enabled = True
        box_8EF34.active = True
        box_8EF34.use_property_split = False
        box_8EF34.use_property_decorate = False
        box_8EF34.alignment = 'Expand'.upper()
        box_8EF34.scale_x = 1.0
        box_8EF34.scale_y = 1.0
        if not True: box_8EF34.operator_context = "EXEC_DEFAULT"
        box_8EF34.label(text='Layer Controls:', icon_value=23)
        if (bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[1].default_value) or bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[2].default_value) or bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[3].default_value) or bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[4].default_value) or bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[5].default_value) or bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[6].default_value)):
            col_66C70 = box_8EF34.column(heading='', align=False)
            col_66C70.alert = False
            col_66C70.enabled = True
            col_66C70.active = True
            col_66C70.use_property_split = False
            col_66C70.use_property_decorate = False
            col_66C70.scale_x = 1.0
            col_66C70.scale_y = 1.0
            col_66C70.alignment = 'Expand'.upper()
            if not True: col_66C70.operator_context = "EXEC_DEFAULT"
            if bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[1].default_value):
                box_F9DC7 = col_66C70.box()
                box_F9DC7.alert = False
                box_F9DC7.enabled = True
                box_F9DC7.active = True
                box_F9DC7.use_property_split = False
                box_F9DC7.use_property_decorate = False
                box_F9DC7.alignment = 'Expand'.upper()
                box_F9DC7.scale_x = 1.0
                box_F9DC7.scale_y = 1.0
                if not True: box_F9DC7.operator_context = "EXEC_DEFAULT"
                box_F9DC7.label(text='Layer 1:', icon_value=0)
                box_F9DC7.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[11], 'default_value', text='Coverage', icon_value=0, emboss=True)
                box_F9DC7.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[12], 'default_value', text='Scale', icon_value=0, emboss=True)
                box_F9DC7.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[13], 'default_value', text='Detail', icon_value=0, emboss=True)
                box_F9DC7.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[14], 'default_value', text='Roughness', icon_value=0, emboss=True)
                box_F9DC7.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[15], 'default_value', text='Distortion', icon_value=0, emboss=True)
                box_F9DC7.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ'].inputs[0], 'default_value', text='Location X', icon_value=0, emboss=True)
                box_F9DC7.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ'].inputs[1], 'default_value', text='Location Y', icon_value=0, emboss=True)
            if bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[2].default_value):
                box_39B52 = col_66C70.box()
                box_39B52.alert = False
                box_39B52.enabled = True
                box_39B52.active = True
                box_39B52.use_property_split = False
                box_39B52.use_property_decorate = False
                box_39B52.alignment = 'Expand'.upper()
                box_39B52.scale_x = 1.0
                box_39B52.scale_y = 1.0
                if not True: box_39B52.operator_context = "EXEC_DEFAULT"
                box_39B52.label(text='Layer 2:', icon_value=0)
                box_39B52.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[20], 'default_value', text='Coverage', icon_value=0, emboss=True)
                box_39B52.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[21], 'default_value', text='Scale', icon_value=0, emboss=True)
                box_39B52.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[22], 'default_value', text='Randomness', icon_value=0, emboss=True)
                box_39B52.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[23], 'default_value', text='Detail', icon_value=0, emboss=True)
                box_39B52.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ.005'].inputs[0], 'default_value', text='Location X', icon_value=0, emboss=True)
                box_39B52.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ.005'].inputs[1], 'default_value', text='Location Y', icon_value=0, emboss=True)
            if bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[3].default_value):
                box_9A1DF = col_66C70.box()
                box_9A1DF.alert = False
                box_9A1DF.enabled = True
                box_9A1DF.active = True
                box_9A1DF.use_property_split = False
                box_9A1DF.use_property_decorate = False
                box_9A1DF.alignment = 'Expand'.upper()
                box_9A1DF.scale_x = 1.0
                box_9A1DF.scale_y = 1.0
                if not True: box_9A1DF.operator_context = "EXEC_DEFAULT"
                box_9A1DF.label(text='Layer 3:', icon_value=0)
                box_9A1DF.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[28], 'default_value', text='Coverage', icon_value=0, emboss=True)
                box_9A1DF.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[29], 'default_value', text='Scale', icon_value=0, emboss=True)
                box_9A1DF.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[30], 'default_value', text='Detail', icon_value=0, emboss=True)
                box_9A1DF.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[31], 'default_value', text='Distortion', icon_value=0, emboss=True)
                box_9A1DF.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[32], 'default_value', text='Detail Scale', icon_value=0, emboss=True)
                box_9A1DF.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ.008'].inputs[0], 'default_value', text='Location X', icon_value=0, emboss=True)
                box_9A1DF.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ.008'].inputs[1], 'default_value', text='Location Y', icon_value=0, emboss=True)
            if bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[4].default_value):
                box_C2E21 = col_66C70.box()
                box_C2E21.alert = False
                box_C2E21.enabled = True
                box_C2E21.active = True
                box_C2E21.use_property_split = False
                box_C2E21.use_property_decorate = False
                box_C2E21.alignment = 'Expand'.upper()
                box_C2E21.scale_x = 1.0
                box_C2E21.scale_y = 1.0
                if not True: box_C2E21.operator_context = "EXEC_DEFAULT"
                box_C2E21.label(text='Layer 4:', icon_value=0)
                box_C2E21.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[37], 'default_value', text='Coverage', icon_value=0, emboss=True)
                box_C2E21.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[38], 'default_value', text='Scale', icon_value=0, emboss=True)
                box_C2E21.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[39], 'default_value', text='Distortion', icon_value=0, emboss=True)
                box_C2E21.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[40], 'default_value', text='Detail', icon_value=0, emboss=True)
                box_C2E21.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[41], 'default_value', text='Detail Scale', icon_value=0, emboss=True)
                box_C2E21.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[42], 'default_value', text='Detail Roughness', icon_value=0, emboss=True)
                box_C2E21.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[43], 'default_value', text='Phase Offset', icon_value=0, emboss=True)
                box_C2E21.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[44], 'default_value', text='Rotation', icon_value=0, emboss=True)
                box_C2E21.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ.011'].inputs[0], 'default_value', text='Location X', icon_value=0, emboss=True)
                box_C2E21.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ.011'].inputs[1], 'default_value', text='Location Y', icon_value=0, emboss=True)
            if bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[5].default_value):
                box_86C76 = col_66C70.box()
                box_86C76.alert = False
                box_86C76.enabled = True
                box_86C76.active = True
                box_86C76.use_property_split = False
                box_86C76.use_property_decorate = False
                box_86C76.alignment = 'Expand'.upper()
                box_86C76.scale_x = 1.0
                box_86C76.scale_y = 1.0
                if not True: box_86C76.operator_context = "EXEC_DEFAULT"
                box_86C76.label(text='Layer 5:', icon_value=0)
                box_86C76.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[49], 'default_value', text='Coverage', icon_value=0, emboss=True)
                box_86C76.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[50], 'default_value', text='Distortion', icon_value=0, emboss=True)
                box_86C76.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[51], 'default_value', text='Detail', icon_value=0, emboss=True)
                box_86C76.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[53], 'default_value', text='Roughness', icon_value=0, emboss=True)
                box_86C76.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ.014'].inputs[0], 'default_value', text='Location X', icon_value=0, emboss=True)
                box_86C76.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ.014'].inputs[1], 'default_value', text='Location Y', icon_value=0, emboss=True)
            if bool(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[6].default_value):
                box_CC42D = col_66C70.box()
                box_CC42D.alert = False
                box_CC42D.enabled = True
                box_CC42D.active = True
                box_CC42D.use_property_split = False
                box_CC42D.use_property_decorate = False
                box_CC42D.alignment = 'Expand'.upper()
                box_CC42D.scale_x = 1.0
                box_CC42D.scale_y = 1.0
                if not True: box_CC42D.operator_context = "EXEC_DEFAULT"
                box_CC42D.label(text='Layer 6:', icon_value=0)
                box_CC42D.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[58], 'default_value', text='Coverage', icon_value=0, emboss=True)
                box_CC42D.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[59], 'default_value', text='Scale', icon_value=0, emboss=True)
                box_CC42D.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[60], 'default_value', text='Detail', icon_value=0, emboss=True)
                box_CC42D.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[61], 'default_value', text='Roughness', icon_value=0, emboss=True)
                box_CC42D.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Clouds'].inputs[62], 'default_value', text='Distortion', icon_value=0, emboss=True)
                box_CC42D.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ.017'].inputs[0], 'default_value', text='Location X', icon_value=0, emboss=True)
                box_CC42D.prop(bpy.data.materials['Sky-Lab-Clouds'].node_tree.nodes['Combine XYZ.017'].inputs[1], 'default_value', text='Location Y', icon_value=0, emboss=True)
        else:
            box_8EF34.label(text='Enable a layer for the settings.', icon_value=2)


class SNA_PT_ATMOSPHERIC_CONDITIONS_F1301(bpy.types.Panel):
    bl_label = 'Atmospheric Conditions'
    bl_idname = 'SNA_PT_ATMOSPHERIC_CONDITIONS_F1301'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 1
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_SKYLAB_508F7'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        col_4BF53 = layout.column(heading='', align=False)
        col_4BF53.alert = False
        col_4BF53.enabled = True
        col_4BF53.active = True
        col_4BF53.use_property_split = False
        col_4BF53.use_property_decorate = False
        col_4BF53.scale_x = 1.0
        col_4BF53.scale_y = 1.0
        col_4BF53.alignment = 'Expand'.upper()
        if not True: col_4BF53.operator_context = "EXEC_DEFAULT"
        box_71CEE = col_4BF53.box()
        box_71CEE.alert = False
        box_71CEE.enabled = True
        box_71CEE.active = True
        box_71CEE.use_property_split = True
        box_71CEE.use_property_decorate = False
        box_71CEE.alignment = 'Expand'.upper()
        box_71CEE.scale_x = 1.0
        box_71CEE.scale_y = 1.0
        if not True: box_71CEE.operator_context = "EXEC_DEFAULT"
        box_71CEE.label(text='Sun Settings:', icon_value=299)
        box_71CEE.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Sky Texture'], 'sun_disc', text='Sun Disc', icon_value=(299 if bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Sky Texture'].sun_disc else 288), emboss=True)
        box_71CEE.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Sky Texture'], 'sun_size', text='Angular Diameter', icon_value=0, emboss=True)
        box_71CEE.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Sky Texture'], 'sun_intensity', text='Strength', icon_value=0, emboss=True)
        box_71CEE.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Sky Texture'], 'sun_elevation', text='Elevation', icon_value=0, emboss=True)
        box_71CEE.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Sky Texture'], 'sun_rotation', text='Azimuth', icon_value=0, emboss=True)
        col_4BF53.separator(factor=1.0)
        box_7988A = col_4BF53.box()
        box_7988A.alert = False
        box_7988A.enabled = True
        box_7988A.active = True
        box_7988A.use_property_split = True
        box_7988A.use_property_decorate = False
        box_7988A.alignment = 'Expand'.upper()
        box_7988A.scale_x = 1.0
        box_7988A.scale_y = 1.0
        if not True: box_7988A.operator_context = "EXEC_DEFAULT"
        box_7988A.label(text='Atmosphere:', icon_value=735)
        box_7988A.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Sky Texture'], 'altitude', text='Altitude', icon_value=0, emboss=True)
        box_7988A.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Sky Texture'], 'air_density', text='Air', icon_value=0, emboss=True)
        box_7988A.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Sky Texture'], 'dust_density', text='Dust', icon_value=0, emboss=True)
        box_7988A.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Sky Texture'], 'ozone_density', text='Ozone', icon_value=0, emboss=True)
        box_7988A.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['NightSky'].inputs[0], 'default_value', text='Horizon Cutoff', icon_value=0, emboss=True)
        box_7988A.label(text='Colors:', icon_value=54)
        box_7988A.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Colors'].inputs[2], 'default_value', text='Custom Color A', icon_value=0, emboss=True)
        box_7988A.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Colors'].inputs[3], 'default_value', text='Custom Color B', icon_value=0, emboss=True)
        box_7988A.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Colors'].inputs[4], 'default_value', text='Indirect Light', icon_value=0, emboss=True)
        box_7988A.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Colors'].inputs[5], 'default_value', text='Mix', icon_value=0, emboss=True)
        col_4BF53.separator(factor=1.0)
        box_09615 = col_4BF53.box()
        box_09615.alert = False
        box_09615.enabled = True
        box_09615.active = True
        box_09615.use_property_split = True
        box_09615.use_property_decorate = False
        box_09615.alignment = 'Expand'.upper()
        box_09615.scale_x = 1.0
        box_09615.scale_y = 1.0
        if not True: box_09615.operator_context = "EXEC_DEFAULT"
        box_09615.label(text='Volumetrics', icon_value=723)
        box_09615.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Vol Atmosphere'].inputs[3], 'default_value', text='Scattering', icon_value=0, emboss=True)
        box_09615.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Vol Atmosphere'].inputs[0], 'default_value', text='Scattering Color', icon_value=0, emboss=True)
        box_09615.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Vol Atmosphere'].inputs[2], 'default_value', text='Absorption', icon_value=0, emboss=True)
        box_09615.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Vol Atmosphere'].inputs[1], 'default_value', text='Absorption Color', icon_value=0, emboss=True)
        box_09615.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Vol Atmosphere'].inputs[4], 'default_value', text='Anisotropy', icon_value=0, emboss=True)
        box_09615.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Vol Atmosphere'].inputs[5], 'default_value', text='Altitude', icon_value=0, emboss=True)
        col_4BF53.separator(factor=1.0)
        box_6CCB7 = col_4BF53.box()
        box_6CCB7.alert = False
        box_6CCB7.enabled = True
        box_6CCB7.active = True
        box_6CCB7.use_property_split = True
        box_6CCB7.use_property_decorate = False
        box_6CCB7.alignment = 'Expand'.upper()
        box_6CCB7.scale_x = 1.0
        box_6CCB7.scale_y = 1.0
        if not True: box_6CCB7.operator_context = "EXEC_DEFAULT"
        box_6CCB7.label(text='Night Sky:', icon_value=654)
        box_6CCB7.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Night Sky'].inputs[3], 'default_value', text='Galaxy Angle', icon_value=0, emboss=True)
        box_6CCB7.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Night Sky'].inputs[5], 'default_value', text='Galaxy Strength', icon_value=0, emboss=True)
        box_6CCB7.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Night Sky'].inputs[6], 'default_value', text='Galaxy Contrast', icon_value=0, emboss=True)
        box_6CCB7.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Night Sky'].inputs[7], 'default_value', text='Night Color A', icon_value=0, emboss=True)
        box_6CCB7.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Night Sky'].inputs[8], 'default_value', text='Night Color B', icon_value=0, emboss=True)
        box_6CCB7.prop(bpy.data.worlds['Sky-Lab-Atmosphere'].node_tree.nodes['Night Sky'].inputs[9], 'default_value', text='Atmosphere Strength', icon_value=0, emboss=True)
        box_40B92 = box_6CCB7.box()
        box_40B92.alert = False
        box_40B92.enabled = True
        box_40B92.active = True
        box_40B92.use_property_split = False
        box_40B92.use_property_decorate = False
        box_40B92.alignment = 'Expand'.upper()
        box_40B92.scale_x = 1.0
        box_40B92.scale_y = 1.0
        if not True: box_40B92.operator_context = "EXEC_DEFAULT"
        box_40B92.label(text='Galaxy Texture by European Southern Observatory (ESO)', icon_value=52)
        box_40B92.label(text='ESO/S. Brunier, CC BY 4.0 <https://creativecommons.org/licenses/by/4.0>, via Wikimedia Commons', icon_value=0)
        op = box_40B92.operator('wm.url_open', text='Galaxy Texture in Other Resolutions + License Info', icon_value=72, emboss=True, depress=False)
        op.url = 'https://commons.wikimedia.org/wiki/File:ESO_-_Milky_Way.jpg'


class SNA_PT_PROJECT_SETTINGS_9929F(bpy.types.Panel):
    bl_label = 'Project Settings'
    bl_idname = 'SNA_PT_PROJECT_SETTINGS_9929F'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 3
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_SKYLAB_508F7'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        layout.label(text='Color Management', icon_value=565)
        if hasattr(bpy.types,"RENDER_PT_color_management"):
            if not hasattr(bpy.types.RENDER_PT_color_management, "poll") or bpy.types.RENDER_PT_color_management.poll(context):
                bpy.types.RENDER_PT_color_management.draw(self, context)
            else:
                layout.label(text="Can't display this panel here!", icon="ERROR")
        else:
            layout.label(text="Can't display this panel!", icon="ERROR")
        layout.label(text='Light Paths:', icon_value=221)
        if hasattr(bpy.types,"CYCLES_RENDER_PT_light_paths_max_bounces"):
            if not hasattr(bpy.types.CYCLES_RENDER_PT_light_paths_max_bounces, "poll") or bpy.types.CYCLES_RENDER_PT_light_paths_max_bounces.poll(context):
                bpy.types.CYCLES_RENDER_PT_light_paths_max_bounces.draw(self, context)
            else:
                layout.label(text="Can't display this panel here!", icon="ERROR")
        else:
            layout.label(text="Can't display this panel!", icon="ERROR")
        layout.label(text='Volumes:', icon_value=723)
        if hasattr(bpy.types,"CYCLES_RENDER_PT_volumes"):
            if not hasattr(bpy.types.CYCLES_RENDER_PT_volumes, "poll") or bpy.types.CYCLES_RENDER_PT_volumes.poll(context):
                bpy.types.CYCLES_RENDER_PT_volumes.draw(self, context)
            else:
                layout.label(text="Can't display this panel here!", icon="ERROR")
        else:
            layout.label(text="Can't display this panel!", icon="ERROR")
        layout.label(text='Sampling:', icon_value=116)
        layout.label(text='Viewport', icon_value=0)
        if hasattr(bpy.types,"CYCLES_RENDER_PT_sampling_viewport"):
            if not hasattr(bpy.types.CYCLES_RENDER_PT_sampling_viewport, "poll") or bpy.types.CYCLES_RENDER_PT_sampling_viewport.poll(context):
                bpy.types.CYCLES_RENDER_PT_sampling_viewport.draw(self, context)
            else:
                layout.label(text="Can't display this panel here!", icon="ERROR")
        else:
            layout.label(text="Can't display this panel!", icon="ERROR")
        layout.prop(bpy.context.scene.cycles, 'use_preview_denoising', text='Denoise', icon_value=0, emboss=True)
        if hasattr(bpy.types,"CYCLES_RENDER_PT_sampling_viewport_denoise"):
            if not hasattr(bpy.types.CYCLES_RENDER_PT_sampling_viewport_denoise, "poll") or bpy.types.CYCLES_RENDER_PT_sampling_viewport_denoise.poll(context):
                bpy.types.CYCLES_RENDER_PT_sampling_viewport_denoise.draw(self, context)
            else:
                layout.label(text="Can't display this panel here!", icon="ERROR")
        else:
            layout.label(text="Can't display this panel!", icon="ERROR")
        layout.separator(factor=1.0)
        layout.label(text='Render', icon_value=0)
        if hasattr(bpy.types,"CYCLES_RENDER_PT_sampling_render"):
            if not hasattr(bpy.types.CYCLES_RENDER_PT_sampling_render, "poll") or bpy.types.CYCLES_RENDER_PT_sampling_render.poll(context):
                bpy.types.CYCLES_RENDER_PT_sampling_render.draw(self, context)
            else:
                layout.label(text="Can't display this panel here!", icon="ERROR")
        else:
            layout.label(text="Can't display this panel!", icon="ERROR")
        layout.prop(bpy.data.scenes['Scene'].cycles, 'use_denoising', text='Denoise', icon_value=0, emboss=True)
        if hasattr(bpy.types,"CYCLES_RENDER_PT_sampling_render_denoise"):
            if not hasattr(bpy.types.CYCLES_RENDER_PT_sampling_render_denoise, "poll") or bpy.types.CYCLES_RENDER_PT_sampling_render_denoise.poll(context):
                bpy.types.CYCLES_RENDER_PT_sampling_render_denoise.draw(self, context)
            else:
                layout.label(text="Can't display this panel here!", icon="ERROR")
        else:
            layout.label(text="Can't display this panel!", icon="ERROR")


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_OT_Add_Skylab_B88F2)
    bpy.utils.register_class(SNA_OT_Add_Clouds_4C6F2)
    bpy.utils.register_class(SNA_PT_SKYLAB_508F7)
    bpy.utils.register_class(SNA_PT_CLOUDS_34F65)
    bpy.utils.register_class(SNA_PT_ATMOSPHERIC_CONDITIONS_F1301)
    bpy.utils.register_class(SNA_PT_PROJECT_SETTINGS_9929F)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_OT_Add_Skylab_B88F2)
    bpy.utils.unregister_class(SNA_OT_Add_Clouds_4C6F2)
    bpy.utils.unregister_class(SNA_PT_SKYLAB_508F7)
    bpy.utils.unregister_class(SNA_PT_CLOUDS_34F65)
    bpy.utils.unregister_class(SNA_PT_ATMOSPHERIC_CONDITIONS_F1301)
    bpy.utils.unregister_class(SNA_PT_PROJECT_SETTINGS_9929F)
