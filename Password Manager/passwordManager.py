import os
import json
import hashlib
import getpass

FILE_NAME="passwords.json"

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()


def load_data():
  if not os.path.exists(FILE_NAME):
    with open(FILE_NAME,'w') as file:
      file.write("{}")
  with open(FILE_NAME,'r') as file:
    data=json.loads(file.read())
    return data


def save_password(website,username,password):
    data=load_data()
    data[website]={"username":username,"password":hash_password(password)}
    with open(FILE_NAME,'w') as file:
      json.dump(data,file,indent=4)

save_password("example2.com","user123","passw0rd!")

def show_data():
  data=load_data()
  for website,credentials in data.items():
    print(f"Website: {website}")
    print(f"Username:{credentials['username']}")
    print(f"Password:{credentials['password']}")

# show_data()

def get_password(website):
  data=load_data()
  if website in data:
    print(hashlib.data[website]['password'])
  else:
    print("Website not found.")
    
get_password("example.com")