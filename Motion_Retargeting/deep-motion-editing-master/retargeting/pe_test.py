import os
from datasets.bvh_parser import BVH_file
from datasets.bvh_writer import BVH_writer
from models.IK import fix_foot_contact
from os.path import join as pjoin


# downsampling and remove redundant joints
def copy_ref_file(src, dst):
    file = BVH_file(src)
    writer = BVH_writer(file.edges, file.names)
    writer.write_raw(file.to_tensor(quater=True)[..., ::2], 'quaternion', dst)


def get_height(file):
    file = BVH_file(file)
    return file.get_height()


def example(src_name, dest_name, src_bvh_name, dest_bvh_name, test_type, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    input_file = './datasets/Mixamo/{}/{}'.format(src_name, src_bvh_name)
    ref_file = './datasets/Mixamo/{}/{}'.format(dest_name, dest_bvh_name)
    copy_ref_file(input_file, pjoin(output_path, 'input.bvh'))
    copy_ref_file(ref_file, pjoin(output_path, 'gt.bvh'))
    height = get_height(input_file)

    src_bvh_name = src_bvh_name.replace(' ', '_')
    dest_bvh_name = dest_bvh_name.replace(' ','_')
    input_file = './datasets/Mixamo/{}/{}'.format(src_name, src_bvh_name)
    ref_file = './datasets/Mixamo/{}/{}'.format(dest_name, dest_bvh_name)

    cmd = 'python retarget_single_pair.py --input_bvh={} --target_bvh={} --output_filename={} --test_type={}'.format(
        input_file, ref_file, pjoin(output_path, 'result.bvh'), test_type
    )
    os.system(cmd)

    fix_foot_contact(pjoin(output_path, 'result.bvh'),
                     pjoin(output_path, 'input.bvh'),
                     pjoin(output_path, 'result.bvh'),
                     height)


if __name__ == '__main__':
    #example('Aj', 'BigVegas', 'Dancing Running Man.bvh','Box Turn.bvh', 'cross', './examples/Test')
    #example('Aj', 'Mousey_m', 'Dual Weapon Combo.bvh','Box Turn.bvh', 'cross', './examples/Test')
    example('PE', 'Mousey_m', 'dance.bvh', 'Box Turn.bvh', 'cross', './examples/Test4')
    #example('PE', 'Aj', 'dance.bvh', 'Box Turn.bvh', 'intra', './examples/Test3')
    print('Finished!')
