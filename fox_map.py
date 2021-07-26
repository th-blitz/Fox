import os
import sys
import fox_info
import copy

fox_folder_path = os.path.dirname(os.path.abspath(__file__))
fox_envs_folder_path = os.path.join(fox_folder_path, 'fox_envs')
fox_data_path = os.path.join(fox_folder_path, 'fox_data')
fox_scripts_path = os.path.join(fox_folder_path, 'fox_scripts')
fox_package_vault = os.path.join(fox_folder_path, 'fox_package_vault')

default_env_map = {
        'env_name' : 'base',
        'Include' : [],
        'site-packages' : ['distutils-precedence.pth', 'pip', 'pip-21.1.1.dist-info', 'pkg_resources', 'setuptools', 'setuptools-56.0.0.dist-info', '_distutils_hack'],
        'Scripts' : ['activate', 'Activate.ps1', 'deactivate.bat', 'fox_base.bat', 'pip.exe', 'pip3.8.exe', 'pip3.exe', 'python.exe', 'pythonw.exe'],
}

def register_env(env_name):
    env_map = map_env(env_name)

    dict = fox_info.fetch_data('env_map')

    dict['envs'].update({
        env_name:{
            'total_versions':0,
            'version':{
                '0':env_map
                }
            }
        })

    fox_info.save_data('env_map',dict)

    return

def register_version():

    env_name = fox_info.check_for_active_env()
    dict = fox_info.fetch_data('env_map')

    total_versions = dict['envs'][env_name]['total_versions']
    total_versions = total_versions + 1

    env_map = map_env(env_name)

    version_dict = {
        f'{total_versions}':env_map
    }

    dict['envs'][env_name]['total_versions'] = total_versions
    dict['envs'][env_name]['version'].update(version_dict)
    fox_info.save_data('env_map', dict)

def map_env(env_name=fox_info.check_for_active_env()):

    dict = fox_info.fetch_data('fox_envs_data')

    env_path = dict['env_list'][env_name]['env_final_path']

    sub_paths = {}
    for i in os.listdir(env_path):

        if i == 'Lib':
            a = os.path.join(i, 'site-packages')
            i = 'site-packages'
        else:
            a = i

        path = os.path.join(env_path, a )

        if os.path.isdir(path):
            files = []
            for file in os.listdir(path):
                files.append(file)
            sub_paths.update({f'{i}' : files})

    sub_paths.update({'env_name' : env_name})
    try:
        sub_paths['site-packages'].remove('__pycache__')
        sub_paths['Scripts'].remove('__pycache__')
    except:
        pass

    return sub_paths

def cmp_map(env_name=fox_info.check_for_active_env()):

    dict = fox_info.fetch_data('env_map')
    total_versions = dict['envs'][env_name]['total_versions']
    if total_versions < 1:
        return 'error'
    else:

        map_1 = dict['envs'][env_name]['version'][f'{total_versions}']
        map_2 = dict['envs'][env_name]['version'][f'{total_versions-1}']

        positive_map = compare_map( map_1, map_2)

        if len(positive_map['site-packages'])==0 and len(positive_map['Scripts'])==0:
            positive_map = None
            positive = False
        else:
            positive = True

        negative_map = compare_map( map_2, map_1 )

        if len(negative_map['site-packages'])==0 and len(negative_map['Scripts'])==0:
            negative_map = None
            negative = False
        else:
            negative = True

        return positive_map , negative_map , positive , negative

def compare_map( map_1 , map_2 = default_env_map ):

    map_1 = copy.deepcopy(map_1)
    map_2 = copy.deepcopy(map_2)

    env_name = map_2['env_name']
    map_2.pop('env_name')

    map_2['Scripts'].remove(f'fox_{env_name}.bat')

    env_name = map_1['env_name']
    map_1.pop('env_name')

    map_1['Scripts'].remove(f'fox_{env_name}.bat')

    for i in map_2:
        files = map_2[i]
        for file in files:
            try:
                map_1[i].remove(file)
            except:
                pass

    return map_1

def check_map(package):
    pass

def map(package):
    pass

def set_default(package):
    pass
