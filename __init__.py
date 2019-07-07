#Copyright 2019 Steve Day

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.

bl_info = {
    "name" : "CopyRig",
    "author" : "Steve Day",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy, bmesh, mathutils, math, bpy_extras, ast, os, time

class CPYRIG_PT_Panel(bpy.types.Panel):
    bl_idname = "CPYRIG_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Copy Rig"
    # bl_context = "objectmode"
    bl_category = "Copy Rig"

    def draw(self, context):
        col = self.layout.column()
        col.label(text="Copy Rig")
        col.operator('object.cpyrig_copy')
        col.operator('object.cpyrig_paste')


class CPYRIG_OT_copy(bpy.types.Operator):
    bl_idname = "object.cpyrig_copy"
    bl_label = "Copy"
    bl_description = "Copy Rig Data"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object.type == 'ARMATURE' and context.active_object.mode == 'EDIT'

    def execute(self, context):
        CopyRig.copy()
        return {'FINISHED'}
    
class CPYRIG_OT_paste(bpy.types.Operator):
    bl_idname = "object.cpyrig_paste"
    bl_label = "Paste"
    bl_description = "Paste Rig Data"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return CopyRig.has_data() and context.active_object.type == 'ARMATURE' and context.active_object.mode == 'EDIT'
    
    def execute(self, context):
        CopyRig.paste()
        return {'FINISHED'}

bpy.utils.register_class(CPYRIG_OT_copy)
bpy.utils.register_class(CPYRIG_OT_paste)
bpy.utils.register_class(CPYRIG_PT_Panel)

class CopyRig:
    # makehuman game rig
    translate = {
    #'Root':'root_ref.x', 'pelvis': '', 'spine_01':'', 'spine_02':'', 'spine_03':'',
    'clavicle_l':'shoulder_ref.l', 
    'upperarm_l':'arm_ref.l', 
    'lowerarm_l':'forearm_ref.l', 
    'hand_l':'hand_ref.l', 
    'index_01_l': 'index1_ref.l', 
    'index_02_l': 'index2_ref.l', 
    'index_03_l': 'index3_ref.l', 
    'middle_01_l':'middle1_ref.l', 
    'middle_02_l':'middle2_ref.l', 
    'middle_03_l':'middle3_ref.l', 
    'pinky_01_l':'pinky1_ref.l', 
    'pinky_02_l':'pinky2_ref.l', 
    'pinky_03_l':'pinky3_ref.l', 
    'ring_01_l':'ring1_ref.l', 
    'ring_02_l':'ring2_ref.l', 
    'ring_03_l':'ring3_ref.l', 
    'thumb_01_l':'thumb1_ref.l', 
    'thumb_02_l':'thumb2_ref.l', 
    'thumb_03_l':'thumb3_ref.l', 
    'clavicle_r':'shoulder_ref.r',
    'upperarm_r':'arm_ref.r', 
    'lowerarm_r':'forearm_ref.r', 
    'hand_r':'hand_ref.r', 
    'index_01_r':'index1_ref.r', 
    'index_02_r':'index2_ref.r',
    'index_03_r':'index3_ref.r', 
    'middle_01_r':'middle1_ref.r', 
    'middle_02_r':'middle2_ref.r',
    'middle_03_r':'middle3_ref.r',
    'pinky_01_r':'pinky1_ref.r', 
    'pinky_02_r':'pinky2_ref.r', 
    'pinky_03_r':'pinky3_ref.r', 
    'ring_01_r':'ring1_ref.r', 
    'ring_02_r':'ring2_ref.r', 
    'ring_03_r':'ring3_ref.r', 
    'thumb_01_r':'thumb1_ref.r', 
    'thumb_02_r':'thumb2_ref.r', 
    'thumb_03_r':'thumb3_ref.r', 
    'neck_01':'neck_ref.x', 
    'head':'head_ref.x', 
    'thigh_l':'thigh_ref.l', 
    'calf_l':'leg_ref.l', 
    'foot_l':'foot_ref.l', 
    'ball_l':'toes_ref.l', 
    'thigh_r':'thigh_ref.r', 
    'calf_r':'leg_ref.r', 
    'foot_r':'foot_ref.r', 
    'ball_r':'toes_ref.r'
    }
    
    __dict = {}
   
    @classmethod
    def has_data(cls):
        return bool(cls.__dict)

    @classmethod
    def copy(cls):
        for bone in bpy.context.active_object.data.edit_bones:
            if bone.name in cls.translate:
                cls.__dict[cls.translate[bone.name]] = [bone.head[0], bone.head[1], bone.head[2]], [bone.tail[0], bone.tail[1], bone.tail[2]], bone.roll 

    @classmethod
    def paste(cls):
        for bone in bpy.context.active_object.data.edit_bones:
            if bone.layers[17] and bone.name in cls.__dict:
                bone.head, bone.tail, bone.roll = cls.__dict[bone.name]


classes = (
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)