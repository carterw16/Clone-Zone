import os
import json
import bvhio
import numpy as np

# motionet_to_coco19 = {
#     0: 2,   # Hip → COCO19[2]
#     1: 12,   # Right Hip → COCO19[12]
#     2: 13,   # Right Knee → COCO19[13]
#     3: 14,  # Right Foot → COCO19[14]
#     4: 6,  # Left Hip → COCO19[6]
#     5: 7,   # Left Knee → COCO19[7]
#     6: 8,   # Left Foot → COCO19[8]
#     7: None,   # Spine → None
#     8: None,  # Thorax → None
#     9: [0,1],  # Neck/Nose → COCO19[0,1]
#     10: None,  # Head → None
#     11: 3,  # Left Shoulder → COCO19[3]
#     12: 4,  # Left Elbow → COCO19[4]
#     13: 11,  # Left Wrist → COCO19[11]
#     14: 9,  # Right Shoulder → COCO19[9]
#     15: 10,  # Right Elbow → COCO19[10]
#     16: 11,  # Right Wrist → COCO19[11]
# }

# def extract_keypoints_from_bvh(bvh_file_path):
#     """
#     Extract 3D keypoints from a BVH file using bvhio.

#     Args:
#         bvh_file_path (str): Path to the BVH file.

#     Returns:
#         np.ndarray: A numpy array of shape (num_frames, num_joints, 3) containing 3D keypoints.
#     """
#     # Load BVH file as a hierarchical structure
#     root = bvhio.readAsHierarchy(bvh_file_path)

#     # Initialize a list to store keypoints for all frames
#     all_keypoints = []

#     # Iterate through all frames
#     # Total number of frames
#     for frame_id in range(root.getKeyframeRange()[1] + 1):
#         root.loadPose(frame_id)  # Load pose for the current frame
#         frame_keypoints = []

#         # Extract position of each joint in world space
#         for joint, index, depth in root.layout():
#             frame_keypoints.append(joint.PositionWorld)  # World-space position

#         all_keypoints.append(frame_keypoints)

#     return np.array(all_keypoints)  # Convert to numpy array


# # Example usage
# motionet_keypoints = extract_keypoints_from_bvh('motionet_output.bvh')
# tdpt_keypoints = extract_keypoints_from_bvh('tdpt_output.bvh')


def parse_ground_truth(json_folder_path):
    """
    Parse ground truth JSON files and extract 3D keypoints.

    Args:
        json_folder_path (str): Path to the folder containing Body3DScene_<file_number>.json files.

    Returns:
        dict: A dictionary with frame indices as keys and numpy arrays of shape (num_bodies, num_joints, 3) as values.
    """
    ground_truth_data = {}

    for file_name in sorted(os.listdir(json_folder_path)):
        if file_name.endswith(".json"):
            file_path = os.path.join(json_folder_path, file_name)
            with open(file_path, 'r') as f:
                data = json.load(f)

            frame_idx = int(file_name.split('_')[-1].split('.')[0])
            bodies = data.get("bodies", [])

            # Extract joints19 for each body in the frame
            frame_keypoints = []
            for body in bodies:
                joints19 = body.get("joints19", [])
                joints19_xyz = np.array(
                    joints19).reshape(-1, 4)[:, :3]  # x, y, z only
                frame_keypoints.append(joints19_xyz)

            ground_truth_data[frame_idx] = np.array(frame_keypoints)

    return ground_truth_data


ground_truth_keypoints = parse_ground_truth('171204_pose1_sample/hdPose3d_stage1_coco19')


# def compute_mpjpe(predicted_keypoints, ground_truth_keypoints):
#     """
#     Compute Mean Per Joint Position Error (MPJPE).

#     Args:
#         predicted_keypoints (np.ndarray): Predicted keypoints of shape (num_frames, num_joints, 3).
#         ground_truth_keypoints (dict): Ground truth keypoints as a dictionary with frame indices as keys.

#     Returns:
#         float: The MPJPE value.
#     """
#     total_error = 0.0
#     total_joints = 0

#     for frame_idx in range(predicted_keypoints.shape[0]):
#         if frame_idx in ground_truth_keypoints:
#             gt_frame_data = ground_truth_keypoints[frame_idx]

#             if len(gt_frame_data) > 0:  # Assuming single person detection for simplicity
#                 # First detected person in the frame
#                 gt_joints = gt_frame_data[0]

#                 pred_joints = predicted_keypoints[frame_idx]

#                 if pred_joints.shape == gt_joints.shape:  # Ensure both have same number of joints
#                     error_per_joint = np.linalg.norm(
#                         pred_joints - gt_joints, axis=1)
#                     total_error += np.sum(error_per_joint)
#                     total_joints += pred_joints.shape[0]

#     return total_error / total_joints if total_joints > 0 else float('inf')

# def compute_mpjpe_adjusted(predicted_keypoints, ground_truth_keypoints):
#     """
#     Compute MPJPE while handling missing keypoints.

#     Args:
#         predicted_keypoints (np.ndarray): Predicted keypoints of shape `(num_frames, num_joints_predicted, 3)`.
#         ground_truth_keypoints (np.ndarray): Ground truth keypoints of shape `(num_frames, num_joints_ground_truth, 3)`.

#     Returns:
#         float: Adjusted MPJPE value.
#     """
#     valid_indices = ~np.isnan(predicted_keypoints).any(
#         axis=2) & ~np.isnan(ground_truth_keypoints).any(axis=2)

#     total_error = np.sum(
#         np.linalg.norm(
#             predicted_keypoints[valid_indices] - ground_truth_keypoints[valid_indices], axis=1)
#     )

#     total_joints = np.sum(valid_indices)

#     return total_error / total_joints if total_joints > 0 else float('inf')


def parse_bvh_to_world(bvh_path):

    # The package allows to make modifcation on the animation data very conviniently.
    root = bvhio.readAsHierarchy(bvh_path)

    # Add a root bone to the hierarchy and set itself as 'root'.
    root = bvhio.Joint('Root').attach(root, keep=['position', 'rotation', 'scale'])

    # Scale so the data represent roughly meters, assuming the data is in inches.
    # Because the scale is on the root and the rest pose, it is applied to all world space data.
    # root.RestPose.Scale = 0.0254

    # this bakes the rest pos scale of 0.0254 into the positions,
    # so that the scale can be reseted to 1 again.
    # root.applyRestposeScale(recursive=True, bakeKeyframes=True)

    # tursn the animation by 180 degrees.
    # Keep in mind that local keyframe and child rest pose data is still untouched.
    # root.RestPose.addEuler((0, 180, 0))

    # Set all joints to the first keyframe.
    # The animation pose is calculated by -> Pose = RestPose + Keyframe.
    root.loadPose(0)

    # print info
    print('\nPosition and Y-direction of each joint in world space ')
    for joint, index, depth in root.layout():
        print(f'{joint.PositionWorld} {joint.UpWorld} {joint.Name}')

# Motionet specific processing
def process_motionet(bvh_path):
    """Convert Motionet BVH to COCO19 format"""
    frames, joints = parse_bvh_to_world(bvh_path)

    # Motionet joint mapping to COCO19 indices
    MOTIONET_MAP = {
        'Hips': 2,        # BodyCenter (calculated below)
        'Neck': 0,
        'Head': 1,
        'LeftShoulder': 3,
        'LeftArm': 4,
        'LeftHand': 5,
        'RightShoulder': 9,
        'RightArm': 10,
        'RightHand': 11,
        'LeftUpLeg': 6,
        'LeftLeg': 7,
        'LeftFoot': 8,
        'RightUpLeg': 12,
        'RightLeg': 13,
        'RightFoot': 14
    }

    # Calculate BodyCenter as midpoint between hips
    left_hip = frames[:, joints.index('LeftUpLeg')]
    right_hip = frames[:, joints.index('RightUpLeg')]
    body_center = (left_hip + right_hip) / 2

    # Build output array
    output = np.full((len(frames), 19, 3), np.nan)
    for joint, idx in MOTIONET_MAP.items():
        output[:, idx] = frames[:, joints.index(joint)]

    output[:, 2] = body_center  # Insert calculated BodyCenter
    return output

# TDPT specific processing


def process_tdpt(bvh_path):
    """Convert TDPT BVH to COCO19 format"""
    frames, joints = parse_bvh_to_world(bvh_path)

    # TDPT joint mapping to COCO19 indices
    TDPT_MAP = {
        'Spine2': 0,      # Neck
        'Head': 1,
        'LeftShoulder': 3,
        'LeftArm': 4,
        'LeftHand': 5,
        'RightShoulder': 9,
        'RightArm': 10,
        'RightHand': 11,
        'LeftUpLeg': 6,
        'LeftLeg': 7,
        'LeftFoot': 8,
        'RightUpLeg': 12,
        'RightLeg': 13,
        'RightFoot': 14,
        'LeftEye': 16,
        'RightEye': 15,
        'LeftEar': 18,
        'RightEar': 17
    }

    # Calculate BodyCenter
    left_hip = frames[:, joints.index('LeftUpLeg')]
    right_hip = frames[:, joints.index('RightUpLeg')]
    body_center = (left_hip + right_hip) / 2

    # Build output array
    output = np.full((len(frames), 19, 3), np.nan)
    for joint, idx in TDPT_MAP.items():
        output[:, idx] = frames[:, joints.index(joint)]

    output[:, 2] = body_center  # Insert calculated BodyCenter
    return output


def compute_mpjpe(predicted, ground_truth):
    """Robust MPJPE calculation with NaN handling"""
    valid = ~np.isnan(predicted).any(
        axis=-1) & ~np.isnan(ground_truth).any(axis=-1)
    return np.linalg.norm(predicted[valid] - ground_truth[valid], axis=-1).mean()


# motionet_keypoints = parse_bvh_to_world('motionet_output.bvh')
# tdpt_keypoints = parse_bvh_to_world('tdpt_output.bvh')
print(ground_truth_keypoints.shape)
print(ground_truth_keypoints[0])
# print(motionet_keypoints[0].shape)
# print(motionet_keypoints[0])
# print(tdpt_keypoints[0].shape)
# print(tdpt_keypoints[0])
# Example usage
# motionet_mpjpe = compute_mpjpe(motionet_keypoints, ground_truth_keypoints)
# tdpt_mpjpe = compute_mpjpe(tdpt_keypoints, ground_truth_keypoints)

# print(f"Motionet MPJPE: {motionet_mpjpe:.2f}")
# print(f"TDPT MPJPE: {tdpt_mpjpe:.2f}")
