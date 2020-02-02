#!/usr/bin/env python3
import hashlib
import sha3
import base64
import argparse
from Crypto.Hash import MD2

OUTPUT32 = 32 # output 256 bits
OUTPUT64 = 64 # output 512 bits

class FoundHash:
    """use: hashlib, sha3, crypto.hash_md2"""

    def __init__(self, myfile, a, m):
        self.myfile = myfile
        self.addhash = a
        self.myhash = m 

    def md2(self):
        if self.myhash == "md2":
            for password in self.myfile:
                check_pass = MD2.new(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

    def md4(self):
        if self.myhash == "md4":
            for password in self.myfile:
                check_pass = hashlib.new('md4', (password.strip().encode())).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

    def md5(self):
        if self.myhash == "md5":
            for password in self.myfile:
                check_pass = hashlib.md5(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

    def sha_full(self):
        if self.myhash == "sha1":
            for password in self.myfile:
                check_pass = hashlib.sha1(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "sha224":
            for password in self.myfile:
                check_pass = hashlib.sha224(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "sha256":
            for password in self.myfile:
                check_pass = hashlib.sha256(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "sha384":
            for password in self.myfile:
                check_pass = hashlib.sha384(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "sha512":
            for password in self.myfile:
                check_pass = hashlib.sha512(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

    def ripemd160(self):
        if self.myhash == "ripemd160":
            for password in self.myfile:
                check_pass = hashlib.new('ripemd160', (password.strip().encode())).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

    def keccak_full(self):
        if self.myhash == "keccak224":
            for password in self.myfile:
                check_pass = sha3.keccak_224(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "keccak256":
            for password in self.myfile:
                check_pass = sha3.keccak_256(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "keccak384":
            for password in self.myfile:
                check_pass = sha3.keccak_384(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "keccak512":
            for password in self.myfile:
                check_pass = sha3.keccak_512(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

    def shake_full(self):
        if self.myhash == "shake128-256":
            for password in self.myfile:
                check_pass = sha3.shake_128(password.strip().encode()).hexdigest(OUTPUT32)
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "shake256-512":
            for password in self.myfile:
                check_pass = sha3.shake_256(password.strip().encode()).hexdigest(OUTPUT64)
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

    def sha3_full(self):
        if self.myhash == "sha3-224":
            for password in self.myfile:
                check_pass = hashlib.sha3_224(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "sha3-256":
            for password in self.myfile:
                check_pass = hashlib.sha3_256(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "sha3-384":
            for password in self.myfile:
                check_pass = hashlib.sha3_384(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

        elif self.myhash == "sha3-512":
            for password in self.myfile:
                check_pass = hashlib.sha3_512(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("=" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("=" * 20)
                    break
            else:
                print("=" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("=" * 20)

class FoundBinary:
    """use: base64"""

    def __init__(self, myfile, a, m):
        self.myfile = myfile
        self.addhash = a
        self.myhash = m

    def base32_64(self):
        if self.myhash == "base32":
            check_pass = base64.b32decode(self.addhash.encode())
            print("=" * 20)
            print("[!]Password found ---> {}".format(check_pass))
            print("=" * 20)

        elif self.myhash == "base64":
            check_pass = base64.b64decode(self.addhash.encode())
            print("=" * 20)
            print("[!]Password found ---> {}".format(check_pass))
            print("=" * 20)

    def ascii85(self):
        if self.myhash == "ascii85":
            check_pass = base64.a85decode(self.addhash.encode())
            print("=" * 20)
            print("[!]Password found ---> {}".format(check_pass))
            print("=" * 20)

def main():
    try:
        myfile = open("rockyou.txt", "r", encoding="utf-8", errors="ignore")
    except:
        print("\nError: txt file not found, check folder.")
        quit()

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=str, help="add hash")
    parser.add_argument("-m", type=str, help="add title function")
    args = parser.parse_args()

    finalH = FoundHash(myfile, args.a, args.m)
    finalB = FoundBinary(myfile, args.a, args.m)

    finalH.md2()
    finalH.md4()
    finalH.md5()
    finalH.sha_full()
    finalH.ripemd160()
    finalH.sha3_full()
    finalH.keccak_full()
    finalH.shake_full()
    finalB.base32_64()
    finalB.ascii85()

if __name__ == "__main__":
    main()
