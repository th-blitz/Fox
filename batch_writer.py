import fox_info

def edit_fox_env_bat(file_path):

    path = fox_info.executable_python()
    path = path.split('\\')[-1]

    list_of_lines = [f'''    call set "PROMPT=%%PROMPT:%farg%=({path})%%"''',
        f'''    call set "PROMPT=%%PROMPT:%farg%=({path})%%"'''
    ]

    count_list = [7,21]

    insert_lines_in_file(file_path, list_of_lines, count_list)

    return


def insert_lines_in_file(file_path, list_of_lines, count_list):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    line_list = []
    index = 0
    prev_count = None
    added_lines = 0

    for count in count_list:
        line_num = count + added_lines - 1
        lines.insert(line_num, f"{list_of_lines[index]}\n")
        added_lines = added_lines + 1
        index = index + 1

    with open(file_path, 'w') as file:
        file.writelines(lines)

    return
