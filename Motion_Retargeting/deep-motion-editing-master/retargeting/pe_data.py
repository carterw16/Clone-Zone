import sys
sys.path.append("../utils")
import BVH_mod as BVH
anim, names, frametime = BVH.load("datasets/Mixamo/PE/dance.bvh")
#anim, names, frametime = BVH.load("datasets/Mixamo/Aj/Dual Weapon Combo.bvh")
#anim, names, frametime = BVH.load("datasets/Mixamo/Kaya/Dancing Running Man.bvh")
#anim, names, frametime = BVH.load("datasets/Mixamo/Mousey_m/Dual Weapon Combo.bvh")
import numpy as np
kaya = np.load("datasets/Mixamo/mean_var/Kaya_mean.npy",allow_pickle=True)
print(kaya.shape)
print(names)
print(anim.shape)
test_entity = anim[100][2]
# print(test_entity.rotations)
#print(test_entity.positions)
#print(test_entity.orients)
# print(test_entity.offsets)
# print(test_entity.parents)
#print(1/frametime)  60hz
print(len(names))
#corps_name_1 = ['Pelvis', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'Hips', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Head', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightArm', 'RightForeArm']

corps_name_1 = ['Pelvis', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'Hips', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Head', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand']
corps_name_2 = ['Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'LeftToe_End', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'RightToe_End', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Head', 'HeadTop_End', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand']
corps_name_3 = ['Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'RightUpLeg', 'RightLeg', 'RightFoot', 'Spine', 'Spine1', 'Neck', 'Head', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand']
corps_name_boss = ['Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Neck1', 'Head', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand']
corps_name_boss2 = ['Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'Left_End', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'Right_End', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Neck1', 'Head', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand']
corps_name_cmu = ['Hips', 'LHipJoint', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'RHipJoint', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'LowerBack', 'Spine', 'Spine1', 'Neck', 'Neck1', 'Head', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand']
corps_name_monkey = ['Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'Spine', 'Spine1', 'Neck', 'Head', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand']
corps_name_three_arms = ['Three_Arms_Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'Spine', 'Spine1', 'Neck', 'Head', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand']
corps_name_three_arms_split = ['Three_Arms_split_Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'Spine', 'Spine1', 'Neck', 'Head', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'LeftHand_split', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand', 'RightHand_split']
corps_name_Prisoner = ['HipsPrisoner', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'LeftToe_End', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'RightToe_End', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Head', 'HeadTop_End', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightArm', 'RightForeArm']
corps_name_mixamo2_m = ['Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'LeftToe_End', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'RightToe_End', 'Spine', 'Spine1', 'Spine1_split', 'Spine2', 'Neck', 'Head', 'HeadTop_End', 'LeftShoulder', 'LeftShoulder_split', 'LeftArm', 'LeftForeArm', 'LeftHand', 'RightShoulder', 'RightShoulder_split', 'RightArm', 'RightForeArm', 'RightHand']
# corps_name_example = ['Root', 'LeftUpLeg', ..., 'LeftToe', 'RightUpLeg', ..., 'RightToe', 'Spine', ..., 'Head', 'LeftShoulder', ..., 'LeftHand', 'RightShoulder', ..., 'RightHand']
#
"""
2.
Specify five end effectors' name.
Please follow the same order as in 1.
"""
ee_name_1 = ['LeftToeBase', 'RightToeBase', 'Head', 'LeftHand', 'RightHand']
ee_name_2 = ['LeftToe_End', 'RightToe_End', 'HeadTop_End', 'LeftHand', 'RightHand']
ee_name_3 = ['LeftFoot', 'RightFoot', 'Head', 'LeftHand', 'RightHand']
ee_name_cmu = ['LeftToeBase', 'RightToeBase', 'Head', 'LeftHand', 'RightHand']
ee_name_monkey = ['LeftToeBase', 'RightToeBase', 'Head', 'LeftHand', 'RightHand']
ee_name_three_arms_split = ['LeftToeBase', 'RightToeBase', 'Head', 'LeftHand_split', 'RightHand_split']
ee_name_Prisoner = ['LeftToe_End', 'RightToe_End', 'HeadTop_End', 'LeftHand', 'RightForeArm']
# ee_name_example = ['LeftToe', 'RightToe', 'Head', 'LeftHand', 'RightHand']


corps_names = [corps_name_1, corps_name_2, corps_name_3, corps_name_cmu, corps_name_monkey, corps_name_boss,
               corps_name_boss, corps_name_three_arms, corps_name_three_arms_split, corps_name_Prisoner, corps_name_mixamo2_m]
ee_names = [ee_name_1, ee_name_2, ee_name_3, ee_name_cmu, ee_name_monkey, ee_name_1, ee_name_1, ee_name_1, ee_name_three_arms_split, ee_name_Prisoner, ee_name_2]

full_fill = [1] * len(corps_names)
for i, ref_names in enumerate(corps_names):
    for ref_name in ref_names:
        if ref_name not in names:
            full_fill[i] = 0
            break
print(full_fill)
skeleton_type=-1
if full_fill[3]:
    skeleton_type = 3
else:
    for i, _ in enumerate(full_fill):
        if full_fill[i]:
            skeleton_type = i
            break

if skeleton_type == 2 and full_fill[4]:
    skeleton_type = 4

if 'Neck1' in names:
    skeleton_type = 5
if 'Left_End' in names:
    skeleton_type = 6
if 'Three_Arms_Hips' in names:
    skeleton_type = 7
if 'Three_Arms_Hips_split' in names:
    skeleton_type = 8

if 'LHipJoint' in names:
    skeleton_type = 3

if 'HipsPrisoner' in names:
    skeleton_type = 9

if 'Spine1_split' in names:
    skeleton_type = 10

print(skeleton_type)
corps = []


for name in corps_names[skeleton_type]:
    for j in range(anim.shape[1]):
        if name == names[j]:
            corps.append(j)
            break
print(len(corps_names[skeleton_type]))
print(corps)
print(len(corps))