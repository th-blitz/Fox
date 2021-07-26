import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':

    try:
        command = str(sys.argv[1])
    except:
        command = None

    try:
        arg_2 = str(sys.argv[2])

    except:
        arg_2 = None
        pass

    try:
        arg_3 = str(sys.argv[3])
    except:
        arg_3 = None
        pass

    access = None

    if command == None:
        command = 'commands'

    command_info_list = ['help', 'commands', 'reset_fox_envs_data', 'reset_env_map_data', 'freeze',
    'list_envs', 'env_info', 'info']

    command_editor_list = ['create', 'burn', 'rename', 'clone']

    command_version_control_list = ['list_versions', 'change_version']

    command_package_list = ['install', 'remove', 'register', 'melt']

    command_team_list = ['init']

    if command in command_team_list:

        import fox_team

        if command == 'init':
            fox_team.add_project(arg_2)

        access = True

    elif command in command_info_list:


        import fox_info

        if command == 'help':
            fox_info.help_()

        elif command == 'commands':
            fox_info.commands()

        elif command == 'reset_fox_envs_data':
            fox_info.reset_fox_envs_data()

        elif command == 'reset_env_map_data':
            fox_info.reset_env_map_data()

        elif command == 'freeze':
            fox_info.freeze()

        elif command == 'list_envs':
            fox_info.list_envs()

        elif command == 'env_info':
            fox_info.env_info(arg_2)

        elif command == 'info':
            fox_info.info()

        access = True

    elif command in command_editor_list:

        import fox_editor

        if command == 'create':
            fox_editor.create(arg_2, arg_3)

        elif command == 'burn':
            fox_editor.burn(arg_2)

        elif command == 'rename':
            fox_editor.rename(arg_2, arg_3)

        elif command == 'clone':
            fox_editor.clone(arg_2, arg_3)

        access = True

    elif command in command_version_control_list:

        import fox_version_control

        if command == 'list_versions':
            fox_version_control.list_versions()

        elif command == 'change_version':
            fox_version_control.change_version_to(arg_2)

        access = True

    elif command in command_package_list:

        import fox_package

        if command == 'install':
            fox_package.install(arg_2)

        elif command == 'remove':
            fox_package.remove(arg_2)

        elif command == 'register':
            fox_package.register(arg_2)

        elif command == 'melt':
            fox_package.melt(arg_2)

        access = True

    elif command == 'deactivate':

        print('- fox activate <env_name> ( To activate the env )')
        print(' ')
        access = True

    elif command == 'activate':

        import fox_info
        env_list = fox_info.fetch_data('fox_envs_data')['env_names_list']

        if arg_2 != None and arg_2 in env_list:

            print('- fox deactivate ( To deactivate from the env )')
            access = True

        else:

            print('- Enter a valid env name')
            print('- fox activate <env_name> ')


    if access == None :
        print('- FOX command unlisted, enter $ fox ( to get a list of all the commands )')

    elif access == False:
        access_message = 'none'
        print(f'{access_message}')

    else:
        pass
