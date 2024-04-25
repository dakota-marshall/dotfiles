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
    "name" : "Alt Tab Easy Fog 2 Demo",
    "author" : "Alt Tab - Fluffy & BleachedBroccoli", 
    "description" : "Easily add and adjust volumes.",
    "blender" : (3, 4, 0),
    "version" : (1, 0, 0),
    "location" : "N-Panel",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews
import os
from bpy.app.handlers import persistent


addon_keymaps = {}
_icons = None


def property_exists(prop_path, glob, loc):
    try:
        eval(prop_path, glob, loc)
        return True
    except:
        return False


_item_map = dict()


def make_enum_item(_id, name, descr, preview_id, uid):
    lookup = str(_id)+"\0"+str(name)+"\0"+str(descr)+"\0"+str(preview_id)+"\0"+str(uid)
    if not lookup in _item_map:
        _item_map[lookup] = (_id, name, descr, preview_id, uid)
    return _item_map[lookup]


def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id


def sna_update_sna_enum_vdbs_68470(self, context):
    sna_updated_prop = self.sna_enum_vdbs
    if (sna_updated_prop == 'Get More Presets'):
        bpy.ops.wm.url_open('INVOKE_DEFAULT', url='https://blendermarket.com/products/alt-tab-easy-fog2')


def sna_update_sna_enum_volumes_A2B57(self, context):
    sna_updated_prop = self.sna_enum_volumes
    if (sna_updated_prop == 'Get More Presets'):
        bpy.ops.wm.url_open('INVOKE_DEFAULT', url='https://blendermarket.com/products/alt-tab-easy-fog2')


def sna_absorbhue_00A37(layout_function, node_name, hide_absorbtion_values):
    for i_9DE56 in range(len((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes)):
        if ((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes[i_9DE56].name == node_name):
            col_0B73F = layout_function.column(heading='', align=False)
            col_0B73F.alert = False
            col_0B73F.enabled = True
            col_0B73F.active = True
            col_0B73F.use_property_split = False
            col_0B73F.use_property_decorate = False
            col_0B73F.scale_x = 1.0
            col_0B73F.scale_y = 1.0
            col_0B73F.alignment = 'Expand'.upper()
            col_0B73F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_059D6 = col_0B73F.column(heading='', align=False)
            col_059D6.alert = False
            col_059D6.enabled = True
            col_059D6.active = True
            col_059D6.use_property_split = False
            col_059D6.use_property_decorate = False
            col_059D6.scale_x = 1.0
            col_059D6.scale_y = 1.0
            col_059D6.alignment = 'Expand'.upper()
            col_059D6.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EXPLOSION' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                row_97B1C = col_059D6.row(heading='', align=False)
                row_97B1C.alert = False
                row_97B1C.enabled = True
                row_97B1C.active = True
                row_97B1C.use_property_split = False
                row_97B1C.use_property_decorate = False
                row_97B1C.scale_x = 1.0
                row_97B1C.scale_y = 1.5
                row_97B1C.alignment = 'Expand'.upper()
                row_97B1C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_97B1C.label(text='Smoke Color', icon_value=0)
            if (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes[node_name].inputs['Color'].is_linked:
                layout_function = col_059D6
                sna_colorramp_display_3BC97(layout_function, 'COLRAMP')
            else:
                row_8ED56 = col_059D6.row(heading='', align=False)
                row_8ED56.alert = False
                row_8ED56.enabled = True
                row_8ED56.active = True
                row_8ED56.use_property_split = False
                row_8ED56.use_property_decorate = False
                row_8ED56.scale_x = 1.0
                row_8ED56.scale_y = 1.0
                row_8ED56.alignment = 'Expand'.upper()
                row_8ED56.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_8ED56.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[4], 'default_value', text='', icon_value=0, emboss=True)
            if hide_absorbtion_values:
                pass
            else:
                row_F890F = col_059D6.row(heading='', align=False)
                row_F890F.alert = False
                row_F890F.enabled = True
                row_F890F.active = True
                row_F890F.use_property_split = False
                row_F890F.use_property_decorate = False
                row_F890F.scale_x = 1.0
                row_F890F.scale_y = 1.0
                row_F890F.alignment = 'Expand'.upper()
                row_F890F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_F890F.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[0], 'default_value', text='Hue', icon_value=0, emboss=True)
            if hide_absorbtion_values:
                pass
            else:
                row_2A61F = col_059D6.row(heading='', align=False)
                row_2A61F.alert = False
                row_2A61F.enabled = True
                row_2A61F.active = True
                row_2A61F.use_property_split = False
                row_2A61F.use_property_decorate = False
                row_2A61F.scale_x = 1.0
                row_2A61F.scale_y = 1.0
                row_2A61F.alignment = 'Expand'.upper()
                row_2A61F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_2A61F.prop(bpy.context.view_layer.objects.active.active_material.node_tree.nodes[node_name].inputs[1], 'default_value', text='Sat', icon_value=0, emboss=True)
            if hide_absorbtion_values:
                pass
            else:
                row_C41D3 = col_059D6.row(heading='', align=False)
                row_C41D3.alert = False
                row_C41D3.enabled = True
                row_C41D3.active = True
                row_C41D3.use_property_split = False
                row_C41D3.use_property_decorate = False
                row_C41D3.scale_x = 1.0
                row_C41D3.scale_y = 1.0
                row_C41D3.alignment = 'Expand'.upper()
                row_C41D3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_C41D3.prop(bpy.context.view_layer.objects.active.active_material.node_tree.nodes[node_name].inputs[2], 'default_value', text='Value', icon_value=0, emboss=True)


class SNA_OT_Col_Operator_Adcef(bpy.types.Operator):
    bl_idname = "sna.col_operator_adcef"
    bl_label = "COL Operator"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_collapse_bool_1:
            bpy.context.scene.sna_collapse_bool_1 = False
        else:
            bpy.context.scene.sna_collapse_bool_1 = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Col_Operator_2_F7F90(bpy.types.Operator):
    bl_idname = "sna.col_operator_2_f7f90"
    bl_label = "COL Operator 2"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_collapse_bool_2:
            bpy.context.scene.sna_collapse_bool_2 = False
        else:
            bpy.context.scene.sna_collapse_bool_2 = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Col_Operator_3_70D30(bpy.types.Operator):
    bl_idname = "sna.col_operator_3_70d30"
    bl_label = "COL Operator 3"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_collapse_bool_3:
            bpy.context.scene.sna_collapse_bool_3 = False
        else:
            bpy.context.scene.sna_collapse_bool_3 = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Col_Operator_4_9Bbec(bpy.types.Operator):
    bl_idname = "sna.col_operator_4_9bbec"
    bl_label = "COL Operator 4"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_collapse_bool_4:
            bpy.context.scene.sna_collapse_bool_4 = False
        else:
            bpy.context.scene.sna_collapse_bool_4 = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Col_Operator_5_D8Da2(bpy.types.Operator):
    bl_idname = "sna.col_operator_5_d8da2"
    bl_label = "COL Operator 5"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_collapse_bool5:
            bpy.context.scene.sna_collapse_bool5 = False
        else:
            bpy.context.scene.sna_collapse_bool5 = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Col_Operator_6_28476(bpy.types.Operator):
    bl_idname = "sna.col_operator_6_28476"
    bl_label = "COL Operator 6"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_collapse_bool_6:
            bpy.context.scene.sna_collapse_bool_6 = False
        else:
            bpy.context.scene.sna_collapse_bool_6 = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Col_Operator_7_111E2(bpy.types.Operator):
    bl_idname = "sna.col_operator_7_111e2"
    bl_label = "COL Operator 7"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_collapser_bool_7:
            bpy.context.scene.sna_collapser_bool_7 = False
        else:
            bpy.context.scene.sna_collapser_bool_7 = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_mixnode_FFD62(layout_function, node_name):
    if (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes[node_name].inputs['Color'].is_linked:
        layout_function = layout_function
        sna_colorramp_display_3BC97(layout_function, 'COLRAMP')
    else:
        row_4394C = layout_function.row(heading='', align=False)
        row_4394C.alert = False
        row_4394C.enabled = True
        row_4394C.active = True
        row_4394C.use_property_split = False
        row_4394C.use_property_decorate = False
        row_4394C.scale_x = 1.0
        row_4394C.scale_y = 1.5
        row_4394C.alignment = 'Expand'.upper()
        row_4394C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_4394C.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[4], 'default_value', text='', icon_value=0, emboss=True)
    layout_function.separator(factor=0.23999999463558197)
    split_1FDFB = layout_function.split(factor=0.5, align=True)
    split_1FDFB.alert = False
    split_1FDFB.enabled = True
    split_1FDFB.active = True
    split_1FDFB.use_property_split = False
    split_1FDFB.use_property_decorate = False
    split_1FDFB.scale_x = 1.0
    split_1FDFB.scale_y = 1.0
    split_1FDFB.alignment = 'Expand'.upper()
    if not True: split_1FDFB.operator_context = "EXEC_DEFAULT"
    col_53200 = split_1FDFB.column(heading='', align=False)
    col_53200.alert = False
    col_53200.enabled = True
    col_53200.active = True
    col_53200.use_property_split = False
    col_53200.use_property_decorate = False
    col_53200.scale_x = 1.0
    col_53200.scale_y = 1.0
    col_53200.alignment = 'Expand'.upper()
    col_53200.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_CF71B = col_53200.row(heading='', align=False)
    row_CF71B.alert = False
    row_CF71B.enabled = True
    row_CF71B.active = True
    row_CF71B.use_property_split = False
    row_CF71B.use_property_decorate = False
    row_CF71B.scale_x = 1.0
    row_CF71B.scale_y = 1.0
    row_CF71B.alignment = 'Expand'.upper()
    row_CF71B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_CF71B.label(text='Hue', icon_value=0)
    row_4F0AA = col_53200.row(heading='', align=False)
    row_4F0AA.alert = False
    row_4F0AA.enabled = True
    row_4F0AA.active = True
    row_4F0AA.use_property_split = False
    row_4F0AA.use_property_decorate = False
    row_4F0AA.scale_x = 1.0
    row_4F0AA.scale_y = 1.0
    row_4F0AA.alignment = 'Expand'.upper()
    row_4F0AA.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_4F0AA.label(text='Saturation', icon_value=0)
    row_F7F5C = col_53200.row(heading='', align=False)
    row_F7F5C.alert = False
    row_F7F5C.enabled = True
    row_F7F5C.active = True
    row_F7F5C.use_property_split = False
    row_F7F5C.use_property_decorate = False
    row_F7F5C.scale_x = 1.0
    row_F7F5C.scale_y = 1.0
    row_F7F5C.alignment = 'Expand'.upper()
    row_F7F5C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_F7F5C.label(text='Value', icon_value=0)
    col_EC924 = split_1FDFB.column(heading='', align=False)
    col_EC924.alert = False
    col_EC924.enabled = True
    col_EC924.active = True
    col_EC924.use_property_split = False
    col_EC924.use_property_decorate = False
    col_EC924.scale_x = 1.0
    col_EC924.scale_y = 1.0
    col_EC924.alignment = 'Expand'.upper()
    col_EC924.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_3767E = col_EC924.row(heading='', align=False)
    row_3767E.alert = False
    row_3767E.enabled = True
    row_3767E.active = True
    row_3767E.use_property_split = False
    row_3767E.use_property_decorate = False
    row_3767E.scale_x = 1.0
    row_3767E.scale_y = 1.0
    row_3767E.alignment = 'Expand'.upper()
    row_3767E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_3767E.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[0], 'default_value', text='', icon_value=0, emboss=True)
    row_2885E = col_EC924.row(heading='', align=False)
    row_2885E.alert = False
    row_2885E.enabled = True
    row_2885E.active = True
    row_2885E.use_property_split = False
    row_2885E.use_property_decorate = False
    row_2885E.scale_x = 1.0
    row_2885E.scale_y = 1.0
    row_2885E.alignment = 'Expand'.upper()
    row_2885E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_2885E.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[1], 'default_value', text='', icon_value=0, emboss=True)
    row_B23D1 = col_EC924.row(heading='', align=False)
    row_B23D1.alert = False
    row_B23D1.enabled = True
    row_B23D1.active = True
    row_B23D1.use_property_split = False
    row_B23D1.use_property_decorate = False
    row_B23D1.scale_x = 1.0
    row_B23D1.scale_y = 1.0
    row_B23D1.alignment = 'Expand'.upper()
    row_B23D1.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_B23D1.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[2], 'default_value', text='', icon_value=0, emboss=True)


def sna_colorramp_display_3BC97(layout_function, node_name):
    col_2A041 = layout_function.column(heading='', align=False)
    col_2A041.alert = False
    col_2A041.enabled = True
    col_2A041.active = True
    col_2A041.use_property_split = False
    col_2A041.use_property_decorate = False
    col_2A041.scale_x = 1.0
    col_2A041.scale_y = 1.5
    col_2A041.alignment = 'Expand'.upper()
    col_2A041.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    col_2A041.template_color_ramp((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active.active_material.name)].material.node_tree.nodes[node_name], "color_ramp")


def sna_density_A2816(layout_function, node_name, label_name, integer_switch):
    for i_B4339 in range(len((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes)):
        if ((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes[i_B4339].name == node_name):
            col_C6730 = layout_function.column(heading='', align=False)
            col_C6730.alert = False
            col_C6730.enabled = True
            col_C6730.active = True
            col_C6730.use_property_split = False
            col_C6730.use_property_decorate = False
            col_C6730.scale_x = 1.0
            col_C6730.scale_y = 1.0
            col_C6730.alignment = 'Expand'.upper()
            col_C6730.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_1AEE5 = col_C6730.column(heading='', align=False)
            col_1AEE5.alert = False
            col_1AEE5.enabled = True
            col_1AEE5.active = True
            col_1AEE5.use_property_split = False
            col_1AEE5.use_property_decorate = False
            col_1AEE5.scale_x = 1.0
            col_1AEE5.scale_y = 1.0
            col_1AEE5.alignment = 'Expand'.upper()
            col_1AEE5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_1AEE5.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[(2 if integer_switch else 1)], 'default_value', text=label_name, icon_value=0, emboss=True)


def sna_enum_vdbs_enum_items(self, context):
    enum_items = [['Aerial Explosion6', 'Aerial Explosion6', 'Aerial Explosion6', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Aerial Explosion6.png'))], ['Big Ground Explosion2', 'Big Ground Explosion2', 'Big Ground Explosion2', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Big Ground Explosion2.png'))], ['Cloud1', 'Cloud1', 'Cloud1', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Cloud1.png'))], ['Cloud19', 'Cloud19', 'Cloud19', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Cloud19.png'))], ['Heavy Smoke1', 'Heavy Smoke1', 'Heavy Smoke1', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Heavy Smoke1.png'))], ['Smoke Shockwave1', 'Smoke Shockwave1', 'Smoke Shockwave1', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Smoke Shockwave1.png'))], ['Get More Presets', 'Get More Presets', 'Get More Presets', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'IMG_2907.png'))]]
    return [make_enum_item(item[0], item[1], item[2], item[3], i) for i, item in enumerate(enum_items)]


def sna_enum_volumes_enum_items(self, context):
    enum_items = [['GodRay Fog', 'GodRay Fog', 'GodRay Fog', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Godrayfog.png'))], ['Ground Fog11', 'Ground Fog11', 'Ground Fog11', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Ground Fog11.png'))], ['Get More Presets', 'Get More Presets', 'Get More Presets', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'IMG_2907.png'))]]
    return [make_enum_item(item[0], item[1], item[2], item[3], i) for i, item in enumerate(enum_items)]


class SNA_OT_Enumselectorplanes_A688C(bpy.types.Operator):
    bl_idname = "sna.enumselectorplanes_a688c"
    bl_label = "EnumSelectorPLANES"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_modeselectenum = 'Planes'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Enumselectorvolumes_D5052(bpy.types.Operator):
    bl_idname = "sna.enumselectorvolumes_d5052"
    bl_label = "EnumSelectorVOLUMES"
    bl_description = "Show Volumes"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_modeselectenum = 'Volumes'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Enumselectorvdbs_E7824(bpy.types.Operator):
    bl_idname = "sna.enumselectorvdbs_e7824"
    bl_label = "EnumSelectorVDBs"
    bl_description = "Show VDBs"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_modeselectenum = 'VDBs'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Fogpropenumselectordensity_B75B0(bpy.types.Operator):
    bl_idname = "sna.fogpropenumselectordensity_b75b0"
    bl_label = "FogPropEnumSelectorDensity"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_fogpropenum = 'DensityTog'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Fogpropenumselectornoise_Fb05E(bpy.types.Operator):
    bl_idname = "sna.fogpropenumselectornoise_fb05e"
    bl_label = "FogPropEnumSelectorNoise"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_fogpropenum = 'NoiseTog'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Fogpropenumselectormapping_9A4E8(bpy.types.Operator):
    bl_idname = "sna.fogpropenumselectormapping_9a4e8"
    bl_label = "FogPropEnumSelectorMapping"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_fogpropenum = 'MappingTog'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Fog_It_Up_Vdb_20Dfb(bpy.types.Operator):
    bl_idname = "sna.fog_it_up_vdb_20dfb"
    bl_label = "Fog It Up VDB"
    bl_description = "Add selected preset to 3D cursor"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.scene.sna_show_vdb_category == 'All'):
            sna_append_and_center_vdb_EB13F(bpy.context.scene.sna_enum_vdbs)
        else:
            if (bpy.context.scene.sna_show_vdb_category == 'Explosions'):
                sna_append_and_center_vdb_EB13F(bpy.context.scene.sna_explosions)
            else:
                if (bpy.context.scene.sna_show_vdb_category == 'Smokes'):
                    sna_append_and_center_vdb_EB13F(bpy.context.scene.sna_smokes)
                else:
                    if (bpy.context.scene.sna_show_vdb_category == 'Clouds'):
                        sna_append_and_center_vdb_EB13F(bpy.context.scene.sna_clouds)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Fog_It_Up_Volume_D3482(bpy.types.Operator):
    bl_idname = "sna.fog_it_up_volume_d3482"
    bl_label = "Fog It Up Volume"
    bl_description = "Add selected preset to 3D cursor"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (bpy.context.scene.sna_show_volume_category == 'All'):
            sna_append_and_center_volumes_02B1C(bpy.context.scene.sna_enum_volumes)
        else:
            if (bpy.context.scene.sna_show_volume_category == 'Ground Fogs'):
                sna_append_and_center_volumes_02B1C(bpy.context.scene.sna_ground_fogs)
            else:
                if (bpy.context.scene.sna_show_volume_category == 'Fog Planes & Puffs'):
                    sna_append_and_center_volumes_02B1C(bpy.context.scene.sna_fog_planes_and_puffs)
                else:
                    if (bpy.context.scene.sna_show_volume_category == 'Tornado'):
                        sna_append_and_center_volumes_02B1C(bpy.context.scene.sna_tornado)
                    else:
                        if (bpy.context.scene.sna_show_volume_category == 'Magic & Other'):
                            sna_append_and_center_volumes_02B1C(bpy.context.scene.sna_magic__other)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_append_and_center_vdb_EB13F(NAME_TO_APPEND):
    # Define the collection name
    collection_name = "Alt Tab Easy Fog"
    # Function to check if the collection exists in the current scene

    def collection_exists_in_scene(name, scene):
        return any(col.name == name for col in scene.collection.children)
    # Function to create a new collection and link it to the current scene

    def create_and_link_collection_to_scene(name, scene):
        if name not in bpy.data.collections:  # Check if collection exists in the blend file
            new_collection = bpy.data.collections.new(name)  # Create new collection
        else:
            new_collection = bpy.data.collections[name]  # Get existing collection
        # Link the collection to the current scene if it's not already linked
        if new_collection.name not in scene.collection.children:
            scene.collection.children.link(new_collection)
        return new_collection
    # Function to set a collection as active

    def set_active_collection(collection):

        def recurse_layer_collections(lc, name):
            for layer_collection in lc:
                if layer_collection.collection.name == name:
                    bpy.context.view_layer.active_layer_collection = layer_collection
                    return True
                if recurse_layer_collections(layer_collection.children, name):
                    return True
            return False
        if not recurse_layer_collections(bpy.context.view_layer.layer_collection.children, collection.name):
            print(f"Failed to set '{collection.name}' as the active collection.")
    # Function to set the color tag of a collection

    def set_collection_color_tag(collection, color_tag):
        collection.color_tag = color_tag
    # Main execution
    current_scene = bpy.context.scene  # Get the current scene
    # Check if the collection exists in the current scene, and create and link it if it doesn't
    if not collection_exists_in_scene(collection_name, current_scene):
        new_collection = create_and_link_collection_to_scene(collection_name, current_scene)
        print(f"Collection '{collection_name}' created and added to the current scene.")
    else:
        new_collection = bpy.data.collections.get(collection_name)
        print(f"Collection '{collection_name}' already exists in the current scene.")
    # Set the collection color tag to pink (COLOR_04)
    set_collection_color_tag(new_collection, 'COLOR_04')
    print(f"Collection '{collection_name}' color tag set to pink.")
    # Set the new or existing collection as the active collection
    set_active_collection(new_collection)
    print(f"Collection '{collection_name}' is now the active collection.")
    before_data = list(bpy.data.objects)
    bpy.ops.wm.append(directory=bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'VDB Demo.blend')) + r'\Object', filename=NAME_TO_APPEND, link=False)
    new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
    appended_7CC0D = None if not new_data else new_data[0]
    bpy.context.view_layer.objects.active = appended_7CC0D
    bpy.ops.view3d.snap_selected_to_cursor('INVOKE_DEFAULT', )
    bpy.ops.file.find_missing_files(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Demo Volumes'))


def sna_append_and_center_volumes_02B1C(APPEND_NAME):
    # Define the collection name
    collection_name = "Alt Tab Easy Fog"
    # Function to check if the collection exists in the current scene

    def collection_exists_in_scene(name, scene):
        return any(col.name == name for col in scene.collection.children)
    # Function to create a new collection and link it to the current scene

    def create_and_link_collection_to_scene(name, scene):
        if name not in bpy.data.collections:  # Check if collection exists in the blend file
            new_collection = bpy.data.collections.new(name)  # Create new collection
        else:
            new_collection = bpy.data.collections[name]  # Get existing collection
        # Link the collection to the current scene if it's not already linked
        if new_collection.name not in scene.collection.children:
            scene.collection.children.link(new_collection)
        return new_collection
    # Function to set a collection as active

    def set_active_collection(collection):

        def recurse_layer_collections(lc, name):
            for layer_collection in lc:
                if layer_collection.collection.name == name:
                    bpy.context.view_layer.active_layer_collection = layer_collection
                    return True
                if recurse_layer_collections(layer_collection.children, name):
                    return True
            return False
        if not recurse_layer_collections(bpy.context.view_layer.layer_collection.children, collection.name):
            print(f"Failed to set '{collection.name}' as the active collection.")
    # Function to set the color tag of a collection

    def set_collection_color_tag(collection, color_tag):
        collection.color_tag = color_tag
    # Main execution
    current_scene = bpy.context.scene  # Get the current scene
    # Check if the collection exists in the current scene, and create and link it if it doesn't
    if not collection_exists_in_scene(collection_name, current_scene):
        new_collection = create_and_link_collection_to_scene(collection_name, current_scene)
        print(f"Collection '{collection_name}' created and added to the current scene.")
    else:
        new_collection = bpy.data.collections.get(collection_name)
        print(f"Collection '{collection_name}' already exists in the current scene.")
    # Set the collection color tag to pink (COLOR_04)
    set_collection_color_tag(new_collection, 'COLOR_04')
    print(f"Collection '{collection_name}' color tag set to pink.")
    # Set the new or existing collection as the active collection
    set_active_collection(new_collection)
    print(f"Collection '{collection_name}' is now the active collection.")
    before_data = list(bpy.data.objects)
    bpy.ops.wm.append(directory=bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'FogVolumesDemo.blend')) + r'\Object', filename=APPEND_NAME, link=False)
    new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
    appended_25590 = None if not new_data else new_data[0]
    bpy.context.view_layer.objects.active = appended_25590
    bpy.ops.view3d.snap_selected_to_cursor('INVOKE_DEFAULT', )


class SNA_PT_ALT_TAB_EASY_FOG_2_DEMO_E4563(bpy.types.Panel):
    bl_label = 'Alt Tab Easy Fog 2 Demo'
    bl_idname = 'SNA_PT_ALT_TAB_EASY_FOG_2_DEMO_E4563'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Alt Tab Easy Fog 2'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_05264 = layout.row(heading='', align=False)
        row_05264.alert = False
        row_05264.enabled = True
        row_05264.active = True
        row_05264.use_property_split = False
        row_05264.use_property_decorate = False
        row_05264.scale_x = 1.0
        row_05264.scale_y = 1.1100000143051147
        row_05264.alignment = 'Expand'.upper()
        row_05264.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_05264.operator('sna.enumselectorvolumes_d5052', text='Volumes', icon_value=583, emboss=True, depress=(bpy.context.scene.sna_modeselectenum == 'Volumes'))
        op = row_05264.operator('sna.enumselectorvdbs_e7824', text='VDBs', icon_value=657, emboss=True, depress=(bpy.context.scene.sna_modeselectenum == 'VDBs'))
        if bpy.context.scene.sna_modeselectenum == "Volumes":
            if bpy.context.scene.sna_show_volume_category == "All":
                col_1C91B = layout.column(heading='', align=False)
                col_1C91B.alert = False
                col_1C91B.enabled = True
                col_1C91B.active = True
                col_1C91B.use_property_split = False
                col_1C91B.use_property_decorate = False
                col_1C91B.scale_x = 1.0
                col_1C91B.scale_y = 1.0
                col_1C91B.alignment = 'Expand'.upper()
                col_1C91B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_8DBEA = col_1C91B.row(heading='', align=False)
                row_8DBEA.alert = False
                row_8DBEA.enabled = True
                row_8DBEA.active = True
                row_8DBEA.use_property_split = False
                row_8DBEA.use_property_decorate = False
                row_8DBEA.scale_x = 1.0
                row_8DBEA.scale_y = 1.0
                row_8DBEA.alignment = 'Expand'.upper()
                row_8DBEA.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_8DBEA.template_icon_view(bpy.context.scene, 'sna_enum_volumes', show_labels=True, scale=5.0, scale_popup=bpy.context.preferences.addons['alt_tab_easy_fog_2_demo'].preferences.sna_image_ui_scale)
                row_C9FF0 = col_1C91B.row(heading='', align=False)
                row_C9FF0.alert = False
                row_C9FF0.enabled = True
                row_C9FF0.active = True
                row_C9FF0.use_property_split = False
                row_C9FF0.use_property_decorate = False
                row_C9FF0.scale_x = 1.0
                row_C9FF0.scale_y = 1.5
                row_C9FF0.alignment = 'Expand'.upper()
                row_C9FF0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_C9FF0.operator('sna.fog_it_up_volume_d3482', text='Fog It Up!', icon_value=0, emboss=True, depress=False)
            elif bpy.context.scene.sna_show_volume_category == "Ground Fogs":
                col_0B693 = layout.column(heading='', align=False)
                col_0B693.alert = False
                col_0B693.enabled = True
                col_0B693.active = True
                col_0B693.use_property_split = False
                col_0B693.use_property_decorate = False
                col_0B693.scale_x = 1.0
                col_0B693.scale_y = 1.0
                col_0B693.alignment = 'Expand'.upper()
                col_0B693.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_63AE9 = col_0B693.row(heading='', align=False)
                row_63AE9.alert = False
                row_63AE9.enabled = True
                row_63AE9.active = True
                row_63AE9.use_property_split = False
                row_63AE9.use_property_decorate = False
                row_63AE9.scale_x = 1.0
                row_63AE9.scale_y = 1.5399999618530273
                row_63AE9.alignment = 'Expand'.upper()
                row_63AE9.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_2C2D3 = col_0B693.row(heading='', align=False)
                row_2C2D3.alert = False
                row_2C2D3.enabled = True
                row_2C2D3.active = True
                row_2C2D3.use_property_split = False
                row_2C2D3.use_property_decorate = False
                row_2C2D3.scale_x = 1.0
                row_2C2D3.scale_y = 1.0
                row_2C2D3.alignment = 'Expand'.upper()
                row_2C2D3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_2C2D3.template_icon_view(bpy.context.scene, 'sna_ground_fogs', show_labels=True, scale=5.0, scale_popup=bpy.context.preferences.addons['alt_tab_easy_fog_2_demo'].preferences.sna_image_ui_scale)
                row_B6A30 = col_0B693.row(heading='', align=False)
                row_B6A30.alert = False
                row_B6A30.enabled = True
                row_B6A30.active = True
                row_B6A30.use_property_split = False
                row_B6A30.use_property_decorate = False
                row_B6A30.scale_x = 1.0
                row_B6A30.scale_y = 1.5
                row_B6A30.alignment = 'Expand'.upper()
                row_B6A30.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_B6A30.operator('sna.fog_it_up_volume_d3482', text='Fog It Up!', icon_value=0, emboss=True, depress=False)
            elif bpy.context.scene.sna_show_volume_category == "Fog Planes & Puffs":
                col_A5286 = layout.column(heading='', align=False)
                col_A5286.alert = False
                col_A5286.enabled = True
                col_A5286.active = True
                col_A5286.use_property_split = False
                col_A5286.use_property_decorate = False
                col_A5286.scale_x = 1.0
                col_A5286.scale_y = 1.0
                col_A5286.alignment = 'Expand'.upper()
                col_A5286.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_48125 = col_A5286.row(heading='', align=False)
                row_48125.alert = False
                row_48125.enabled = True
                row_48125.active = True
                row_48125.use_property_split = False
                row_48125.use_property_decorate = False
                row_48125.scale_x = 1.0
                row_48125.scale_y = 1.5399999618530273
                row_48125.alignment = 'Expand'.upper()
                row_48125.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_8BED4 = col_A5286.row(heading='', align=False)
                row_8BED4.alert = False
                row_8BED4.enabled = True
                row_8BED4.active = True
                row_8BED4.use_property_split = False
                row_8BED4.use_property_decorate = False
                row_8BED4.scale_x = 1.0
                row_8BED4.scale_y = 1.0
                row_8BED4.alignment = 'Expand'.upper()
                row_8BED4.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_8BED4.template_icon_view(bpy.context.scene, 'sna_fog_planes_and_puffs', show_labels=True, scale=5.0, scale_popup=bpy.context.preferences.addons['alt_tab_easy_fog_2_demo'].preferences.sna_image_ui_scale)
                row_B62DE = col_A5286.row(heading='', align=False)
                row_B62DE.alert = False
                row_B62DE.enabled = True
                row_B62DE.active = True
                row_B62DE.use_property_split = False
                row_B62DE.use_property_decorate = False
                row_B62DE.scale_x = 1.0
                row_B62DE.scale_y = 1.5
                row_B62DE.alignment = 'Expand'.upper()
                row_B62DE.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_B62DE.operator('sna.fog_it_up_volume_d3482', text='Fog It Up!', icon_value=0, emboss=True, depress=False)
            elif bpy.context.scene.sna_show_volume_category == "Tornado":
                col_30EEB = layout.column(heading='', align=False)
                col_30EEB.alert = False
                col_30EEB.enabled = True
                col_30EEB.active = True
                col_30EEB.use_property_split = False
                col_30EEB.use_property_decorate = False
                col_30EEB.scale_x = 1.0
                col_30EEB.scale_y = 1.0
                col_30EEB.alignment = 'Expand'.upper()
                col_30EEB.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_642BE = col_30EEB.row(heading='', align=False)
                row_642BE.alert = False
                row_642BE.enabled = True
                row_642BE.active = True
                row_642BE.use_property_split = False
                row_642BE.use_property_decorate = False
                row_642BE.scale_x = 1.0
                row_642BE.scale_y = 1.5399999618530273
                row_642BE.alignment = 'Expand'.upper()
                row_642BE.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_BEFE8 = col_30EEB.row(heading='', align=False)
                row_BEFE8.alert = False
                row_BEFE8.enabled = True
                row_BEFE8.active = True
                row_BEFE8.use_property_split = False
                row_BEFE8.use_property_decorate = False
                row_BEFE8.scale_x = 1.0
                row_BEFE8.scale_y = 1.0
                row_BEFE8.alignment = 'Expand'.upper()
                row_BEFE8.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_BEFE8.template_icon_view(bpy.context.scene, 'sna_tornado', show_labels=True, scale=5.0, scale_popup=bpy.context.preferences.addons['alt_tab_easy_fog_2_demo'].preferences.sna_image_ui_scale)
                row_63B31 = col_30EEB.row(heading='', align=False)
                row_63B31.alert = False
                row_63B31.enabled = True
                row_63B31.active = True
                row_63B31.use_property_split = False
                row_63B31.use_property_decorate = False
                row_63B31.scale_x = 1.0
                row_63B31.scale_y = 1.5
                row_63B31.alignment = 'Expand'.upper()
                row_63B31.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_63B31.operator('sna.fog_it_up_volume_d3482', text='Fog It Up!', icon_value=0, emboss=True, depress=False)
            elif bpy.context.scene.sna_show_volume_category == "Magic & Other":
                col_8F48D = layout.column(heading='', align=False)
                col_8F48D.alert = False
                col_8F48D.enabled = True
                col_8F48D.active = True
                col_8F48D.use_property_split = False
                col_8F48D.use_property_decorate = False
                col_8F48D.scale_x = 1.0
                col_8F48D.scale_y = 1.0
                col_8F48D.alignment = 'Expand'.upper()
                col_8F48D.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_5A6EC = col_8F48D.row(heading='', align=False)
                row_5A6EC.alert = False
                row_5A6EC.enabled = True
                row_5A6EC.active = True
                row_5A6EC.use_property_split = False
                row_5A6EC.use_property_decorate = False
                row_5A6EC.scale_x = 1.0
                row_5A6EC.scale_y = 1.5399999618530273
                row_5A6EC.alignment = 'Expand'.upper()
                row_5A6EC.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_7BDA2 = col_8F48D.row(heading='', align=False)
                row_7BDA2.alert = False
                row_7BDA2.enabled = True
                row_7BDA2.active = True
                row_7BDA2.use_property_split = False
                row_7BDA2.use_property_decorate = False
                row_7BDA2.scale_x = 1.0
                row_7BDA2.scale_y = 1.0
                row_7BDA2.alignment = 'Expand'.upper()
                row_7BDA2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_7BDA2.template_icon_view(bpy.context.scene, 'sna_magic__other', show_labels=True, scale=5.0, scale_popup=bpy.context.preferences.addons['alt_tab_easy_fog_2_demo'].preferences.sna_image_ui_scale)
                row_70DD2 = col_8F48D.row(heading='', align=False)
                row_70DD2.alert = False
                row_70DD2.enabled = True
                row_70DD2.active = True
                row_70DD2.use_property_split = False
                row_70DD2.use_property_decorate = False
                row_70DD2.scale_x = 1.0
                row_70DD2.scale_y = 1.5
                row_70DD2.alignment = 'Expand'.upper()
                row_70DD2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_70DD2.operator('sna.fog_it_up_volume_d3482', text='Fog It Up!', icon_value=0, emboss=True, depress=False)
            else:
                pass
        elif bpy.context.scene.sna_modeselectenum == "VDBs":
            if bpy.context.scene.sna_show_vdb_category == "All":
                col_732A8 = layout.column(heading='', align=False)
                col_732A8.alert = False
                col_732A8.enabled = True
                col_732A8.active = True
                col_732A8.use_property_split = False
                col_732A8.use_property_decorate = False
                col_732A8.scale_x = 1.0
                col_732A8.scale_y = 1.0
                col_732A8.alignment = 'Expand'.upper()
                col_732A8.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_E8C23 = col_732A8.row(heading='', align=False)
                row_E8C23.alert = False
                row_E8C23.enabled = True
                row_E8C23.active = True
                row_E8C23.use_property_split = False
                row_E8C23.use_property_decorate = False
                row_E8C23.scale_x = 1.0
                row_E8C23.scale_y = 1.5399999618530273
                row_E8C23.alignment = 'Expand'.upper()
                row_E8C23.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_F0012 = col_732A8.row(heading='', align=False)
                row_F0012.alert = False
                row_F0012.enabled = True
                row_F0012.active = True
                row_F0012.use_property_split = False
                row_F0012.use_property_decorate = False
                row_F0012.scale_x = 1.0
                row_F0012.scale_y = 1.0
                row_F0012.alignment = 'Expand'.upper()
                row_F0012.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_F0012.template_icon_view(bpy.context.scene, 'sna_enum_vdbs', show_labels=True, scale=5.0, scale_popup=bpy.context.preferences.addons['alt_tab_easy_fog_2_demo'].preferences.sna_image_ui_scale)
                row_7390B = col_732A8.row(heading='', align=False)
                row_7390B.alert = False
                row_7390B.enabled = True
                row_7390B.active = True
                row_7390B.use_property_split = False
                row_7390B.use_property_decorate = False
                row_7390B.scale_x = 1.0
                row_7390B.scale_y = 1.5
                row_7390B.alignment = 'Expand'.upper()
                row_7390B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_7390B.operator('sna.fog_it_up_vdb_20dfb', text='Fog It Up!', icon_value=0, emboss=True, depress=False)
            elif bpy.context.scene.sna_show_vdb_category == "Explosions":
                col_634CF = layout.column(heading='', align=False)
                col_634CF.alert = False
                col_634CF.enabled = True
                col_634CF.active = True
                col_634CF.use_property_split = False
                col_634CF.use_property_decorate = False
                col_634CF.scale_x = 1.0
                col_634CF.scale_y = 1.0
                col_634CF.alignment = 'Expand'.upper()
                col_634CF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_6E9C9 = col_634CF.row(heading='', align=False)
                row_6E9C9.alert = False
                row_6E9C9.enabled = True
                row_6E9C9.active = True
                row_6E9C9.use_property_split = False
                row_6E9C9.use_property_decorate = False
                row_6E9C9.scale_x = 1.0
                row_6E9C9.scale_y = 1.5399999618530273
                row_6E9C9.alignment = 'Expand'.upper()
                row_6E9C9.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_3AD6B = col_634CF.row(heading='', align=False)
                row_3AD6B.alert = False
                row_3AD6B.enabled = True
                row_3AD6B.active = True
                row_3AD6B.use_property_split = False
                row_3AD6B.use_property_decorate = False
                row_3AD6B.scale_x = 1.0
                row_3AD6B.scale_y = 1.0
                row_3AD6B.alignment = 'Expand'.upper()
                row_3AD6B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_3AD6B.template_icon_view(bpy.context.scene, 'sna_explosions', show_labels=True, scale=5.0, scale_popup=bpy.context.preferences.addons['alt_tab_easy_fog_2_demo'].preferences.sna_image_ui_scale)
                row_E91D5 = col_634CF.row(heading='', align=False)
                row_E91D5.alert = False
                row_E91D5.enabled = True
                row_E91D5.active = True
                row_E91D5.use_property_split = False
                row_E91D5.use_property_decorate = False
                row_E91D5.scale_x = 1.0
                row_E91D5.scale_y = 1.5
                row_E91D5.alignment = 'Expand'.upper()
                row_E91D5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_E91D5.operator('sna.fog_it_up_vdb_20dfb', text='Fog It Up!', icon_value=0, emboss=True, depress=False)
            elif bpy.context.scene.sna_show_vdb_category == "Smokes":
                col_EA15E = layout.column(heading='', align=False)
                col_EA15E.alert = False
                col_EA15E.enabled = True
                col_EA15E.active = True
                col_EA15E.use_property_split = False
                col_EA15E.use_property_decorate = False
                col_EA15E.scale_x = 1.0
                col_EA15E.scale_y = 1.0
                col_EA15E.alignment = 'Expand'.upper()
                col_EA15E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_3530A = col_EA15E.row(heading='', align=False)
                row_3530A.alert = False
                row_3530A.enabled = True
                row_3530A.active = True
                row_3530A.use_property_split = False
                row_3530A.use_property_decorate = False
                row_3530A.scale_x = 1.0
                row_3530A.scale_y = 1.5399999618530273
                row_3530A.alignment = 'Expand'.upper()
                row_3530A.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_ED89C = col_EA15E.row(heading='', align=False)
                row_ED89C.alert = False
                row_ED89C.enabled = True
                row_ED89C.active = True
                row_ED89C.use_property_split = False
                row_ED89C.use_property_decorate = False
                row_ED89C.scale_x = 1.0
                row_ED89C.scale_y = 1.0
                row_ED89C.alignment = 'Expand'.upper()
                row_ED89C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_ED89C.template_icon_view(bpy.context.scene, 'sna_smokes', show_labels=True, scale=5.0, scale_popup=bpy.context.preferences.addons['alt_tab_easy_fog_2_demo'].preferences.sna_image_ui_scale)
                row_324AD = col_EA15E.row(heading='', align=False)
                row_324AD.alert = False
                row_324AD.enabled = True
                row_324AD.active = True
                row_324AD.use_property_split = False
                row_324AD.use_property_decorate = False
                row_324AD.scale_x = 1.0
                row_324AD.scale_y = 1.5
                row_324AD.alignment = 'Expand'.upper()
                row_324AD.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_324AD.operator('sna.fog_it_up_vdb_20dfb', text='Fog It Up!', icon_value=0, emboss=True, depress=False)
            elif bpy.context.scene.sna_show_vdb_category == "Clouds":
                col_EA8FE = layout.column(heading='', align=False)
                col_EA8FE.alert = False
                col_EA8FE.enabled = True
                col_EA8FE.active = True
                col_EA8FE.use_property_split = False
                col_EA8FE.use_property_decorate = False
                col_EA8FE.scale_x = 1.0
                col_EA8FE.scale_y = 1.0
                col_EA8FE.alignment = 'Expand'.upper()
                col_EA8FE.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_F5BCB = col_EA8FE.row(heading='', align=False)
                row_F5BCB.alert = False
                row_F5BCB.enabled = True
                row_F5BCB.active = True
                row_F5BCB.use_property_split = False
                row_F5BCB.use_property_decorate = False
                row_F5BCB.scale_x = 1.0
                row_F5BCB.scale_y = 1.5399999618530273
                row_F5BCB.alignment = 'Expand'.upper()
                row_F5BCB.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_5CE4B = col_EA8FE.row(heading='', align=False)
                row_5CE4B.alert = False
                row_5CE4B.enabled = True
                row_5CE4B.active = True
                row_5CE4B.use_property_split = False
                row_5CE4B.use_property_decorate = False
                row_5CE4B.scale_x = 1.0
                row_5CE4B.scale_y = 1.0
                row_5CE4B.alignment = 'Expand'.upper()
                row_5CE4B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_5CE4B.template_icon_view(bpy.context.scene, 'sna_clouds', show_labels=True, scale=5.0, scale_popup=bpy.context.preferences.addons['alt_tab_easy_fog_2_demo'].preferences.sna_image_ui_scale)
                row_FC6BF = col_EA8FE.row(heading='', align=False)
                row_FC6BF.alert = False
                row_FC6BF.enabled = True
                row_FC6BF.active = True
                row_FC6BF.use_property_split = False
                row_FC6BF.use_property_decorate = False
                row_FC6BF.scale_x = 1.0
                row_FC6BF.scale_y = 1.5
                row_FC6BF.alignment = 'Expand'.upper()
                row_FC6BF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_FC6BF.operator('sna.fog_it_up_vdb_20dfb', text='Fog It Up!', icon_value=0, emboss=True, depress=False)
            else:
                pass
        else:
            pass


def sna_mapping_B7727(layout_function, node_name):
    for i_7C349 in range(len((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes)):
        if ((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes[i_7C349].name == node_name):
            col_430EC = layout_function.column(heading='', align=False)
            col_430EC.alert = False
            col_430EC.enabled = True
            col_430EC.active = True
            col_430EC.use_property_split = False
            col_430EC.use_property_decorate = False
            col_430EC.scale_x = 1.0
            col_430EC.scale_y = 1.0
            col_430EC.alignment = 'Expand'.upper()
            col_430EC.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_430EC.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[1], 'default_value', text='Location', icon_value=0, emboss=True)
            col_430EC.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[2], 'default_value', text='Rotation', icon_value=0, emboss=True)
            col_430EC.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[3], 'default_value', text='Scale', icon_value=0, emboss=True)


def sna_ntexture_7D31A(layout_function, node_name, box_label):
    for i_7315C in range(len((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes)):
        if ((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes[i_7315C].name == node_name):
            col_01D84 = layout_function.column(heading='', align=False)
            col_01D84.alert = False
            col_01D84.enabled = True
            col_01D84.active = True
            col_01D84.use_property_split = False
            col_01D84.use_property_decorate = False
            col_01D84.scale_x = 1.0
            col_01D84.scale_y = 1.0
            col_01D84.alignment = 'Expand'.upper()
            col_01D84.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_01D84.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[1], 'default_value', text='Seed', icon_value=0, emboss=True)
            col_01D84.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[2], 'default_value', text='Scale', icon_value=0, emboss=True)
            col_01D84.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[3], 'default_value', text='Detail', icon_value=0, emboss=True)
            col_01D84.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[4], 'default_value', text='Roughness', icon_value=0, emboss=True)
            col_01D84.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[5], 'default_value', text='Lacunarity', icon_value=0, emboss=True)
            col_01D84.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].inputs[6], 'default_value', text='Distortion', icon_value=0, emboss=True)


@persistent
def load_post_handler_22468(dummy):
    bpy.context.scene.sna_modeselectenum = 'Volumes'


class SNA_OT_Pin_Settings_7A41C(bpy.types.Operator):
    bl_idname = "sna.pin_settings_7a41c"
    bl_label = "Pin Settings"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_pinbooleean:
            bpy.context.scene.sna_pinbooleean = False
        else:
            bpy.context.scene.sna_pinmaterialname = str(bpy.context.active_object.active_material.name)
            bpy.context.scene.sna_pinobject = bpy.context.view_layer.objects.active
            bpy.context.scene.sna_pinmaterialid = bpy.context.object.active_material
            bpy.context.scene.sna_pinbooleean = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_AddonPreferences_8B506(bpy.types.AddonPreferences):
    bl_idname = 'alt_tab_easy_fog_2_demo'
    sna_image_ui_scale: bpy.props.FloatProperty(name='IMAGE UI SCALE', description='Preview images scale', default=6.0, subtype='NONE', unit='NONE', min=2.0, max=20.0, step=10, precision=1)

    def draw(self, context):
        if not (False):
            layout = self.layout 
            col_A629B = layout.column(heading='', align=False)
            col_A629B.alert = False
            col_A629B.enabled = True
            col_A629B.active = True
            col_A629B.use_property_split = False
            col_A629B.use_property_decorate = False
            col_A629B.scale_x = 1.0
            col_A629B.scale_y = 1.0
            col_A629B.alignment = 'Expand'.upper()
            col_A629B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_11240 = col_A629B.row(heading='', align=False)
            row_11240.alert = False
            row_11240.enabled = True
            row_11240.active = True
            row_11240.use_property_split = False
            row_11240.use_property_decorate = False
            row_11240.scale_x = 1.0
            row_11240.scale_y = 1.5
            row_11240.alignment = 'Expand'.upper()
            row_11240.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            op = row_11240.operator('wm.url_open', text='Youtube', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'YoutubeLogo.png')), emboss=True, depress=False)
            op.url = 'https://www.youtube.com/@alttab3d'
            op = row_11240.operator('wm.url_open', text='Discord', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'DiscordLogo.png')), emboss=True, depress=False)
            op.url = 'https://discord.gg/fsKBW4kcRw'
            op = row_11240.operator('wm.url_open', text='Blendermarket', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'BlendermarketLogo.png')), emboss=True, depress=False)
            op.url = 'https://blendermarket.com/creators/alttab'
            col_A629B.separator(factor=1.0)
            row_4D786 = col_A629B.row(heading='', align=False)
            row_4D786.alert = False
            row_4D786.enabled = True
            row_4D786.active = True
            row_4D786.use_property_split = False
            row_4D786.use_property_decorate = False
            row_4D786.scale_x = 1.0
            row_4D786.scale_y = 1.5
            row_4D786.alignment = 'Expand'.upper()
            row_4D786.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_4D786.label(text='UI Settings', icon_value=233)
            row_90A4F = col_A629B.row(heading='', align=False)
            row_90A4F.alert = False
            row_90A4F.enabled = True
            row_90A4F.active = True
            row_90A4F.use_property_split = False
            row_90A4F.use_property_decorate = False
            row_90A4F.scale_x = 1.0
            row_90A4F.scale_y = 1.0
            row_90A4F.alignment = 'Expand'.upper()
            row_90A4F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_90A4F.label(text='Global Image preview scale', icon_value=0)
            row_90A4F.prop(bpy.context.preferences.addons['alt_tab_easy_fog_2_demo'].preferences, 'sna_image_ui_scale', text='', icon_value=0, emboss=True)


class SNA_PT_alt_tab_easy_fog_2_7C50C(bpy.types.Panel):
    bl_label = ''
    bl_idname = 'SNA_PT_alt_tab_easy_fog_2_7C50C'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Alt Tab Easy Fog 2'
    bl_order = 2
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not ((not ((property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'DENSITY' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'DISRAMP' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'COLORHUE' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EMISSIONCOLOR' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EMISSION' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'FLAMEDIST' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'FLAMEINTENSITY' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'ABSORBHUE' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'HIGHLIGHTS' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'SHADOWS' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'NTEXTURE' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) or (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'MAP' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes))))

    def draw_header(self, context):
        layout = self.layout
        layout.label(text='Properties', icon_value=79)

    def draw(self, context):
        layout = self.layout
        if bpy.context.scene.sna_fogpropenum == "DensityTog":
            box_18C32 = layout.box()
            box_18C32.alert = False
            box_18C32.enabled = True
            box_18C32.active = True
            box_18C32.use_property_split = False
            box_18C32.use_property_decorate = False
            box_18C32.alignment = 'Expand'.upper()
            box_18C32.scale_x = 1.0
            box_18C32.scale_y = 1.0
            if not True: box_18C32.operator_context = "EXEC_DEFAULT"
            col_8BC78 = box_18C32.column(heading='', align=False)
            col_8BC78.alert = False
            col_8BC78.enabled = True
            col_8BC78.active = True
            col_8BC78.use_property_split = False
            col_8BC78.use_property_decorate = False
            col_8BC78.scale_x = 1.0
            col_8BC78.scale_y = 1.0
            col_8BC78.alignment = 'Expand'.upper()
            col_8BC78.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_69A50 = col_8BC78.row(heading='', align=False)
            row_69A50.alert = False
            row_69A50.enabled = True
            row_69A50.active = True
            row_69A50.use_property_split = False
            row_69A50.use_property_decorate = False
            row_69A50.scale_x = 1.0
            row_69A50.scale_y = 1.1710000038146973
            row_69A50.alignment = 'Expand'.upper()
            row_69A50.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_094E9 = row_69A50.row(heading='', align=False)
            row_094E9.alert = False
            row_094E9.enabled = False
            row_094E9.active = False
            row_094E9.use_property_split = False
            row_094E9.use_property_decorate = False
            row_094E9.scale_x = 1.0
            row_094E9.scale_y = 1.0
            row_094E9.alignment = 'Expand'.upper()
            row_094E9.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_094E9.label(text=' ' + (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).name, icon_value=0)
            op = row_69A50.operator('sna.pin_settings_7a41c', text='', icon_value=(43 if bpy.context.scene.sna_pinbooleean else 42), emboss=False, depress=True)
            box_36BC5 = col_8BC78.box()
            box_36BC5.alert = False
            box_36BC5.enabled = True
            box_36BC5.active = True
            box_36BC5.use_property_split = False
            box_36BC5.use_property_decorate = False
            box_36BC5.alignment = 'Expand'.upper()
            box_36BC5.scale_x = 1.0
            box_36BC5.scale_y = 1.0
            if not True: box_36BC5.operator_context = "EXEC_DEFAULT"
            col_C8B20 = box_36BC5.column(heading='', align=False)
            col_C8B20.alert = False
            col_C8B20.enabled = True
            col_C8B20.active = True
            col_C8B20.use_property_split = False
            col_C8B20.use_property_decorate = False
            col_C8B20.scale_x = 1.0
            col_C8B20.scale_y = 1.0
            col_C8B20.alignment = 'Expand'.upper()
            col_C8B20.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_1321E = col_C8B20.row(heading='', align=False)
            row_1321E.alert = False
            row_1321E.enabled = True
            row_1321E.active = True
            row_1321E.use_property_split = True
            row_1321E.use_property_decorate = False
            row_1321E.scale_x = 1.0
            row_1321E.scale_y = 2.0
            row_1321E.alignment = 'Left'.upper()
            row_1321E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_ED09D = row_1321E.column(heading='', align=False)
            col_ED09D.alert = False
            col_ED09D.enabled = True
            col_ED09D.active = True
            col_ED09D.use_property_split = True
            col_ED09D.use_property_decorate = False
            col_ED09D.scale_x = 1.0
            col_ED09D.scale_y = 1.0
            col_ED09D.alignment = 'Left'.upper()
            col_ED09D.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            op = col_ED09D.operator('sna.col_operator_adcef', text='Density', icon_value=(5 if bpy.context.scene.sna_collapse_bool_1 else 4), emboss=False, depress=False)
            row_E9043 = row_1321E.row(heading='', align=False)
            row_E9043.alert = False
            row_E9043.enabled = True
            row_E9043.active = True
            row_E9043.use_property_split = True
            row_E9043.use_property_decorate = False
            row_E9043.scale_x = 100.0
            row_E9043.scale_y = 1.0
            row_E9043.alignment = 'Right'.upper()
            row_E9043.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            op = row_E9043.operator('sna.col_operator_adcef', text='', icon_value=0, emboss=False, depress=False)
            op = row_1321E.operator('sna.col_operator_adcef', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Density.png')), emboss=False, depress=True)
            if bpy.context.scene.sna_collapse_bool_1:
                col_8C59E = col_C8B20.column(heading='', align=False)
                col_8C59E.alert = False
                col_8C59E.enabled = True
                col_8C59E.active = True
                col_8C59E.use_property_split = False
                col_8C59E.use_property_decorate = False
                col_8C59E.scale_x = 1.0
                col_8C59E.scale_y = 1.0
                col_8C59E.alignment = 'Expand'.upper()
                col_8C59E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_A307F = col_8C59E.row(heading='', align=False)
                row_A307F.alert = False
                row_A307F.enabled = True
                row_A307F.active = True
                row_A307F.use_property_split = False
                row_A307F.use_property_decorate = False
                row_A307F.scale_x = 1.0
                row_A307F.scale_y = 1.5
                row_A307F.alignment = 'Expand'.upper()
                row_A307F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'DENSITY' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                    if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['DENSITY']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                        col_8E401 = row_A307F.column(heading='', align=False)
                        col_8E401.alert = False
                        col_8E401.enabled = True
                        col_8E401.active = True
                        col_8E401.use_property_split = False
                        col_8E401.use_property_decorate = False
                        col_8E401.scale_x = 1.0
                        col_8E401.scale_y = 1.0
                        col_8E401.alignment = 'Expand'.upper()
                        col_8E401.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                        row_1F803 = col_8E401.row(heading='', align=False)
                        row_1F803.alert = False
                        row_1F803.enabled = True
                        row_1F803.active = True
                        row_1F803.use_property_split = False
                        row_1F803.use_property_decorate = False
                        row_1F803.scale_x = 1.0
                        row_1F803.scale_y = 1.0
                        row_1F803.alignment = 'Expand'.upper()
                        row_1F803.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                        layout_function = row_1F803
                        sna_density_A2816(layout_function, 'DENSITY', 'Density', False)
                if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'DISRAMP' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                    col_8C59E.separator(factor=1.0)
                    box_949C9 = col_8C59E.box()
                    box_949C9.alert = False
                    box_949C9.enabled = True
                    box_949C9.active = True
                    box_949C9.use_property_split = False
                    box_949C9.use_property_decorate = False
                    box_949C9.alignment = 'Expand'.upper()
                    box_949C9.scale_x = 1.0
                    box_949C9.scale_y = 1.0
                    if not True: box_949C9.operator_context = "EXEC_DEFAULT"
                    col_62B4F = box_949C9.column(heading='', align=False)
                    col_62B4F.alert = False
                    col_62B4F.enabled = True
                    col_62B4F.active = True
                    col_62B4F.use_property_split = False
                    col_62B4F.use_property_decorate = False
                    col_62B4F.scale_x = 1.0
                    col_62B4F.scale_y = 1.0
                    col_62B4F.alignment = 'Expand'.upper()
                    col_62B4F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    col_62B4F.label(text='Density Distribution', icon_value=0)
                    if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'DISRAMP' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['DISRAMP']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                            layout_function = col_62B4F
                            sna_colorramp_display_3BC97(layout_function, 'DISRAMP')
                if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'CLOUD' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                    box_52BFF = col_8C59E.box()
                    box_52BFF.alert = False
                    box_52BFF.enabled = True
                    box_52BFF.active = True
                    box_52BFF.use_property_split = False
                    box_52BFF.use_property_decorate = False
                    box_52BFF.alignment = 'Expand'.upper()
                    box_52BFF.scale_x = 1.0
                    box_52BFF.scale_y = 1.0
                    if not True: box_52BFF.operator_context = "EXEC_DEFAULT"
                    box_52BFF.label(text='Highlights & Shadows', icon_value=0)
                    col_0F13A = box_52BFF.column(heading='', align=False)
                    col_0F13A.alert = False
                    col_0F13A.enabled = True
                    col_0F13A.active = True
                    col_0F13A.use_property_split = False
                    col_0F13A.use_property_decorate = False
                    col_0F13A.scale_x = 1.0
                    col_0F13A.scale_y = 1.0
                    col_0F13A.alignment = 'Expand'.upper()
                    col_0F13A.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    col_97D78 = col_0F13A.column(heading='', align=False)
                    col_97D78.alert = False
                    col_97D78.enabled = True
                    col_97D78.active = True
                    col_97D78.use_property_split = False
                    col_97D78.use_property_decorate = False
                    col_97D78.scale_x = 1.0
                    col_97D78.scale_y = 1.5
                    col_97D78.alignment = 'Expand'.upper()
                    col_97D78.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    col_5A01D = col_97D78.column(heading='', align=False)
                    col_5A01D.alert = False
                    col_5A01D.enabled = True
                    col_5A01D.active = True
                    col_5A01D.use_property_split = False
                    col_5A01D.use_property_decorate = False
                    col_5A01D.scale_x = 1.0
                    col_5A01D.scale_y = 1.0
                    col_5A01D.alignment = 'Expand'.upper()
                    col_5A01D.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'HIGHLIGHTS' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['HIGHLIGHTS']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                            layout_function = col_5A01D
                            sna_value_4D0A9(layout_function, 'HIGHLIGHTS', 'Highlights')
                    col_CE822 = col_97D78.column(heading='', align=False)
                    col_CE822.alert = False
                    col_CE822.enabled = True
                    col_CE822.active = True
                    col_CE822.use_property_split = False
                    col_CE822.use_property_decorate = False
                    col_CE822.scale_x = 1.0
                    col_CE822.scale_y = 1.0
                    col_CE822.alignment = 'Expand'.upper()
                    col_CE822.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'SHADOWS' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['SHADOWS']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                            layout_function = col_CE822
                            sna_value_4D0A9(layout_function, 'SHADOWS', 'Shadows')
            box_E253A = col_8BC78.box()
            box_E253A.alert = False
            box_E253A.enabled = True
            box_E253A.active = True
            box_E253A.use_property_split = False
            box_E253A.use_property_decorate = False
            box_E253A.alignment = 'Expand'.upper()
            box_E253A.scale_x = 1.0
            box_E253A.scale_y = 1.0
            if not True: box_E253A.operator_context = "EXEC_DEFAULT"
            col_C1AAF = box_E253A.column(heading='', align=False)
            col_C1AAF.alert = False
            col_C1AAF.enabled = True
            col_C1AAF.active = True
            col_C1AAF.use_property_split = False
            col_C1AAF.use_property_decorate = False
            col_C1AAF.scale_x = 1.0
            col_C1AAF.scale_y = 1.0
            col_C1AAF.alignment = 'Expand'.upper()
            col_C1AAF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_D4C2B = col_C1AAF.row(heading='', align=False)
            row_D4C2B.alert = False
            row_D4C2B.enabled = True
            row_D4C2B.active = True
            row_D4C2B.use_property_split = False
            row_D4C2B.use_property_decorate = False
            row_D4C2B.scale_x = 1.0
            row_D4C2B.scale_y = 2.0
            row_D4C2B.alignment = 'Left'.upper()
            row_D4C2B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_268B3 = row_D4C2B.column(heading='', align=False)
            col_268B3.alert = False
            col_268B3.enabled = True
            col_268B3.active = True
            col_268B3.use_property_split = False
            col_268B3.use_property_decorate = False
            col_268B3.scale_x = 1.0
            col_268B3.scale_y = 1.0
            col_268B3.alignment = 'Left'.upper()
            col_268B3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            op = col_268B3.operator('sna.col_operator_2_f7f90', text=('Smoke Color' if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EXPLOSION' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) else 'Color'), icon_value=(5 if bpy.context.scene.sna_collapse_bool_2 else 4), emboss=False, depress=False)
            row_5C331 = row_D4C2B.row(heading='', align=False)
            row_5C331.alert = False
            row_5C331.enabled = True
            row_5C331.active = True
            row_5C331.use_property_split = True
            row_5C331.use_property_decorate = False
            row_5C331.scale_x = 100.0
            row_5C331.scale_y = 1.0
            row_5C331.alignment = 'Right'.upper()
            row_5C331.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            op = row_5C331.operator('sna.col_operator_2_f7f90', text='', icon_value=0, emboss=False, depress=False)
            op = row_D4C2B.operator('sna.col_operator_2_f7f90', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Color.png')), emboss=False, depress=False)
            if bpy.context.scene.sna_collapse_bool_2:
                col_A185D = col_C1AAF.column(heading='', align=False)
                col_A185D.alert = False
                col_A185D.enabled = True
                col_A185D.active = True
                col_A185D.use_property_split = False
                col_A185D.use_property_decorate = False
                col_A185D.scale_x = 1.0
                col_A185D.scale_y = 1.0
                col_A185D.alignment = 'Expand'.upper()
                col_A185D.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                col_A862C = col_A185D.column(heading='', align=False)
                col_A862C.alert = False
                col_A862C.enabled = True
                col_A862C.active = True
                col_A862C.use_property_split = False
                col_A862C.use_property_decorate = False
                col_A862C.scale_x = 1.0
                col_A862C.scale_y = 1.0
                col_A862C.alignment = 'Expand'.upper()
                col_A862C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'COLORHUE' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                    if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['COLORHUE']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                        layout_function = col_A862C
                        sna_mixnode_FFD62(layout_function, 'COLORHUE')
                if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EMISSION' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                    if  not (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EXPLOSION' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        col_A185D.separator(factor=1.0)
                        box_3496B = col_A185D.box()
                        box_3496B.alert = False
                        box_3496B.enabled = True
                        box_3496B.active = True
                        box_3496B.use_property_split = False
                        box_3496B.use_property_decorate = False
                        box_3496B.alignment = 'Expand'.upper()
                        box_3496B.scale_x = 1.0
                        box_3496B.scale_y = 1.0
                        if not True: box_3496B.operator_context = "EXEC_DEFAULT"
                        col_F9977 = box_3496B.column(heading='', align=False)
                        col_F9977.alert = False
                        col_F9977.enabled = True
                        col_F9977.active = True
                        col_F9977.use_property_split = False
                        col_F9977.use_property_decorate = False
                        col_F9977.scale_x = 1.0
                        col_F9977.scale_y = 1.5
                        col_F9977.alignment = 'Expand'.upper()
                        col_F9977.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                        col_F9977.label(text='Emission', icon_value=0)
                        if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EMISSION' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                            if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['EMISSION']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                                layout_function = col_F9977
                                sna_density_A2816(layout_function, 'EMISSION', ('Emission' if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EMISSIONCOLOR' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) else 'Emission'), False)
                        if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EMISSIONCOLOR' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                            if  not (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EXPLOSION' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                                box_3496B.separator(factor=0.0010000000474974513)
                                col_89A69 = box_3496B.column(heading='', align=False)
                                col_89A69.alert = False
                                col_89A69.enabled = True
                                col_89A69.active = True
                                col_89A69.use_property_split = False
                                col_89A69.use_property_decorate = False
                                col_89A69.scale_x = 1.0
                                col_89A69.scale_y = 1.0
                                col_89A69.alignment = 'Expand'.upper()
                                col_89A69.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                                col_89A69.label(text='Emission Color', icon_value=0)
                                if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EMISSIONCOLOR' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                                    if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['EMISSIONCOLOR']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                                        layout_function = col_89A69
                                        sna_colorramp_display_3BC97(layout_function, 'EMISSIONCOLOR')
                if  not (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'CLOUD' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                    if  not (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EXPLOSION' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        col_A185D.separator(factor=1.0)
                        box_3498D = col_A185D.box()
                        box_3498D.alert = False
                        box_3498D.enabled = True
                        box_3498D.active = True
                        box_3498D.use_property_split = False
                        box_3498D.use_property_decorate = False
                        box_3498D.alignment = 'Expand'.upper()
                        box_3498D.scale_x = 1.0
                        box_3498D.scale_y = 1.0
                        if not True: box_3498D.operator_context = "EXEC_DEFAULT"
                        col_6DD1B = box_3498D.column(heading='', align=False)
                        col_6DD1B.alert = False
                        col_6DD1B.enabled = True
                        col_6DD1B.active = True
                        col_6DD1B.use_property_split = False
                        col_6DD1B.use_property_decorate = False
                        col_6DD1B.scale_x = 1.0
                        col_6DD1B.scale_y = 1.5
                        col_6DD1B.alignment = 'Expand'.upper()
                        col_6DD1B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                        col_6DD1B.label(text='Absorbtion', icon_value=0)
                        if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'ABSORBHUE' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                            if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['ABSORBHUE']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                                layout_function = col_6DD1B
                                sna_absorbhue_00A37(layout_function, 'ABSORBHUE', True)
            if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'NTEXTURE' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                box_DEDFF = col_8BC78.box()
                box_DEDFF.alert = False
                box_DEDFF.enabled = True
                box_DEDFF.active = True
                box_DEDFF.use_property_split = False
                box_DEDFF.use_property_decorate = False
                box_DEDFF.alignment = 'Expand'.upper()
                box_DEDFF.scale_x = 1.0
                box_DEDFF.scale_y = 1.0
                if not True: box_DEDFF.operator_context = "EXEC_DEFAULT"
                col_04727 = box_DEDFF.column(heading='', align=False)
                col_04727.alert = False
                col_04727.enabled = True
                col_04727.active = True
                col_04727.use_property_split = False
                col_04727.use_property_decorate = False
                col_04727.scale_x = 1.0
                col_04727.scale_y = 1.0
                col_04727.alignment = 'Expand'.upper()
                col_04727.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_6C3E9 = col_04727.row(heading='', align=False)
                row_6C3E9.alert = False
                row_6C3E9.enabled = True
                row_6C3E9.active = True
                row_6C3E9.use_property_split = False
                row_6C3E9.use_property_decorate = False
                row_6C3E9.scale_x = 1.0
                row_6C3E9.scale_y = 2.0
                row_6C3E9.alignment = 'Left'.upper()
                row_6C3E9.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                col_6DF1F = row_6C3E9.column(heading='', align=False)
                col_6DF1F.alert = False
                col_6DF1F.enabled = True
                col_6DF1F.active = True
                col_6DF1F.use_property_split = False
                col_6DF1F.use_property_decorate = False
                col_6DF1F.scale_x = 1.0
                col_6DF1F.scale_y = 1.0
                col_6DF1F.alignment = 'Left'.upper()
                col_6DF1F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = col_6DF1F.operator('sna.col_operator_3_70d30', text='Noise Texture', icon_value=(5 if bpy.context.scene.sna_collapse_bool_3 else 4), emboss=False, depress=False)
                row_771DA = row_6C3E9.row(heading='', align=False)
                row_771DA.alert = False
                row_771DA.enabled = True
                row_771DA.active = True
                row_771DA.use_property_split = True
                row_771DA.use_property_decorate = False
                row_771DA.scale_x = 100.0
                row_771DA.scale_y = 1.0
                row_771DA.alignment = 'Right'.upper()
                row_771DA.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_771DA.operator('sna.col_operator_3_70d30', text='', icon_value=0, emboss=False, depress=False)
                op = row_6C3E9.operator('sna.col_operator_3_70d30', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Texture.png')), emboss=False, depress=False)
                if bpy.context.scene.sna_collapse_bool_3:
                    col_D63C0 = col_04727.column(heading='', align=False)
                    col_D63C0.alert = False
                    col_D63C0.enabled = True
                    col_D63C0.active = True
                    col_D63C0.use_property_split = False
                    col_D63C0.use_property_decorate = False
                    col_D63C0.scale_x = 1.0
                    col_D63C0.scale_y = 1.0
                    col_D63C0.alignment = 'Expand'.upper()
                    col_D63C0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    col_8A498 = col_D63C0.column(heading='', align=False)
                    col_8A498.alert = False
                    col_8A498.enabled = True
                    col_8A498.active = True
                    col_8A498.use_property_split = False
                    col_8A498.use_property_decorate = False
                    col_8A498.scale_x = 1.0
                    col_8A498.scale_y = 1.0
                    col_8A498.alignment = 'Expand'.upper()
                    col_8A498.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'NTEXTURE' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['NTEXTURE']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                            layout_function = col_8A498
                            sna_ntexture_7D31A(layout_function, 'NTEXTURE', '')
            if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EXPLOSION' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                box_55ED1 = col_8BC78.box()
                box_55ED1.alert = False
                box_55ED1.enabled = True
                box_55ED1.active = True
                box_55ED1.use_property_split = False
                box_55ED1.use_property_decorate = False
                box_55ED1.alignment = 'Expand'.upper()
                box_55ED1.scale_x = 1.0
                box_55ED1.scale_y = 1.0
                if not True: box_55ED1.operator_context = "EXEC_DEFAULT"
                col_F03D0 = box_55ED1.column(heading='', align=False)
                col_F03D0.alert = False
                col_F03D0.enabled = True
                col_F03D0.active = True
                col_F03D0.use_property_split = False
                col_F03D0.use_property_decorate = False
                col_F03D0.scale_x = 1.0
                col_F03D0.scale_y = 1.0
                col_F03D0.alignment = 'Expand'.upper()
                col_F03D0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_BF7C2 = col_F03D0.row(heading='', align=False)
                row_BF7C2.alert = False
                row_BF7C2.enabled = True
                row_BF7C2.active = True
                row_BF7C2.use_property_split = False
                row_BF7C2.use_property_decorate = False
                row_BF7C2.scale_x = 1.0
                row_BF7C2.scale_y = 2.0
                row_BF7C2.alignment = 'Left'.upper()
                row_BF7C2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                col_E7289 = row_BF7C2.column(heading='', align=False)
                col_E7289.alert = False
                col_E7289.enabled = True
                col_E7289.active = True
                col_E7289.use_property_split = False
                col_E7289.use_property_decorate = False
                col_E7289.scale_x = 1.0
                col_E7289.scale_y = 1.0
                col_E7289.alignment = 'Left'.upper()
                col_E7289.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = col_E7289.operator('sna.col_operator_4_9bbec', text='Fire Settings', icon_value=(5 if bpy.context.scene.sna_collapse_bool_4 else 4), emboss=False, depress=False)
                row_B547C = row_BF7C2.row(heading='', align=False)
                row_B547C.alert = False
                row_B547C.enabled = True
                row_B547C.active = True
                row_B547C.use_property_split = True
                row_B547C.use_property_decorate = False
                row_B547C.scale_x = 100.0
                row_B547C.scale_y = 1.0
                row_B547C.alignment = 'Right'.upper()
                row_B547C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_B547C.operator('sna.col_operator_4_9bbec', text='', icon_value=0, emboss=False, depress=False)
                op = row_BF7C2.operator('sna.col_operator_4_9bbec', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Fire.png')), emboss=False, depress=False)
                if bpy.context.scene.sna_collapse_bool_4:
                    col_CC6EA = col_F03D0.column(heading='', align=False)
                    col_CC6EA.alert = False
                    col_CC6EA.enabled = True
                    col_CC6EA.active = True
                    col_CC6EA.use_property_split = False
                    col_CC6EA.use_property_decorate = False
                    col_CC6EA.scale_x = 1.0
                    col_CC6EA.scale_y = 1.0
                    col_CC6EA.alignment = 'Expand'.upper()
                    col_CC6EA.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    col_9F02D = col_CC6EA.column(heading='Emission', align=False)
                    col_9F02D.alert = False
                    col_9F02D.enabled = True
                    col_9F02D.active = True
                    col_9F02D.use_property_split = False
                    col_9F02D.use_property_decorate = False
                    col_9F02D.scale_x = 1.0
                    col_9F02D.scale_y = 1.5
                    col_9F02D.alignment = 'Expand'.upper()
                    col_9F02D.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EMISSION' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['EMISSION']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                            layout_function = col_9F02D
                            sna_density_A2816(layout_function, 'EMISSION', ('Emission' if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EMISSIONCOLOR' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes) else 'Emission'), False)
                    col_CC6EA.separator(factor=1.0)
                    box_BF5F8 = col_CC6EA.box()
                    box_BF5F8.alert = False
                    box_BF5F8.enabled = True
                    box_BF5F8.active = True
                    box_BF5F8.use_property_split = False
                    box_BF5F8.use_property_decorate = False
                    box_BF5F8.alignment = 'Expand'.upper()
                    box_BF5F8.scale_x = 1.0
                    box_BF5F8.scale_y = 1.0
                    if not True: box_BF5F8.operator_context = "EXEC_DEFAULT"
                    col_24D3E = box_BF5F8.column(heading='', align=False)
                    col_24D3E.alert = False
                    col_24D3E.enabled = True
                    col_24D3E.active = True
                    col_24D3E.use_property_split = False
                    col_24D3E.use_property_decorate = False
                    col_24D3E.scale_x = 1.0
                    col_24D3E.scale_y = 1.0
                    col_24D3E.alignment = 'Expand'.upper()
                    col_24D3E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    col_24D3E.label(text='Fire Color', icon_value=0)
                    if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'EMISSIONCOLOR' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['EMISSIONCOLOR']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                            layout_function = col_24D3E
                            sna_colorramp_display_3BC97(layout_function, 'EMISSIONCOLOR')
                    col_5399C = box_BF5F8.column(heading='', align=False)
                    col_5399C.alert = False
                    col_5399C.enabled = True
                    col_5399C.active = True
                    col_5399C.use_property_split = False
                    col_5399C.use_property_decorate = False
                    col_5399C.scale_x = 1.0
                    col_5399C.scale_y = 1.5
                    col_5399C.alignment = 'Expand'.upper()
                    col_5399C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    col_5399C.separator(factor=0.0010000000474974513)
                    split_ABB97 = col_5399C.split(factor=0.5, align=False)
                    split_ABB97.alert = False
                    split_ABB97.enabled = True
                    split_ABB97.active = True
                    split_ABB97.use_property_split = False
                    split_ABB97.use_property_decorate = False
                    split_ABB97.scale_x = 1.0
                    split_ABB97.scale_y = 1.0
                    split_ABB97.alignment = 'Expand'.upper()
                    if not True: split_ABB97.operator_context = "EXEC_DEFAULT"
                    split_ABB97.label(text='Color Offset', icon_value=0)
                    row_BA7A1 = split_ABB97.row(heading='', align=False)
                    row_BA7A1.alert = False
                    row_BA7A1.enabled = True
                    row_BA7A1.active = True
                    row_BA7A1.use_property_split = False
                    row_BA7A1.use_property_decorate = False
                    row_BA7A1.scale_x = 1.0
                    row_BA7A1.scale_y = 1.0
                    row_BA7A1.alignment = 'Expand'.upper()
                    row_BA7A1.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'FLAMEINTENSITY' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['FLAMEINTENSITY']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                            layout_function = row_BA7A1
                            sna_value_4D0A9(layout_function, 'FLAMEINTENSITY', '')
                    col_CC6EA.separator(factor=1.0)
                    box_D1ABE = col_CC6EA.box()
                    box_D1ABE.alert = False
                    box_D1ABE.enabled = True
                    box_D1ABE.active = True
                    box_D1ABE.use_property_split = False
                    box_D1ABE.use_property_decorate = False
                    box_D1ABE.alignment = 'Expand'.upper()
                    box_D1ABE.scale_x = 1.0
                    box_D1ABE.scale_y = 1.0
                    if not True: box_D1ABE.operator_context = "EXEC_DEFAULT"
                    col_74658 = box_D1ABE.column(heading='', align=False)
                    col_74658.alert = False
                    col_74658.enabled = True
                    col_74658.active = True
                    col_74658.use_property_split = False
                    col_74658.use_property_decorate = False
                    col_74658.scale_x = 1.0
                    col_74658.scale_y = 1.0
                    col_74658.alignment = 'Expand'.upper()
                    col_74658.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    col_74658.label(text='Fire Distribution', icon_value=0)
                    if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'FLAMEDIST' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['FLAMEDIST']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                            layout_function = col_74658
                            sna_colorramp_display_3BC97(layout_function, 'FLAMEDIST')
            if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'MAP' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                box_FBC08 = col_8BC78.box()
                box_FBC08.alert = False
                box_FBC08.enabled = True
                box_FBC08.active = True
                box_FBC08.use_property_split = False
                box_FBC08.use_property_decorate = False
                box_FBC08.alignment = 'Expand'.upper()
                box_FBC08.scale_x = 1.0
                box_FBC08.scale_y = 1.0
                if not True: box_FBC08.operator_context = "EXEC_DEFAULT"
                col_6AAE0 = box_FBC08.column(heading='', align=False)
                col_6AAE0.alert = False
                col_6AAE0.enabled = True
                col_6AAE0.active = True
                col_6AAE0.use_property_split = False
                col_6AAE0.use_property_decorate = False
                col_6AAE0.scale_x = 1.0
                col_6AAE0.scale_y = 1.0
                col_6AAE0.alignment = 'Expand'.upper()
                col_6AAE0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                row_A5C99 = col_6AAE0.row(heading='', align=False)
                row_A5C99.alert = False
                row_A5C99.enabled = True
                row_A5C99.active = True
                row_A5C99.use_property_split = False
                row_A5C99.use_property_decorate = False
                row_A5C99.scale_x = 1.0
                row_A5C99.scale_y = 2.0
                row_A5C99.alignment = 'Left'.upper()
                row_A5C99.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                col_5ED7C = row_A5C99.column(heading='', align=False)
                col_5ED7C.alert = False
                col_5ED7C.enabled = True
                col_5ED7C.active = True
                col_5ED7C.use_property_split = False
                col_5ED7C.use_property_decorate = False
                col_5ED7C.scale_x = 1.0
                col_5ED7C.scale_y = 1.0
                col_5ED7C.alignment = 'Left'.upper()
                col_5ED7C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = col_5ED7C.operator('sna.col_operator_6_28476', text='Mapping', icon_value=(5 if bpy.context.scene.sna_collapse_bool_6 else 4), emboss=False, depress=False)
                row_36481 = row_A5C99.row(heading='', align=False)
                row_36481.alert = False
                row_36481.enabled = True
                row_36481.active = True
                row_36481.use_property_split = True
                row_36481.use_property_decorate = False
                row_36481.scale_x = 100.0
                row_36481.scale_y = 1.0
                row_36481.alignment = 'Right'.upper()
                row_36481.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                op = row_36481.operator('sna.col_operator_6_28476', text='', icon_value=0, emboss=False, depress=False)
                op = row_A5C99.operator('sna.col_operator_6_28476', text='', icon_value=load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'Mapping.png')), emboss=False, depress=False)
                if bpy.context.scene.sna_collapse_bool_6:
                    col_3B254 = col_6AAE0.column(heading='', align=False)
                    col_3B254.alert = False
                    col_3B254.enabled = True
                    col_3B254.active = True
                    col_3B254.use_property_split = False
                    col_3B254.use_property_decorate = False
                    col_3B254.scale_x = 1.0
                    col_3B254.scale_y = 1.0
                    col_3B254.alignment = 'Expand'.upper()
                    col_3B254.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    col_6CC02 = col_3B254.column(heading='', align=False)
                    col_6CC02.alert = False
                    col_6CC02.enabled = True
                    col_6CC02.active = True
                    col_6CC02.use_property_split = False
                    col_6CC02.use_property_decorate = False
                    col_6CC02.scale_x = 1.0
                    col_6CC02.scale_y = 1.0
                    col_6CC02.alignment = 'Expand'.upper()
                    col_6CC02.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                    if (property_exists("(bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes", globals(), locals()) and 'MAP' in (bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).name].material.node_tree.nodes):
                        col_84BF4 = col_6CC02.column(heading='', align=False)
                        col_84BF4.alert = False
                        col_84BF4.enabled = True
                        col_84BF4.active = True
                        col_84BF4.use_property_split = False
                        col_84BF4.use_property_decorate = False
                        col_84BF4.scale_x = 1.0
                        col_84BF4.scale_y = 1.0
                        col_84BF4.alignment = 'Expand'.upper()
                        col_84BF4.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                        row_5B3C4 = col_84BF4.row(heading='', align=False)
                        row_5B3C4.alert = False
                        row_5B3C4.enabled = True
                        row_5B3C4.active = True
                        row_5B3C4.use_property_split = False
                        row_5B3C4.use_property_decorate = False
                        row_5B3C4.scale_x = 1.0
                        row_5B3C4.scale_y = 1.0
                        row_5B3C4.alignment = 'Expand'.upper()
                        row_5B3C4.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
                        if (property_exists("bpy.context.active_object.material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes['MAP']", globals(), locals()) or bpy.context.scene.sna_pinbooleean):
                            layout_function = row_5B3C4
                            sna_mapping_B7727(layout_function, 'MAP')
        else:
            pass


def sna_value_4D0A9(layout_function, node_name, label_name):
    for i_563EB in range(len((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes)):
        if ((bpy.context.scene.sna_pinobject if bpy.context.scene.sna_pinbooleean else bpy.context.view_layer.objects.active).material_slots[(bpy.context.scene.sna_pinmaterialname if bpy.context.scene.sna_pinbooleean else bpy.context.active_object.active_material.name)].material.node_tree.nodes[i_563EB].name == node_name):
            col_2A5D0 = layout_function.column(heading='', align=False)
            col_2A5D0.alert = False
            col_2A5D0.enabled = True
            col_2A5D0.active = True
            col_2A5D0.use_property_split = False
            col_2A5D0.use_property_decorate = False
            col_2A5D0.scale_x = 1.0
            col_2A5D0.scale_y = 1.0
            col_2A5D0.alignment = 'Expand'.upper()
            col_2A5D0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_CDEB2 = col_2A5D0.column(heading='', align=False)
            col_CDEB2.alert = False
            col_CDEB2.enabled = True
            col_CDEB2.active = True
            col_CDEB2.use_property_split = False
            col_CDEB2.use_property_decorate = False
            col_CDEB2.scale_x = 1.0
            col_CDEB2.scale_y = 1.0
            col_CDEB2.alignment = 'Expand'.upper()
            col_CDEB2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_CDEB2.prop((bpy.context.scene.sna_pinmaterialid if bpy.context.scene.sna_pinbooleean else bpy.context.object.active_material).node_tree.nodes[node_name].outputs[0], 'default_value', text=label_name, icon_value=0, emboss=True)


def sna_enum_planes_enum_items(self, context):
    return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]


def sna_clouds_enum_items(self, context):
    return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]


def sna_smokes_enum_items(self, context):
    return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]


def sna_explosions_enum_items(self, context):
    return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]


def sna_ground_fogs_enum_items(self, context):
    return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]


def sna_fog_planes_and_puffs_enum_items(self, context):
    return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]


def sna_tornado_enum_items(self, context):
    return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]


def sna_magic__other_enum_items(self, context):
    return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_modeselectenum = bpy.props.EnumProperty(name='ModeSelectENUM', description='', items=[('Planes', 'Planes', 'Planes', 0, 0), ('Volumes', 'Volumes', 'Volumes', 0, 1), ('VDBs', 'VDBs', 'VDBs', 0, 2)])
    bpy.types.Scene.sna_enum_planes = bpy.props.EnumProperty(name='ENUM Planes', description='', items=sna_enum_planes_enum_items)
    bpy.types.Scene.sna_enum_volumes = bpy.props.EnumProperty(name='ENUM Volumes', description='', items=sna_enum_volumes_enum_items, update=sna_update_sna_enum_volumes_A2B57)
    bpy.types.Scene.sna_enum_vdbs = bpy.props.EnumProperty(name='ENUM VDBs', description='', items=sna_enum_vdbs_enum_items, update=sna_update_sna_enum_vdbs_68470)
    bpy.types.Scene.sna_sample_prop = bpy.props.FloatProperty(name='SAMPLE PROP', description='', default=0.0, subtype='NONE', unit='NONE', step=3, precision=6)
    bpy.types.Scene.sna_fogpropenum = bpy.props.EnumProperty(name='FogPropENUM', description='', items=[('DensityTog', 'DensityTog', 'DensityTog', 0, 0), ('NoiseTog', 'NoiseTog', 'NoiseTog', 0, 1), ('MappingTog', 'MappingTog', 'MappingTog', 0, 2)])
    bpy.types.Scene.sna_pinbooleean = bpy.props.BoolProperty(name='PinBooleean', description='', default=False)
    bpy.types.Scene.sna_pinmaterialname = bpy.props.StringProperty(name='PinMaterialNAME', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pinmaterialid = bpy.props.PointerProperty(name='PinMaterialID', description='', type=bpy.types.Material)
    bpy.types.Scene.sna_pinobject = bpy.props.PointerProperty(name='PinObject', description='', type=bpy.types.Object)
    bpy.types.Scene.sna_hide_absorb_bool = bpy.props.BoolProperty(name='HIDE ABSORB BOOL', description='', default=True)
    bpy.types.Scene.sna_switch_density_to_value = bpy.props.BoolProperty(name='SWITCH DENSITY TO VALUE', description='', default=False)
    bpy.types.Scene.sna_clouds = bpy.props.EnumProperty(name='CLOUDS', description='', items=sna_clouds_enum_items)
    bpy.types.Scene.sna_smokes = bpy.props.EnumProperty(name='SMOKES', description='', items=sna_smokes_enum_items)
    bpy.types.Scene.sna_explosions = bpy.props.EnumProperty(name='EXPLOSIONS', description='', items=sna_explosions_enum_items)
    bpy.types.Scene.sna_show_vdb_category = bpy.props.EnumProperty(name='Show VDB Category', description='', items=[('All', 'All', 'All', 0, 0), ('Explosions', 'Explosions', 'Explosions', 0, 1), ('Smokes', 'Smokes', 'Smokes', 0, 2), ('Clouds', 'Clouds', 'Clouds', 0, 3)])
    bpy.types.Scene.sna_show_volume_category = bpy.props.EnumProperty(name='Show Volume Category', description='', items=[('All', 'All', 'All', 0, 0), ('Ground Fogs', 'Ground Fogs', '', 0, 1), ('Fog Planes & Puffs', 'Fog Planes & Puffs', '', 0, 2), ('Tornado', 'Tornado', '', 0, 3), ('Magic & Other', 'Magic & Other', 'Magic & Other', 0, 4)])
    bpy.types.Scene.sna_ground_fogs = bpy.props.EnumProperty(name='GROUND FOGS', description='', items=sna_ground_fogs_enum_items)
    bpy.types.Scene.sna_fog_planes_and_puffs = bpy.props.EnumProperty(name='FOG PLANES AND PUFFS', description='', items=sna_fog_planes_and_puffs_enum_items)
    bpy.types.Scene.sna_tornado = bpy.props.EnumProperty(name='TORNADO', description='', items=sna_tornado_enum_items)
    bpy.types.Scene.sna_magic__other = bpy.props.EnumProperty(name='Magic & Other', description='', items=sna_magic__other_enum_items)
    bpy.types.Scene.sna_collapse_bool_1 = bpy.props.BoolProperty(name='COLLAPSE BOOL 1', description='', default=False)
    bpy.types.Scene.sna_collapse_bool_2 = bpy.props.BoolProperty(name='COLLAPSE BOOL 2', description='', default=False)
    bpy.types.Scene.sna_collapse_bool_3 = bpy.props.BoolProperty(name='COLLAPSE BOOL 3', description='', default=False)
    bpy.types.Scene.sna_collapse_bool_4 = bpy.props.BoolProperty(name='COLLAPSE BOOL 4', description='', default=False)
    bpy.types.Scene.sna_collapse_bool5 = bpy.props.BoolProperty(name='COLLAPSE BOOL5', description='', default=False)
    bpy.types.Scene.sna_collapse_bool_6 = bpy.props.BoolProperty(name='COLLAPSE BOOL 6', description='', default=False)
    bpy.types.Scene.sna_collapser_bool_7 = bpy.props.BoolProperty(name='COLLAPSER BOOL 7', description='', default=False)
    bpy.utils.register_class(SNA_OT_Col_Operator_Adcef)
    bpy.utils.register_class(SNA_OT_Col_Operator_2_F7F90)
    bpy.utils.register_class(SNA_OT_Col_Operator_3_70D30)
    bpy.utils.register_class(SNA_OT_Col_Operator_4_9Bbec)
    bpy.utils.register_class(SNA_OT_Col_Operator_5_D8Da2)
    bpy.utils.register_class(SNA_OT_Col_Operator_6_28476)
    bpy.utils.register_class(SNA_OT_Col_Operator_7_111E2)
    bpy.utils.register_class(SNA_OT_Enumselectorplanes_A688C)
    bpy.utils.register_class(SNA_OT_Enumselectorvolumes_D5052)
    bpy.utils.register_class(SNA_OT_Enumselectorvdbs_E7824)
    bpy.utils.register_class(SNA_OT_Fogpropenumselectordensity_B75B0)
    bpy.utils.register_class(SNA_OT_Fogpropenumselectornoise_Fb05E)
    bpy.utils.register_class(SNA_OT_Fogpropenumselectormapping_9A4E8)
    bpy.utils.register_class(SNA_OT_Fog_It_Up_Vdb_20Dfb)
    bpy.utils.register_class(SNA_OT_Fog_It_Up_Volume_D3482)
    bpy.utils.register_class(SNA_PT_ALT_TAB_EASY_FOG_2_DEMO_E4563)
    bpy.app.handlers.load_post.append(load_post_handler_22468)
    bpy.utils.register_class(SNA_OT_Pin_Settings_7A41C)
    bpy.utils.register_class(SNA_AddonPreferences_8B506)
    bpy.utils.register_class(SNA_PT_alt_tab_easy_fog_2_7C50C)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_collapser_bool_7
    del bpy.types.Scene.sna_collapse_bool_6
    del bpy.types.Scene.sna_collapse_bool5
    del bpy.types.Scene.sna_collapse_bool_4
    del bpy.types.Scene.sna_collapse_bool_3
    del bpy.types.Scene.sna_collapse_bool_2
    del bpy.types.Scene.sna_collapse_bool_1
    del bpy.types.Scene.sna_magic__other
    del bpy.types.Scene.sna_tornado
    del bpy.types.Scene.sna_fog_planes_and_puffs
    del bpy.types.Scene.sna_ground_fogs
    del bpy.types.Scene.sna_show_volume_category
    del bpy.types.Scene.sna_show_vdb_category
    del bpy.types.Scene.sna_explosions
    del bpy.types.Scene.sna_smokes
    del bpy.types.Scene.sna_clouds
    del bpy.types.Scene.sna_switch_density_to_value
    del bpy.types.Scene.sna_hide_absorb_bool
    del bpy.types.Scene.sna_pinobject
    del bpy.types.Scene.sna_pinmaterialid
    del bpy.types.Scene.sna_pinmaterialname
    del bpy.types.Scene.sna_pinbooleean
    del bpy.types.Scene.sna_fogpropenum
    del bpy.types.Scene.sna_sample_prop
    del bpy.types.Scene.sna_enum_vdbs
    del bpy.types.Scene.sna_enum_volumes
    del bpy.types.Scene.sna_enum_planes
    del bpy.types.Scene.sna_modeselectenum
    bpy.utils.unregister_class(SNA_OT_Col_Operator_Adcef)
    bpy.utils.unregister_class(SNA_OT_Col_Operator_2_F7F90)
    bpy.utils.unregister_class(SNA_OT_Col_Operator_3_70D30)
    bpy.utils.unregister_class(SNA_OT_Col_Operator_4_9Bbec)
    bpy.utils.unregister_class(SNA_OT_Col_Operator_5_D8Da2)
    bpy.utils.unregister_class(SNA_OT_Col_Operator_6_28476)
    bpy.utils.unregister_class(SNA_OT_Col_Operator_7_111E2)
    bpy.utils.unregister_class(SNA_OT_Enumselectorplanes_A688C)
    bpy.utils.unregister_class(SNA_OT_Enumselectorvolumes_D5052)
    bpy.utils.unregister_class(SNA_OT_Enumselectorvdbs_E7824)
    bpy.utils.unregister_class(SNA_OT_Fogpropenumselectordensity_B75B0)
    bpy.utils.unregister_class(SNA_OT_Fogpropenumselectornoise_Fb05E)
    bpy.utils.unregister_class(SNA_OT_Fogpropenumselectormapping_9A4E8)
    bpy.utils.unregister_class(SNA_OT_Fog_It_Up_Vdb_20Dfb)
    bpy.utils.unregister_class(SNA_OT_Fog_It_Up_Volume_D3482)
    bpy.utils.unregister_class(SNA_PT_ALT_TAB_EASY_FOG_2_DEMO_E4563)
    bpy.app.handlers.load_post.remove(load_post_handler_22468)
    bpy.utils.unregister_class(SNA_OT_Pin_Settings_7A41C)
    bpy.utils.unregister_class(SNA_AddonPreferences_8B506)
    bpy.utils.unregister_class(SNA_PT_alt_tab_easy_fog_2_7C50C)
