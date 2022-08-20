# from io import StringIO
# from operator import sub
# from os import lseek
# from statistics import stdev
# import warnings
# import paramiko
# import subprocess
# import sys


# def ssh_conn(free):
#     global client
#     client=paramiko.SSHClient()
#     client.load_system_host_keys()
#     if free=="no":
#         client.connect("10.14.216.18",username="joshua")
#     else:
#         client.connect("10.14.216.18",username="joshua")
#     client.close()

# # def ssh_conn_copy(ssh_path,file_name):
# #     client=paramiko.SSHClient()
# #     client.load_system_host_keys()
# #     client.connect("10.14.216.18",username="joshua",password="02050")
# #     print("True")
# #     stdin,stdout,stderr=client.exec_command(f"cd .ssh;echo >>id_rsa.pub;ls")
# #     #echo '{words}' >> id_rsa.pub
# #     client.close()
# # def copy_id():
# #     client=paramiko.SSHClient()
# #     client.load_system_host_keys()
# #     start=subprocess.Popen("ssh-copy-id -f joshua@10.14.216.18",stdin=subprocess.PIPE,shell=True)
# #     start.stdin.write(b"02050\n")
# #     stdout,stderr=start.communicate()
    
# #     for i in range(10):
# #         print("yes")
# #     client.close()

# # def generate_key(ssh_path,file_name):
# #     import warnings
# #     with warnings.catch_warnings():
# #         warnings.simplefilter("ignore")
# #         from paramiko import RSAKey
# #     global key
# #     key =RSAKey.generate(2048)
# #     key.write_private_key_file(f'{ssh_path}/{file_name}')
# #     # key.write_private_key_file(f'{ssh_path}/{file_name}')
     
# #     return key

# ssh_conn("no")
# subprocess.Popen("rm -d default",shell=True).communicate()[0]
# subprocess.Popen("mkdir default",shell=True).communicate()[0]
# # generate_key('/home/iamdveloper/.ssh','id_rsa.pub')
# # copy_id()
# # ssh_conn("yes")





