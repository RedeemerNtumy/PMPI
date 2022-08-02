import sys
import subprocess
username = "Red" 
username=username.lower()
password="Word"
try:
    subprocess.run(['useradd', '-p', password, username ])      
except:
    print(f"Failed to add user.")                     
    sys.exit(1)