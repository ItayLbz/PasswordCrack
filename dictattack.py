import hashlib

pass_found =0

i_hash= input("Enter The Hashed Password: ")
p_doc = input("\n Enter Password Filename Including Path: ")

p_file = open(p_doc,"r")

for word in p_file:
    enc_word = word.encode("utf-8")
    hash_word = hashlib.md5(enc_word.strip())
    digest = hash_word.hexdigest()

    if(digest == i_hash):
        print(f"Password Found: {word}")
        pass_found=1
        break

if not pass_found:
    print("Password Was Not Found")