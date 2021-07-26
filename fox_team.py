import os
import fox_info

fox_folder_path = os.path.dirname(os.path.abspath(__file__))
fox_team = os.path.join(fox_folder_path, 'fox_team')

def add_project(project_dir):

    if project_dir == None:

        project_dir = os.getcwd()

    project_dir = os.path.normpath(project_dir)

    if os.path.isdir(project_dir) == True:

        project_dir_list = project_dir.split('\\')
        project_name = project_dir_list[-1]

        dict = fox_info.fetch_data('projects')
        dict['projects'].update({
            project_name : project_dir
        })

        fox_info.save_data('projects', dict)

        # create .fox folder at project_dir

        print(f'- added {project_dir} to fox projects')

    else:

        print('- dir was not found')

    return

def create(env_name):

    

    return

def add_to_project(env_name):

    return

def remove_from_project(env_name):

    return

def burn(env_name):

    return

def update(env_name):

    return
