import fox_editor
import fox_info
import fox_package
import json
import shutil
import os

fox_folder_path = os.path.dirname(os.path.abspath(__file__))
fox_envs_folder_path = os.path.join(fox_folder_path, 'fox_envs')
fox_data_path = os.path.join(fox_folder_path, 'fox_data')
fox_scripts_path = os.path.join(fox_folder_path, 'fox_scripts')
fox_package_vault = os.path.join(fox_folder_path, 'fox_package_vault')

def register_env(env_name, final_path, bat_path, ver):

    dict = fox_info.fetch_data('fox_envs_data')

    env_info = {
        'env_name' : env_name,
        'env_final_path' : final_path,
        'env_script_path': bat_path,
        'env_status' : 'intact',
        'total_versions' : 0,## active, intact, broken and deleted
        'python_version' : ver,
        'version' : {
            '0' : {
                'date_time_created' : fox_info.get_time(),
                'pip_command' : '',
                'package_list' : []
            }
        }
    }

    dict['env_list'].update({env_name : env_info})
    dict['env_names_list'].append(env_name)
    dict['env_script_paths'].update({bat_path : env_name})

    fox_info.save_data('fox_envs_data', dict)

    return

def register_version(pip_command):

    dict = fox_info.fetch_data('fox_envs_data')

    env_name = fox_info.check_for_active_env()

    total_versions = dict['env_list'][env_name]['total_versions']
    total_versions = total_versions + 1

    version_dict = {
        f'{total_versions}' : {
            'date_time_created' : fox_info.get_time(),
            'pip_command' : pip_command,
            'package_list' : fox_info.freeze(printable = False).replace('__', '==').split(':')
        }
    }

    dict['env_list'][env_name]['version'].update(version_dict)
    dict['env_list'][env_name]['total_versions'] = total_versions

    fox_info.save_data('fox_envs_data', dict)

    return


def list_versions(env_name = fox_info.check_for_active_env()):


    dict = fox_info.fetch_data('fox_envs_data')

    list_of_versions = dict['env_list'][env_name]['version']
    num_of_versions = dict['env_list'][env_name]['total_versions']

    print('\n')
    print(f'- total_versions : {num_of_versions}')
    print('\n')
    for num in list_of_versions:
        print(f'- version_number :: {num}')
        print('--------------------------------------------')
        for n in list_of_versions[num]:
            if n == 'package_list':
                print(f'- {n}')
                print('-----------------')
                for i in list_of_versions[num][n]:
                    print(f"- {i}")
            else:
                print(f'- {n} :: {list_of_versions[num][n]}' )
        print('\n')

    return


def change_version_to( version_num ):

    # env_name = fox_info.check_for_active_env()
    #
    # dict = fox_info.fetch_data('fox_envs_data')
    #
    # if env_name in dict['env_names_list']:
    #
    #     list_of_packages = fox_info.freeze( printable = False).split(':')
    #
    #     for package in list_of_packages:
    #         package = package.replace('__','==')
    #         fox_package.remove(package, dont_register = True)
    #
    #     list_of_packages_1 = dict['env_list'][env_name]['version'][version_num]['package_list']
    #     pip_command = dict['env_list'][env_name]['version'][version_num]['pip_command']
    #
    #     fox_package.melt()

    return
