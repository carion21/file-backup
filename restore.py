import os
from shutil import copyfile
import time
from utilities import *

params = get_json_from_file('config/params.json')

try:
    if not os.path.exists(params['folder_to_backup']):
        os.makedirs(params['folder_to_backup'])
    print('-'*50)

    intput_files = os.listdir(params['folder_to_backup'])
    output_files = os.listdir(params['folder_of_backup'])

    files_to_backup = list(set(output_files) - set(intput_files))

    if len(files_to_backup) > 0:
        print('Restoring ' + str(len(files_to_backup)) + ' files...')
        list(
            map(
                lambda file: move_file(
                    params['folder_of_backup'] + file,
                    params['folder_to_backup'] + file
                ),
                files_to_backup
            )
        )
    else:
        print('No new files to restore.')

except Exception as e:
    print(e)

