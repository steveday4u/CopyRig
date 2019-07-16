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

class SourceSkel:

    def __init__(self, name):
        self._name = name
    
    def info(self):
        return self._name

    def check(self, bones):
        return False

    def convert(self, bones):
        return {}

class MHGameEngine(SourceSkel):

    _translate = {
        # 'Root':'root_ref.x', 'pelvis': '', 'spine_01':'', 'spine_02':'', 'spine_03':'',
        'clavicle_l': 'shoulder_ref.l',
        'upperarm_l': 'arm_ref.l',
        'lowerarm_l': 'forearm_ref.l',
        'hand_l': 'hand_ref.l',
        'index_01_l': 'index1_ref.l',
        'index_02_l': 'index2_ref.l',
        'index_03_l': 'index3_ref.l',
        'middle_01_l': 'middle1_ref.l',
        'middle_02_l': 'middle2_ref.l',
        'middle_03_l': 'middle3_ref.l',
        'pinky_01_l': 'pinky1_ref.l',
        'pinky_02_l': 'pinky2_ref.l',
        'pinky_03_l': 'pinky3_ref.l',
        'ring_01_l': 'ring1_ref.l',
        'ring_02_l': 'ring2_ref.l',
        'ring_03_l': 'ring3_ref.l',
        'thumb_01_l': 'thumb1_ref.l',
        'thumb_02_l': 'thumb2_ref.l',
        'thumb_03_l': 'thumb3_ref.l',
        'clavicle_r': 'shoulder_ref.r',
        'upperarm_r': 'arm_ref.r',
        'lowerarm_r': 'forearm_ref.r',
        'hand_r': 'hand_ref.r',
        'index_01_r': 'index1_ref.r',
        'index_02_r': 'index2_ref.r',
        'index_03_r': 'index3_ref.r',
        'middle_01_r': 'middle1_ref.r',
        'middle_02_r': 'middle2_ref.r',
        'middle_03_r': 'middle3_ref.r',
        'pinky_01_r': 'pinky1_ref.r',
        'pinky_02_r': 'pinky2_ref.r',
        'pinky_03_r': 'pinky3_ref.r',
        'ring_01_r': 'ring1_ref.r',
        'ring_02_r': 'ring2_ref.r',
        'ring_03_r': 'ring3_ref.r',
        'thumb_01_r': 'thumb1_ref.r',
        'thumb_02_r': 'thumb2_ref.r',
        'thumb_03_r': 'thumb3_ref.r',
        'neck_01': 'neck_ref.x',
        'head': 'head_ref.x',
        'thigh_l': 'thigh_ref.l',
        'calf_l': 'leg_ref.l',
        'foot_l': 'foot_ref.l',
        'ball_l': 'toes_ref.l',
        'thigh_r': 'thigh_ref.r',
        'calf_r': 'leg_ref.r',
        'foot_r': 'foot_ref.r',
        'ball_r': 'toes_ref.r'
    }

    def __init__(self):
        super().__init__("Make Human Game Rig")
    
    def check(self, bones):
        num = len(self._translate)
        for bone in bones:
            if bone.name in self._translate:
                num -= 1
        return num == 0

    def convert(self, bones):
        dict = {}
        for bone in bones:
            if bone.name in self._translate:
                dict[self._translate[bone.name]] = [bone.head[0], bone.head[1], bone.head[2]], [
                    bone.tail[0], bone.tail[1], bone.tail[2]], bone.roll

        return dict
