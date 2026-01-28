import json

def get_users() -> dict:
  with open("db/users.json", 'r') as f:
    users = json.load(f)
  return users

def get_login(user: str, pw: bytes) -> bool:
  users = get_users()
  
  data = users[user]
  salt = data["salt"]
  pwdh = data["hash"]
  if password.hash(password.salt(pw, salt)) == pwdh:
    return True
  return False
  

