from pathlib import Path
p=Path("C:/Users/mrsha/Downloads/demo1")
p.mkdir(parents=True,exist_ok=True) 
print(p.exists())
print(p.is_dir())
print(p.is_file())

p2=Path("C:/Users/mrsha/Downloads/myLog.log")
p2.write_text("hello this is my log file\nI am writing here")

print("successfully written inside the log file")
print(p2.read_text())


# ✅CHECK IF FILE EXIST
# ✅CHECK FILE OR DIRECTORY
# ✅CREATES DIRECTORIES SAFELY
# ✅CREATES AND WRITES A FILE
# ✅READ FILE
# JOINING PATHS
# LOOP THROUGH FILES
# FILE META DATA
# ABSOLUTE VS RELATIVE PATH
# PATH LIB VS OS

