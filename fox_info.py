import sys
import os
import json
import datetime
import shutil
import subprocess

fox_folder_path = os.path.dirname(os.path.abspath(__file__))
fox_envs_folder_path = os.path.join(fox_folder_path, 'fox_envs')
fox_data_path = os.path.join(fox_folder_path, 'fox_data')
fox_scripts_path = os.path.join(fox_folder_path, 'fox_scripts')
fox_package_vault = os.path.join(fox_folder_path, 'fox_package_vault')

def help_():
    print('no help here')
    return

def get_time():  ## done

    now = datetime.datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")

def get_package_list():  ## done

    proc = subprocess.Popen(['pip', 'freeze', '--disable-pip-version-check'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    print(proc)
    ## filter pip
    return installed_packages_list

def fetch_data(data_name):

    data_path = os.path.join(fox_data_path, f'{data_name}.json')

    with open(data_path, 'r') as file:
        dict = json.load(file)

    return dict

def save_data(data_name, dict):

    data_path = os.path.join(fox_data_path, f'{data_name}.json')

    with open(data_path, 'w') as file:
        json.dump(dict, file, sort_keys = True, indent = 4)

    return 'done'

def check_for_active_env():

    dict = fetch_data('fox_envs_data')
    python_path = executable_python()

    list_of_scripts = [ i for i in dict['env_script_paths']]

    if (python_path in list_of_scripts) == True : # True

        env_name = dict['env_script_paths'][python_path]

    elif (python_path in list_of_scripts) == False :
        env_name = None

    return env_name

def executable_python():
    # python.exe folder path and python.exe
    # path , _ = os.path.split(sys.executable)
    output = subprocess.run(f'python {fox_folder_path}\\external.py exe_python', shell=True, stdout=subprocess.PIPE )
    path = output.stdout.decode('utf-8')

    return os.path.normpath(path.rstrip())

def freeze(printable = True):

    # env_name = fox_info.check_for_active_env()
    #
    # env_path = os.path.join(fox_envs_folder_path, env_name)

    pip_command = ['pip','freeze']

    output = subprocess.run(pip_command, stdout=subprocess.PIPE )

    packages = output.stdout.decode('utf-8')

    if printable == True:
        print(packages)

    packages = packages.splitlines()

    pkk = ''

    for i in packages:
        i = i.replace('==','__')
        pkk = pkk + i + ':'
    pkk = pkk[:-1]

    if printable == True:
        print(pkk)

    return pkk

def reset_env_map_data():

    dict = {
        'envs':{

        }
    }

    save_data('env_map', dict)

    print(dict)

    return 'done'

def reset_fox_envs_data():

    # authenticate('admin', 'user')

    dict = {
        'env_list' : {},
        'env_names_list' : [],
        'env_script_paths' : {}
    }

    save_data('fox_envs_data', dict)

    print(dict)

    return 'done'

def commands():

    print(' ')
    print('- fox info')
    print('- fox help')
    print('- fox commands')
    print('- fox list_envs')
    print('- fox env_info <env_name>')
    print('- fox create <env_name>')
    print('- fox burn <env_name>')
    print('- fox activate <env_name>')
    print('- fox deactivate                         (Call inside env only)')
    print('- fox install <package_name>             (Call Inside env only)')
    print('- fox remove <package_name>              (Call Inside env only)')
    print('- fox list_versions                      (Call Inside env only)')
    print('- fox change_version <version_number>    (Call Inside env only)')
    print('- fox freeze')
    print('- fox melt')

    return

def list_envs():

    env_list = fetch_data('fox_envs_data')['env_names_list']

    if len(env_list) == 0:
        print('- No envs found')

    else:
        for env in env_list:
            print(f'- {env}')

    return env_list

def env_info(env_name):

    if env_name == None:

        env_name = check_for_active_env()

    if env_name == None:

        print(f"- enter a env name as ")
        print(f'- fox env_info <env_name>')

    else:
        try:
            env_data = fetch_data('fox_envs_data')['env_list'][env_name]

            print(" ")
            print(f"- env_name          : {env_data['env_name']}")
            print(f"- env_status        : {env_data['env_status']}")
            print(f"- total_versions    : {env_data['total_versions']}")
            print(f"- python_version    : {env_data['python_version']}")
            import fox_version_control
            fox_version_control.list_versions(env_name)
        except KeyError:
            print('- env not found')

def info():

    print('- FOX 2021 (C) COPYRIGHT @ThBlitz')
    print('- (C) LICENSE        - https://github.com/ThBlitz/Fox/blob/main/LICENSE')
    print('- FOX PROJECT REPO   - https://github.com/ThBlitz/Fox')

    return
