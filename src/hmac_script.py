#!/usr/bin/env python3
# coding: utf-8

import hmac as hmac
import hashlib as hashlib
import sys


def hmac_encrypt(f, my_msg, key):
    my_msg = my_msg.encode('utf-8')
    key = str.encode(key)
    if(f == "sha1"):
        answer = hmac.new(key, msg=my_msg, digestmod=hashlib.sha1)
    elif(f == "sha224"):
        answer = hmac.new(key, msg=my_msg, digestmod=hashlib.sha224)
    elif(f == "sha512"):
        answer = hmac.new(key, msg=my_msg, digestmod=hashlib.sha512)
    elif(f == "md5"):
        answer = hmac.new(key, msg=my_msg, digestmod=hashlib.md5)
    else:
        return "Hash function error."

    return answer.hexdigest()


if __name__ == "__main__":
    if(len(sys.argv) != 4):
        print("Error ! Need 3 arguments : hash function (sha1, sha224, sha512 or md5), msg and key")
    else:
        print(hmac_encrypt(sys.argv[1], sys.argv[2], sys.argv[3]))
