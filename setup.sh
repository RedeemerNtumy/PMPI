# #!/bin/bash
# read -p 'Server username: ' uservar
# read -sp 'Password: ' pwvar
# for server in `cat list_of_servers`; do
#     sshpass -p "${pwvar}" ssh-copy-id -i ~/.ssh/id_rsa.pub -o StrictHostKeyChecking=no "${uservar}@${server}"
# done