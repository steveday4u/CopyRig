# Copyright 2019 Steve Day

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import time
import os
import ast
import bpy_extras
import math
import mathutils
import bmesh
import bpy
from . import sourceskels

bl_info = {
    "name": "CopyRig",
    "author": "Steve Day",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic"
}

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
        info = CopyRig.copy()
        if info:
            self.report({'INFO'}, 'Ok. ' + info + ' detected.')
        else:
            self.report({'ERROR'}, 'Unknown rig.')
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

    _skels = [sourceskels.MHGameEngine(), sourceskels.MHDefault()]
    _dict = {}

    @classmethod
    def has_data(cls):
        return bool(cls._dict)

    @classmethod
    def copy(cls):
        bones = bpy.context.active_object.data.edit_bones
        for skel in cls._skels:
            if skel.check(bones):
                cls._dict = skel.convert(bones)
                return skel.info
        # nothing found, print template
        print('------ unknown rig ------')
        for bone in bones:
            print ('\'' + bone.name + '\': ')
        return None

    @classmethod
    def paste(cls):
        print('------ paste to ------')
        for bone in bpy.context.active_object.data.edit_bones:
            print ('\'' + bone.name + '\': ')
            if bone.layers[17] and bone.name in cls._dict:
                bone.head, bone.tail, bone.roll = cls._dict[bone.name]


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
