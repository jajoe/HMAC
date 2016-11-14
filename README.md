# HMAC
Project realized with Koisell to validate the course "Information Theory" with Mme Rogozan.

# Use of the script hmac.sh
Need 3 parameters : the name of the hash function (sha1, sha2, sha3 or md5), the value and the key.

Ex: sh hmac.sh sha3 value key

# Use of the script hmac_script.py

You can test the script by calling it with 3 parameters : the name of the hash function (sha1, sha2, sha3 or md5), the value and the key.

Ex: python hmac_script.py sha3 value key

You can use too the function of this script, which is hmac\_encrypt(f, my\_msg, key) and which return a string.
