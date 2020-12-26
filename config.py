_list = [
    #_list[0] mozaiqa.py
    "============== mozaiqa ==============",
    #_list[1] mozaiqa.py
    "./mozaiqa.py [-test] [-h] [-m] [-a] [-s] [-f] [-i]",
    #_list[2] src/passwordinfo.py
    "/usr/share/dict/words",
    #_list[3] mozaiqa.py
    "md2, md4, md5, \
    sha1, sha224, sha256, sha384, sha512, ripemd160,\
    blake2s-256, blake2b-512, \
    sha3-224, sha3-256, sha3-384, sha3-512, \
    shake128-224, shake128-256, shake128-384, shake128-512, \
    shake256-224, shake256-256, shake256-384, shake256-512, \
    base32, base64, ascii85."
]


def __open():
    try:
        myfile = open("rockyou.txt", "r",
            encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        print("-"*50)
        print("Error: txt file not found, check folder.")
        print("-"*50)
        exit(1)
    return myfile
