## 0. default_fox_files_map

# [fox_folder_path] - Fox_python --- fox_envs \  [fox_env_path]
        #                             | --- env_2
        #                             | --- env_1
        #                         --- fox_scripts \   [fox_scripts_path]
        #                             | --- fox.bat
        #                         --- fox_blockchain \      (none)
        #                             | --- *** (empty)
        #                         --- fox_data \               [fox_data_path]
        #                             | --- fox_envs_data.json
        #                             | --- fox_git_data.json
        #                             | --- pip_firewall.csv
        #                             | --- (others if needed)
        #                         --- fox_package_vault \
        #                             | --- package_data.csv
        #                             | --- (all packages)
        #                         --- fox.py
        #                         --- bridge.py
        #                         --- fox_info.py
        #                         --- fox_version_control.py
        #                         --- fox_package.py
        #                         --- fox_editor.py
        #                         --- PIP_FIREWALL.py
        #                         --- fox_network.py
        #                         --- fox_security.py

## 1 . check for all files in , default_fox_files_map.

## 2 . make required changes for stage 3.

## 3 . loop through. for repairs . errors. etc.

import os
import sys

default_fox_files_map = {
    'fox_envs_dir' : {},
    'fox_scripts_dir' : [],
    'fox_blockchain_dir' : None,
    'fox_data_dir' : ['fox_envs_data.json'],
    'fox_package_vault' : None,
    'python_files':['fox.py', 'bridge.py', 'fox_info.py', 'fox_editor.py', 'fox_package.py', 'fox_version_control.py'
    'PIP_FIREWALL.py', 'fox_network.py', 'fox_security.py']
}
