import httpimport

url = "https://raw.githubusercontent.com/boconnor2017/hesiod/main/python/"

with httpimport.remote_repo(url):
  import lib_general as heslibgen

print(heslibgen.hello_world())