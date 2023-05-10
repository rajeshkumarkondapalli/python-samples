from ansible.parsing.vault import VaultLib
# import subprocess
# import os

password = "my_password"
vault = VaultLib([(None, password)])

# Encrypt data
plaintext = "my sensitive data"
encrypted_data = vault.encrypt(plaintext)

# Decrypt data
decrypted_data = vault.decrypt(encrypted_data)

print(decrypted_data)



# # subprocess.run(["powershell", "pwd"], shell=True)
# # os.system("pwd")

# # os.system('ansible-vault encrypt ' + 'config.yaml')
# ansible-vault encrypt vault.yml --vault-password-file vault_pass.txt
# ansible-vault decrypt vault.yml --vault-password-file vault_pass.txt
