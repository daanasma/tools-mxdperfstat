import glob
import os
import subprocess
import time
import shutil

import mxdperfstat_config as config

output_folder = os.path.join(config.mxd_input_directory, 'output_mxdperfstat')

def create_folder_if_not_exists(foldername, overwrite=False):
    if overwrite:
        try:
            shutil.rmtree(foldername)
            print('Removed folder: {}'.format(foldername))
        except Exception as e:
            print('Couldnt remove folder: %s' %foldername)
            print(e)

    time.sleep(0.3)
    if not os.path.exists(foldername):
        print('Creating folder: {}'.format(foldername))
        os.makedirs(foldername)
    else:
        print('Folder already exists: {}'.format(foldername))

def copy_file_to_directory(input_filepath, target_directory):
    filename = os.path.basename(input_filepath)
    output_filepath = os.path.join(target_directory, filename)
    shutil.copyfile(input_filepath, output_filepath)
    print('Copied {} to {}'.format(filename, target_directory))

def list_all_files_with_ext(input_directory, ext):
    return glob.glob(os.path.join(input_directory, '*.{}'.format(ext)))

def run_mxd_perfstat_on_mxds(list_of_mxds):
    for mxd_path in list_of_mxds:
        print('Start checking mxd: {}'.format(mxd_path))
        final_command = r'{} -mxd {} -scale {}'.format(config.mxd_perfstat_tool,
                                                       mxd_path,
                                                       config.scales_to_check)
        subprocess.call(final_command)
        print('Finished Checking mxd.')


def main():
    create_folder_if_not_exists(output_folder, overwrite=True)
    copy_file_to_directory('mxdperfstat.xsl', output_folder)
    os.chdir(output_folder)
    all_mxds = list_all_files_with_ext(config.mxd_input_directory, 'mxd')
    run_mxd_perfstat_on_mxds(all_mxds)
    print('Finished all. Enjoy')

if __name__ == '__main__':
    main()