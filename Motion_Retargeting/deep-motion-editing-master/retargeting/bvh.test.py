from datasets.bvh_parser import BVH_file
file = "datasets/Mixamo/Aj/Dancing Running Man.bvh"
file = BVH_file(file)
# print(path)
# print(file.skeleton_type)
motion = file.to_tensor(quater=True)
print(motion.shape)
motion = motion[:, ::2]
print(motion.shape)
length = motion.shape[-1]
length = length // 4 * 4
print(length)
new_motion = motion[..., :length]
print(new_motion.shape)