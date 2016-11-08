import hmac as hmac
import hashlib as hashlib
import sys

if(len(sys.argv) != 4):
  print("Error ! Need 3 arguments : hash function (sha1, sha2, sha3 or md5), msg and key")
else:
  if(sys.argv[1] == "sha1"):
    answer = hmac.new(sys.argv[3], msg=sys.argv[2], digestmod=hashlib.sha1)
  elif(sys.argv[1] == "sha2"):
    answer = hmac.new(sys.argv[3], msg=sys.argv[2], digestmod=hashlib.sha224)
  elif(sys.argv[1] == "sha3"):
    answer = hmac.new(sys.argv[3], msg=sys.argv[2], digestmod=hashlib.sha512)
  elif(sys.argv[1] == "md5"):
    answer = hmac.new(sys.argv[3], msg=sys.argv[2], digestmod=hashlib.md5)
  else:
    print("Hash function error. Hash function = sha1, sha2, sha3 or md5")

  print(answer.hexdigest())
