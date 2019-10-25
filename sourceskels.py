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

import mathutils


class SourceSkel:

    info = ''

    def check(self, bones):
        return False

    def convert(self, bones):
        return {}


class MHGameEngine(SourceSkel):

    info = 'Makehuman Game Rig'

    _translate = {
        # 'Root':'root_ref.x', 'pelvis', 'spine_01':'', 'spine_02':'', 'spine_03':'',
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
        # rotation bug in mh
        dict['thigh_ref.l'] = dict['thigh_ref.l'][0], dict['thigh_ref.l'][1], dict['leg_ref.l'][2]
        dict['thigh_ref.r'] = dict['thigh_ref.r'][0], dict['thigh_ref.r'][1], dict['leg_ref.r'][2]
        return dict


class MHDefault(SourceSkel):
    info = 'Makehuman Default Rig'
    _boneset = {
        'breast.L',
        'breast.R',
        'clavicle.L',
        'clavicle.R',
        'eye.L',
        'eye.R',
        'finger1-1.L',
        'finger1-1.R',
        'finger1-2.L',
        'finger1-2.R',
        'finger1-3.L',
        'finger1-3.R',
        'finger2-1.L',
        'finger2-1.R',
        'finger2-2.L',
        'finger2-2.R',
        'finger2-3.L',
        'finger2-3.R',
        'finger3-1.L',
        'finger3-1.R',
        'finger3-2.L',
        'finger3-2.R',
        'finger3-3.L',
        'finger3-3.R',
        'finger4-1.L',
        'finger4-1.R',
        'finger4-2.L',
        'finger4-2.R',
        'finger4-3.L',
        'finger4-3.R',
        'finger5-1.L',
        'finger5-1.R',
        'finger5-2.L',
        'finger5-2.R',
        'finger5-3.L',
        'finger5-3.R',
        'foot.L',
        'foot.R',
        'head',
        'jaw',
        'levator02.L',
        'levator02.R',
        'levator03.L',
        'levator03.R',
        'levator04.L',
        'levator04.R',
        'levator05.L',
        'levator05.R',
        'levator06.L',
        'levator06.R',
        'lowerarm01.L',
        'lowerarm01.R',
        'lowerarm02.L',
        'lowerarm02.R',
        'lowerleg01.L',
        'lowerleg01.R',
        'lowerleg02.L',
        'lowerleg02.R',
        'metacarpal1.L',
        'metacarpal1.R',
        'metacarpal2.L',
        'metacarpal2.R',
        'metacarpal3.L',
        'metacarpal3.R',
        'metacarpal4.L',
        'metacarpal4.R',
        'neck01',
        'neck02',
        'neck03',
        'oculi01.L',
        'oculi01.R',
        'oculi02.L',
        'oculi02.R',
        'orbicularis03.L',
        'orbicularis03.R',
        'orbicularis04.L',
        'orbicularis04.R',
        'oris01',
        'oris02',
        'oris03.L',
        'oris03.R',
        'oris04.L',
        'oris04.R',
        'oris05',
        'oris06',
        'oris06.L',
        'oris06.R',
        'oris07.L',
        'oris07.R',
        'pelvis.L',
        'pelvis.R',
        'risorius02.L',
        'risorius02.R',
        'risorius03.L',
        'risorius03.R',
        'root',
        'shoulder01.L',
        'shoulder01.R',
        'special01',
        'special03',
        'special04',
        'special05.L',
        'special05.R',
        'special06.L',
        'special06.R',
        'spine01',
        'spine02',
        'spine03',
        'spine04',
        'spine05',
        'temporalis01.L',
        'temporalis01.R',
        'temporalis02.L',
        'temporalis02.R',
        'toe1-1.L',
        'toe1-1.R',
        'toe1-2.L',
        'toe1-2.R',
        'toe2-1.L',
        'toe2-1.R',
        'toe2-2.L',
        'toe2-2.R',
        'toe2-3.L',
        'toe2-3.R',
        'toe3-1.L',
        'toe3-1.R',
        'toe3-2.L',
        'toe3-2.R',
        'toe3-3.L',
        'toe3-3.R',
        'toe4-1.L',
        'toe4-1.R',
        'toe4-2.L',
        'toe4-2.R',
        'toe4-3.L',
        'toe4-3.R',
        'toe5-1.L',
        'toe5-1.R',
        'toe5-2.L',
        'toe5-2.R',
        'toe5-3.L',
        'toe5-3.R',
        'tongue00',
        'tongue01',
        'tongue02',
        'tongue03',
        'tongue04',
        'tongue05.L',
        'tongue05.R',
        'tongue06.L',
        'tongue06.R',
        'tongue07.L',
        'tongue07.R',
        'upperarm01.L',
        'upperarm01.R',
        'upperarm02.L',
        'upperarm02.R',
        'upperleg01.L',
        'upperleg01.R',
        'upperleg02.L',
        'upperleg02.R',
        'wrist.L',
        'wrist.R'
    }

    def check(self, bones):
        num = len(self._boneset)
        for bone in bones:
            if bone.name in self._boneset:
                num -= 1
        return num == 0

    def convert(self, bones):
        b = {}
        for bone in bones:
            b[bone.name] = [bone.head[0], bone.head[1], bone.head[2]], [
                bone.tail[0], bone.tail[1], bone.tail[2]], bone.roll
        # get a decent distance in scale
        dist = distance(b['oris05'][0], b['oris05'][1])

        # calculate foot tail
        ft_l = [b['toe2-1.L'][0][0] + (b['toe3-1.L'][0][0] - b['toe2-1.L'][0][0]) / 2, b['toe5-1.L'][0][1], b['toe2-3.L'][1][2]]
        ft_r = [b['toe2-1.R'][0][0] + (b['toe3-1.R'][0][0] - b['toe2-1.R'][0][0]) / 2, b['toe5-1.R'][0][1], b['toe2-3.R'][1][2]]
        # bottom bone calculation: just but it somewhere between the hip and the center
        bt_l = [b['pelvis.L'][1][0] - b['pelvis.L'][1][0] / 4, b['root'][0][1] + dist * 2, b['pelvis.L'][1][2]]
        bt_r = [b['pelvis.R'][1][0] - b['pelvis.R'][1][0] / 4, b['root'][0][1] + dist * 2, b['pelvis.R'][1][2]]

        dict = {
            'arm_ref.l': (b['upperarm01.L'][0], b['upperarm02.L'][1], b['upperarm02.L'][2]),
            'arm_ref.r':  (b['upperarm01.R'][0], b['upperarm02.R'][1], b['upperarm02.R'][2]),
            'bot_bend_ref.l': (bt_l, [bt_l[0], bt_l[1] + dist * 3, bt_l[2]], 0),
            'bot_bend_ref.r': (bt_r, [bt_r[0], bt_r[1] + dist * 3, bt_r[2]], 0),
            # 'cheek_inflate_ref.l':
            # 'cheek_inflate_ref.r':
            # 'cheek_smile_ref.l':
            # 'cheek_smile_ref.r':
            'chin_01_ref.x':  ([0, b['oris06.L'][1][1], b['oris06.L'][1][2]], [0, b['oris06.L'][1][1] - dist, b['oris06.L'][1][2]], None),
            'chin_02_ref.x': (b['special04'][0], [b['special04'][0][0], b['special04'][0][1], b['special04'][0][2] - dist], None),
            # 'ear_01_ref.l':
            # 'ear_01_ref.r':
            # 'ear_02_ref.l':
            # 'ear_02_ref.r':
            # 'eyebrow_01_end_ref.l':
            # 'eyebrow_01_end_ref.r':
            # 'eyebrow_01_ref.l':
            # 'eyebrow_01_ref.r':
            # 'eyebrow_02_ref.l':
            # 'eyebrow_02_ref.r':
            # 'eyebrow_03_ref.l':
            # 'eyebrow_03_ref.r':
            # 'eyebrow_full_ref.l':
            # 'eyebrow_full_ref.r':
            # fix eye center
            'eyelid_bot_01_ref.l': (b['eye.L'][0], None, None),
            'eyelid_bot_01_ref.r': (b['eye.R'][0], None, None),
            'eyelid_bot_02_ref.l': (b['eye.L'][0], None, None),
            'eyelid_bot_02_ref.r': (b['eye.R'][0], None, None),
            'eyelid_bot_03_ref.l': (b['eye.L'][0], None, None),
            'eyelid_bot_03_ref.r': (b['eye.R'][0], None, None),
            'eyelid_bot_ref.l': (b['eye.L'][0], None, None),
            'eyelid_bot_ref.r': (b['eye.R'][0], None, None),
            'eyelid_corner_01_ref.l': (b['eye.L'][0], None, None),
            'eyelid_corner_01_ref.r': (b['eye.R'][0], None, None),
            'eyelid_corner_02_ref.l': (b['eye.L'][0], None, None),
            'eyelid_corner_02_ref.r': (b['eye.R'][0], None, None),
            'eyelid_top_01_ref.l': (b['eye.L'][0], None, None),
            'eyelid_top_01_ref.r': (b['eye.R'][0], None, None),
            'eyelid_top_02_ref.l': (b['eye.L'][0], None, None),
            'eyelid_top_02_ref.r': (b['eye.R'][0], None, None),
            'eyelid_top_03_ref.l': (b['eye.L'][0], None, None),
            'eyelid_top_03_ref.r': (b['eye.R'][0], None, None),
            'eyelid_top_ref.l': (b['eye.L'][0], None, None),
            'eyelid_top_ref.r': (b['eye.R'][0], None, None),
            'eye_offset_ref.l': (b['eye.L'][0], None, None),
            'eye_offset_ref.r': (b['eye.R'][0], None, None),
            # 'foot_bank_01_ref.l':
            # 'foot_bank_01_ref.r':
            # 'foot_bank_02_ref.l':
            # 'foot_bank_02_ref.r':
            # 'foot_heel_ref.l':
            # 'foot_heel_ref.r':
            'foot_ref.l': (b['foot.L'][0], ft_l, b['foot.L'][2]),
            'foot_ref.r': (b['foot.R'][0], ft_r, b['foot.R'][2]),
            'forearm_ref.l': (b['lowerarm01.L'][0], b['lowerarm02.L'][1], b['lowerarm02.L'][2]),
            'forearm_ref.r':  (b['lowerarm01.R'][0], b['lowerarm02.R'][1], b['lowerarm02.R'][2]),
            'hand_ref.l': b['wrist.L'],
            'hand_ref.r': b['wrist.R'],
            'head_ref.x': b['head'],
            'index1_base_ref.l': b['metacarpal1.L'],
            'index1_base_ref.r': b['metacarpal1.R'],
            'index1_ref.l': b['finger2-1.L'],
            'index1_ref.r': b['finger2-1.R'],
            'index2_ref.l': b['finger2-2.L'],
            'index2_ref.r': b['finger2-2.R'],
            'index3_ref.l': b['finger2-3.L'],
            'index3_ref.r': b['finger2-3.R'],
            'jaw_ref.x': (b['jaw'][0], b['special04'][1], b['jaw'][2]),
            'leg_ref.l': (b['lowerleg01.L'][0], b['lowerleg02.L'][1], b['lowerleg02.L'][2]),
            'leg_ref.r': (b['lowerleg01.R'][0], b['lowerleg02.R'][1], b['lowerleg02.R'][2]),
            # 'lips_bot_01_ref.l':
            # 'lips_bot_01_ref.r':
            # 'lips_bot_ref.l':
            # 'lips_bot_ref.r':
            # 'lips_bot_ref.x':
            # 'lips_corner_mini_ref.l':
            # 'lips_corner_mini_ref.r':
            'lips_roll_bot_ref.x': ([b['oris01'][0][0], b['oris01'][0][1] - dist, b['oris01'][0][2]],
                                    [b['oris01'][0][0], b['oris01'][0][1] - dist - dist / 2, b['oris01'][0][2]], None),
            'lips_roll_top_ref.x': ([b['oris06'][1][0], b['oris06'][1][1] - dist, b['oris06'][1][2]],
                                    [b['oris06'][1][0], b['oris06'][1][1] - dist - dist / 2, b['oris06'][1][2]], None),
            # 'lips_smile_ref.l':
            # 'lips_smile_ref.r':
            # 'lips_top_01_ref.l':
            # 'lips_top_01_ref.r':
            # 'lips_top_ref.l':
            # 'lips_top_ref.r':
            # 'lips_top_ref.x':
            'middle1_base_ref.l': b['metacarpal2.L'],
            'middle1_base_ref.r': b['metacarpal2.R'],
            'middle1_ref.l': b['finger3-1.L'],
            'middle1_ref.r': b['finger3-1.R'],
            'middle2_ref.l': b['finger3-2.L'],
            'middle2_ref.r': b['finger3-2.R'],
            'middle3_ref.l': b['finger3-3.L'],
            'middle3_ref.r': b['finger3-3.R'],
            'neck_ref.x': (b['neck01'][0], b['neck03'][1], b['neck02'][2]),
            'nose_01_ref.x': ([0, b['levator06.L'][1][1] - dist / 2, b['levator06.L'][1][2]], [0, b['levator06.L'][1][1] - dist * 1.5, b['levator06.L'][1][2]], 0),
            'nose_02_ref.x': ([0, b['levator06.L'][0][1], b['levator06.L'][0][2]], [0, b['levator06.L'][0][1] - dist, b['levator06.L'][0][2]], 0),
            # 'nose_03_ref.x':
            'pinky1_base_ref.l': b['metacarpal4.L'],
            'pinky1_base_ref.r': b['metacarpal4.R'],
            'pinky1_ref.l': b['finger5-1.L'],
            'pinky1_ref.r': b['finger5-1.R'],
            'pinky2_ref.l': b['finger5-2.L'],
            'pinky2_ref.r': b['finger5-2.R'],
            'pinky3_ref.l': b['finger5-3.L'],
            'pinky3_ref.r': b['finger5-3.R'],
            'ring1_base_ref.l': b['metacarpal3.L'],
            'ring1_base_ref.r': b['metacarpal3.R'],
            'ring1_ref.l': b['finger4-1.L'],
            'ring1_ref.r': b['finger4-1.R'],
            'ring2_ref.l': b['finger4-2.L'],
            'ring2_ref.r': b['finger4-2.R'],
            'ring3_ref.l': b['finger4-3.L'],
            'ring3_ref.r': b['finger4-3.R'],
            'root_ref.x': (b['spine05'][0], b['spine04'][1], b['spine04'][2]),
            # shoulder rotation seems a bit strage in MH rig
            'shoulder_ref.l': (b['clavicle.L'][0], b['shoulder01.L'][1], None),
            'shoulder_ref.r': (b['clavicle.R'][0], b['shoulder01.R'][1], None),
            'spine_01_ref.x': b['spine03'],
            'spine_02_ref.x': (b['spine02'][0], b['spine01'][1], b['spine01'][2]),
            # 'teeth_bot_ref.l':
            # 'teeth_bot_ref.r':
            # 'teeth_bot_ref.x':
            # 'teeth_top_ref.l':
            # 'teeth_top_ref.r':
            # 'teeth_top_ref.x':
            'thigh_ref.l': (b['upperleg01.L'][0], b['upperleg02.L'][1], b['upperleg02.L'][2]),
            'thigh_ref.r': (b['upperleg01.R'][0], b['upperleg02.R'][1], b['upperleg02.R'][2]),
            'thumb1_ref.l': b['finger1-1.L'],
            'thumb1_ref.r': b['finger1-1.R'],
            'thumb2_ref.l': b['finger1-2.L'],
            'thumb2_ref.r': b['finger1-2.R'],
            'thumb3_ref.l': b['finger1-3.L'],
            'thumb3_ref.r': b['finger1-3.R'],
            'toes_thumb1_ref.l': b['toe1-1.L'],
            'toes_thumb1_ref.r': b['toe1-1.R'],
            'toes_thumb2_ref.l': b['toe1-2.L'],
            'toes_thumb2_ref.r': b['toe1-2.R'],
            'toes_index1_ref.l': b['toe2-1.L'],
            'toes_index1_ref.r': b['toe2-1.R'],
            'toes_index2_ref.l': b['toe2-2.L'],
            'toes_index2_ref.r': b['toe2-2.R'],
            'toes_index3_ref.l': b['toe2-3.L'],
            'toes_index3_ref.r': b['toe2-3.R'],
            'toes_middle1_ref.l': b['toe3-1.L'],
            'toes_middle1_ref.r': b['toe3-1.R'],
            'toes_middle2_ref.l': b['toe3-2.L'],
            'toes_middle2_ref.r': b['toe3-2.R'],
            'toes_middle3_ref.l': b['toe3-3.L'],
            'toes_middle3_ref.r': b['toe3-3.R'],
            'toes_ring1_ref.l': b['toe4-1.L'],
            'toes_ring1_ref.r': b['toe4-1.R'],
            'toes_ring2_ref.l': b['toe4-2.L'],
            'toes_ring2_ref.r': b['toe4-2.R'],
            'toes_ring3_ref.l': b['toe4-3.L'],
            'toes_ring3_ref.r': b['toe4-3.R'],
            'toes_pinky1_ref.l': b['toe5-1.L'],
            'toes_pinky1_ref.r': b['toe5-1.R'],
            'toes_pinky2_ref.l': b['toe5-2.L'],
            'toes_pinky2_ref.r': b['toe5-2.R'],
            'toes_pinky3_ref.l': b['toe5-3.L'],
            'toes_pinky3_ref.r': b['toe5-3.R'],
            # 'toes_end_ref.l':
            # 'toes_end_ref.r':
            'toes_ref.l': (ft_l, [ft_l[0], b['toe1-2.L'][1][1], ft_l[2]], b['toe3-1.L'][2]),
            'toes_ref.r': (ft_r, [ft_r[0], b['toe1-2.R'][1][1], ft_r[2]], b['toe3-1.R'][2]),
            'tong_01_ref.x': b['tongue01'],
            'tong_02_ref.x': b['tongue02'],
            'tong_03_ref.x': (b['tongue03'][0], b['tongue04'][1], b['tongue03'][2]),
        }
        return dict


def shorten(origin, end, factor):
    o = mathutils.Vector(origin)
    e = mathutils.Vector(end)
    return (e - o) / factor + o


def distance(p1, p2):
    return (mathutils.Vector(p1) - mathutils.Vector(p2)).length
