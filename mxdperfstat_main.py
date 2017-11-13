import glob
import os
import subprocess
import sys

import mxdperfstat_config as config

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
    all_mxds = list_all_files_with_ext(config.mxd_input_directory, 'mxd')
    run_mxd_perfstat_on_mxds(all_mxds)
    print('Finished all. Move on')

if __name__ == '__main__':
    main()