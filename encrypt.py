from cryptography.fernet  import Fernet
key= Fernet.generate_key()
cipher = Fernet(key)
username= "user1234".encode()
password = "pass@".encode()
encrypted_username=cipher.encrypt(username)
encrypted_password = cipher.encrypt(password)

print("encrypted_username")
print("encrypted_password")

# decrypted_username = cipher.decrypt(encrypted_username)
# decrypted_password = cipher.decrypt(encrypted_password)
# print (decrypted_username.decode()) 
# print(decrypted_password.decode())           