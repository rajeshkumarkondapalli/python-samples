from ansible.parsing.vault import VaultLib

password = "my_password"
vault = VaultLib([(None, password)])

# Encrypt data
plaintext = "my sensitive data"
encrypted_data = vault.encrypt(plaintext)

# Decrypt data
decrypted_data = vault.decrypt(encrypted_data)

print(decrypted_data)
