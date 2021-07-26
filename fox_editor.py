import sys
import os
import fox_info
import shutil
import json
import fox_map
import fox_version_control
import subprocess
import batch_writer

fox_folder_path = os.path.dirname(os.path.abspath(__file__))
fox_envs_folder_path = os.path.join(fox_folder_path, 'fox_envs')
fox_data_path = os.path.join(fox_folder_path, 'fox_data')
fox_scripts_path = os.path.join(fox_folder_path, 'fox_scripts')
fox_package_vault = os.path.join(fox_folder_path, 'fox_package_vault')

virtual_env = os.path.join(fox_folder_path, r'fox_py\\Scripts\\virtualenv.exe')
py_executable = fox_info.executable_python()

def ver_func():
    output = subprocess.run(f'python {fox_folder_path}\\external.py ver',
        shell=True, stdout=subprocess.PIPE
    )
    ver = output.stdout.decode('utf-8')
    return ver.rstrip()

ver = ver_func()

def overwrite_permission(env_name):

    print(f'- env by name {env_name} already exists')
    print(f'- overwriting env will completly delete {env_name} data')
    print(f'- instead create your env by a different name if you dont want to overwrite {env_name}')
    y_n = input('- DO YOU WANT TO OVERWRITE ?? [y/n] : ')

    if y_n == 'y':

        burn(env_name)
        create = True

    else:

        create = False

    return create

def create(env_name, teams = False):

    env_list = fox_info.fetch_data('fox_envs_data')['env_names_list']

    if env_name in env_list:

        create = overwrite_permission(env_name)

    else:

        create = True

    if create == True:

        final_path = os.path.join(fox_envs_folder_path, env_name)

        print(' ')
        print(f'- creating virtualenv at {final_path}')

        output = subprocess.run(f'{virtual_env} --python={py_executable}\\python.exe --clear {final_path}',
            shell=True, stdout=subprocess.PIPE
        )
        output = output.stdout.decode('utf-8')
        print('- output from virtualenv')
        print(' ')

        bat_path = os.path.join(final_path,'Scripts')
        ## set_script = f'setx /M path "%path%;{bat_path}"'
        os.rename( os.path.join(bat_path, 'activate.bat'),
            os.path.join(bat_path, f'fox_{env_name}.bat') )

        py_folder_scripts = os.path.join(fox_folder_path, f'fox_scripts')

        raw_path = os.path.join(bat_path, f'fox_{env_name}.bat')

        batch_writer.edit_fox_env_bat(raw_path)

        print(f'- copying fox_{env_name} to {py_folder_scripts}')
        shutil.copy( raw_path,
            py_folder_scripts )

        fox_version_control.register_env(env_name, final_path, bat_path, ver)
        fox_map.register_env(env_name)

        print(f'- created venv at : {final_path}')
        print(' ')
        print('- fox activate <env_name> ( To activate the env )')

    else:

        print('- aborting env create()')

    return 'done'

def burn(env_name):

    dict = fox_info.fetch_data('fox_envs_data')

    if env_name in dict['env_names_list']:
        path = dict['env_list'][env_name]['env_final_path']
        try:
            shutil.rmtree(path)
        except OSError as e:
            print(f'Fox : {e}')
            pass

        dict['env_list'][env_name]['env_status'] = 'deleted'
        dict['env_names_list'].remove(env_name)
        script_path = dict['env_list'][env_name]['env_script_path']
        dict['env_script_paths'].pop(script_path)
        ver = dict['env_list'][env_name]['python_version']
        dict['env_list'].pop(env_name)

        fox_info.save_data('fox_envs_data', dict)

        file_path = os.path.join(f'{fox_scripts_path}', f'fox_{env_name}.bat')
        os.remove(file_path)

        dict = fox_info.fetch_data('env_map')
        dict['envs'].pop(env_name)
        fox_info.save_data('env_map', dict)

        print('Fox : deleted successfully')

    else:
        print('Fox : env not found')

    return 'done'

def rename(env_1 , env_2):
    print('code incomplete')
    pass

def clone(env_1 , env_2):
    print('code incomplete')
    pass
