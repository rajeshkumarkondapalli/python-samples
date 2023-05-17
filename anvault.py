# import subprocess
# import os
from ansible_vault import Vault

vault = Vault('password')
data = vault.load(open('file1.yml').read())
print(data)

target_file_name = 'file2.yml'
# open(target_file_name, 'w').close()

my_file = open(target_file_name, 'w')
my_file.write(data)
my_file.close()



# # subprocess.run(["powershell", "pwd"], shell=True)
# # os.system("pwd")

# # os.system('ansible-vault encrypt ' + 'config.yaml')
# ansible-vault encrypt vault.yml --vault-password-file vault_pass.txt
# ansible-vault decrypt vault.yml --vault-password-file vault_pass.txt
