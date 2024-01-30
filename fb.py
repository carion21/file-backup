import os
from shutil import copyfile
import time
from utilities import *

params = get_json_from_file('config/params.json')

while True:
    try:
        if not os.path.exists(params['folder_of_backup']):
            os.makedirs(params['folder_of_backup'])
        print('-'*50)

        input_files = os.listdir(params['folder_to_backup'])
        output_files = os.listdir(params['folder_of_backup'])

        files_to_backup = list(set(input_files) - set(output_files))

        if len(files_to_backup) > 0:
            print('Backing up ' + str(len(files_to_backup)) + ' files...')
            list(
                map(
                    lambda file: move_file(
                        params['folder_to_backup'] + file,
                        params['folder_of_backup'] + file
                    ),
                    files_to_backup
                )
            )
        else:
            print('No new files to backup.')

    except Exception as e:
        print(e)

    time.sleep(params['time_interval'])
