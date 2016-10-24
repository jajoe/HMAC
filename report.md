# Implementation
Jajoe doit reprendre code open-source de OpenSSL et l'utiliser pour expliquer dans les grandes lignes comment s'implémente l'HMAC (voir référence).

Koisell doit réaliser une GUI pour pouvoir utiliser cette librairie (OpenSSL) pour encrypter en HMAC. Cette GUI devra permettre de rentrer de nombreux paramètres et encryptera un fichier donné en entrée.

# Rapport
## Expliquation de ce qu'on a fait
## Mini-rappel sur le SHA (vraiment SHA) et sa vulnérabilité
## Preuve de résistance et description du principe
* http://security.stackexchange.com/questions/33123/hotp-with-as-hmac-hashing-algoritme-a-hash-from-the-sha-2-family
* http://stackoverflow.com/questions/3334524/hmac-security-is-the-security-of-the-hmac-based-on-sha-1-affected-by-the-colli
* http://www.iet.unipi.it/g.dini/Teaching/sncs/lectures/handouts/03.hash-and-mac.pdf
* http://csrc.nist.gov/groups/STM/cavp/documents/mac/hmacval.html
* http://crypto.stackexchange.com/questions/10140/using-one-way-hash-functions-as-the-encryption-method
* http://security.stackexchange.com/questions/20129/how-and-when-do-i-use-hmac/20301
# Références 
* OpenSSL : https://gist.github.com/tsupo/112188/acdbf002acf454bd60c355a776b9a5b58b6dff5e
