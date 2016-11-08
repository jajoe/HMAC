if [ $1 = "sha1" ]
then
  echo -n $2 | openssl dgst -sha1 -hmac $3
elif [ $1 = "sha2" ]
then
  echo -n $2 | openssl dgst -sha224 -hmac $3
elif [ $1 = "sha3" ]
then
  echo -n $2 | openssl dgst -sha512 -hmac $3
elif [ $1 = "md5" ]
then
  echo -n $2 | openssl dgst -md5 -hmac $3
else
  echo "Format inconnu"
fi
