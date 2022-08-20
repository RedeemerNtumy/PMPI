### To install packages for the server PC,run this
`xargs -a server_requirements.txt sudo apt-get install`

### To install packages for the client PC,run this
`xargs -a client_requirements.txt sudo apt-get install`

#### Before you run the program, make sure that you have a passwordless login

##### Log in the server PC with the code below and input the recquired password
`ssh username@ip_address` where `username` is the username of the server pc and `ip_address` is the ip address of the server pc
Exit from the server PC and navigate to the ssh folder on the client PC

##### To move to the ssh folder,run the command below
`cd .ssh`

##### You can generate an ssh key with either commands
`ssh-keygen -t rsa` or `ssh-keygen -t dsa`

##### Finally run the command below to allow the passwordless login
`ssh-copy-id username@ip_address`


### To run the program,run this
`sudo python3 Home.py`

<br>
This is very important since we need to give the program admin access to perform succesfully
