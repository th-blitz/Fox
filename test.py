
# import time
# import sys


import fox_secure

# from sympy import factorint
#
# for i in ['2HYap9kFuupv5RYdDL5xEiScXuR4zX3tgRjYZ9rvTyiNJ8', '6g7ej9yZjpqwn1apatS8rHGmV7u6o5gE1rhTP5gqVLMUa5w']:
#     res = fox_secure.hexbase58(i)
#     res = int(res, 16)
#     print(res)
#     res = factorint(res)
#     print(res)

github_url = r'https://github.com/ThBlitz'
key, public_key, public_address = fox_secure.fox_address_generator(github_url, strength = 4)
url, address, checksum, strength = fox_secure.decode_fox_public_address(public_address)

private_key_base58 = fox_secure.hexbase58('fa' + key)
public_key_base58 = fox_secure.hexbase58('fb' + public_key)

print(private_key_base58)
print(public_key_base58)
print(public_address)
print(url, address, checksum, strength)


# animation_1 = r"/-\|/"
#
# for i in range(100):
#     time.sleep(0.04)
#     sys.stdout.write("\r" + f"[...{animation_1[i % len(animation_1)]}]")
#     sys.stdout.flush()
# print ("done")



# dict = {
# 'admin' : {
#     'address': '',
#     'public_key': '',
#     "env_name" : 'base',
#     "date_and_time_of_creation": '',
#     "python_version": '',
#     "hash_type": 'sha3_256',
#     "ecda_curve": 'SECP256k1',
#     "team_length": 1,
# },
#
# "team_members": [
#     {
#         'info' : {
#             'member_address' : '',
#             'member_public_key' : None,
#         },
#
#         'member_auth' : {
#             'member_info_hash': '',
#             'member_info_signature': None,
#         },
#
#         'member_permission': '', #locked #unlocked #manager #admin
#
#         'admin_auth' : {
#             'hash' : '',
#             'admin_signature' : '',
#         },
#
#         "versions": [
#             {
#                 'info': {
#                     'version_number': 0,
#                     'pip_command': '',
#                     'freeze': '',
#                     'list': '',
#                     'date_and_time_added': ''
#                 },
#
#                 'auth': {
#                     'hash': '',
#                     'signature': '',
#                     'address': ''
#                 }
#             }
#         ],
#     }
# ],
#
# 'admin_auth': {
#     'hash': [],
#     'signature': [],
# },
#
#
#
#
#
#
#
#


















# import hashlib
# import random
#
# nbl_zeros = number_of_leading_zeros = 6
# control_number = str(hex(random.getrandbits(512)))
#
# while(True):
#
#     hash = hashlib.sha3_512(control_number.encode('utf-8')).hexdigest()
#     counter += 1
#
#     if nbl_zeros == 0:
#         print(hash)
#         break
#
#     if int(hash[:nbl_zeros], 16) == 0 :
#
#         print('0x' + hash)
#         break
#
#     else:
#         control_number = str(hex(random.getrandbits(128)))
#         # print(int(control_number, 0))
#
# print(counter)
# print(control_number)
# print(len(control_number))
#

# "new_requests": [
#     {
#         'data' : {
#             'user_name':'',
#             'user_public_key':'',
#             "total_requests" : '',
#             "request": {},
#             "request_message": '',
#             "date_and_time_of_request": '',
#         },
#         'auth' : {
#             'new_requests_hash': [],
#             'new_requests_signature': [],
#         }
#     }
# ]
# }

# import sys
#
# public_address = str(sys.argv[1])
#
# # print(public_address)
#
# data , hash = decode_fox_public_address(public_address)
# print(data)
#
# ans = verify_signature(data['info']['public_key'],
#     data['info_signature'], data['info_hash']
#     )
# print(ans)
# def insert_lines_in_file(file_path, list_of_lines, count_list):
#
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#
#     line_list = []
#     index = 0
#     prev_count = None
#     added_lines = 0
#
#     for count in count_list:
#         line_num = count + added_lines - 1
#         lines.insert(line_num, f"{list_of_lines[index]}\n")
#         added_lines = added_lines + 1
#         index = index + 1
#
#     with open(file_path, 'w') as file:
#         file.writelines(lines)
#
# path = fox_info.executable_python()
# path = path.split('\\')[-1]
# print(path)
#
# file_path = r'D:\Fox_Python\fox_scripts\fox_env.bat'
#
# list_of_lines = [f'''    call set "PROMPT=%%PROMPT:%farg%=({path})%%"''', f'''    call set "PROMPT=%%PROMPT:%farg%=({path})%%"'''
# ]
#
# count_list = [7,21]
#
# insert_lines_in_file(file_path, list_of_lines, count_list)




# a,b,c,d = fox_map.cmp_map('env_1')
#
# print(a)
# print('----------------------------------------------------------------')
# print(b)
#
# pck_info=[]
# pcks=[]
# pck_names=[]
# scripts = []
#
# site_packages=r''
#
# for i in a['site-packages']:
#     if i.endswith('.dist-info'):
#         pck_info.append(i)
#         pck = i.split('-')
#         pck_with_ver = pck[0] + '==' + pck[1].replace('.dist','')
#         pcks.append(pck_with_ver)
#
# for i in pck_info:
#
#     try:
#         i_folder = os.path.join(site_packages, i)
#         top_level = os.path.join(i_folder, 'top_level.txt')
#         with open(top_level, 'r') as file:
#             name = file.read().rstrip()
#         pck_names.append(name)
#     except FileNotFoundError:
#         pass
#     try:
#         entry_points = os.path.join(i_folder, 'entry_points.txt')
#         with open(entry_points, 'r') as file:
#             lines = [line.rstrip() for line in file]
#             if lines[0] == '[console_scripts]':
#                 script = lines[1].split(' ')[0]
#                 scripts.append(script)
#             else:
#                 raise FileNotFoundError('error raised in else loop')
#     except FileNotFoundError:
#         pass
#
# print(pck_names)
# print(scripts)
