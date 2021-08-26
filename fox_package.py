import fox_info
import PIP_FIREWALL
import subprocess
import os
import fox_map
import fox_version_control

fox_folder_path = os.path.dirname(os.path.abspath(__file__))
fox_envs_folder_path = os.path.join(fox_folder_path, 'fox_envs')
fox_data_path = os.path.join(fox_folder_path, 'fox_data')
fox_scripts_path = os.path.join(fox_folder_path, 'fox_scripts')
fox_package_vault = os.path.join(fox_folder_path, 'fox_package_vault')

def install(package, version = None, dont_register = False):

    if version != None:
        pip_command = ['pip','install',f'{package}=={version}']

    else:
        pip_command = ['pip','install',f'{package}']
    access = PIP_FIREWALL.access_check( pip_command )

    if access == True :

        subprocess.run(pip_command)
        print(pip_command)

        if dont_register == False:
            ' '.join(pip_command)
            fox_version_control.register_version( pip_command )
            fox_map.register_version()

        # if package_check(package)==False:
        #
        #     addition, subtraction, add, sub = fox_map.cmp_map()
        #     if sub==False and add==True:
        #         register_package(package, addition)

    else:
        print('access_denied')

    return 'done'

def remove(package, dont_register = False):

    pip_command = ['pip','uninstall',f'{package}','-y']
    subprocess.run(pip_command)

    if dont_register == False:
        ' '.join(pip_command)
        fox_version_control.register_version( pip_command )
        fox_map.register_version()
    else:
        pass

    return 'done'

def melt(package_list_str):

    package_list = package_list_str.replace('__', '==').split(':')

    current_packages = fox_info.freeze(printable = False).replace('__', '==').split(':')

    if current_packages != '':

        for i in current_packages:

            remove(i, dont_register = True)

    if package_list != '':

        for i in package_list:

            install(i, dont_register = True)

    return

# def package_check(package_name):
#
#     return False
#
# def find_package_version(package_name):
#
#     env_name = fox_info.check_for_active_env()
#     env_dir = os.path.join(fox_envs_folder_path, env_name)
#     site_packages = os.path.join(env_dir, os.path.join('Lib', 'site-packages'))
#
#     return
#
#
# def register_package(package_name, map, env_name = fox_info.check_for_active_env()):
#
#     env_dir = os.path.join(fox_envs_folder_path, env_name)
#     site_packages = os.path.join(env_dir, os.path.join('Lib', 'site-packages'))
#     scripts = os.path.join(env_dir, 'Scripts')
#
#     package_dir = os.path.join(fox_package_vault, package_name)
#
#
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#
#     return
#
# def add_package(package_name):
#     pass
