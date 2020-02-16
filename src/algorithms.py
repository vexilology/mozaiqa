import sys
import hashlib
import sha3
import base64
import config
from Crypto.Hash import MD2

class FoundHash:
    """use: hashlib, sha3, crypto.hash md2"""

    def __init__(self, myfile, a, m):
        self.myfile = myfile
        self.addhash = m
        self.myhash = a

    def md2(self):
        if self.myhash == "md2":
            for password in self.myfile:
                check_pass = MD2.new(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

    def md4(self):
        if self.myhash == "md4":
            for password in self.myfile:
                check_pass = hashlib.new('md4', (password.strip().encode())).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

    def md5(self):
        if self.myhash == "md5":
            for password in self.myfile:
                check_pass = hashlib.md5(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

    def sha_full(self):
        if self.myhash == "sha1":
            for password in self.myfile:
                check_pass = hashlib.sha1(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "sha224":
            for password in self.myfile:
                check_pass = hashlib.sha224(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "sha256":
            for password in self.myfile:
                check_pass = hashlib.sha256(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "sha384":
            for password in self.myfile:
                check_pass = hashlib.sha384(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "sha512":
            for password in self.myfile:
                check_pass = hashlib.sha512(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

    def ripemd160(self):
        if self.myhash == "ripemd160":
            for password in self.myfile:
                check_pass = hashlib.new('ripemd160', (password.strip().encode())).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

    def keccak_full(self):
        if self.myhash == "keccak224":
            for password in self.myfile:
                if sys.version_info < (3, 6, 8):
                    sys.stderr.write("\033[31m[!]You need python3.6.9+" \
                            "or later to run this script.\n")
                    quit()
                check_pass = sha3.keccak_224(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "keccak256":
            for password in self.myfile:
                if sys.version_info < (3, 6, 8):
                    sys.stderr.write("\033[31m[!]You need python3.6.9+" \
                            "or later to run this script.\n")
                    quit()
                check_pass = sha3.keccak_256(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "keccak384":
            for password in self.myfile:
                if sys.version_info < (3, 6, 8):
                    sys.stderr.write("\033[31m[!]You need python3.6.9+" \
                            "or later to run this script.\n")
                    quit()
                check_pass = sha3.keccak_384(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "keccak512":
            for password in self.myfile:
                if sys.version_info < (3, 6, 8):
                    sys.stderr.write("\033[31m[!]You need python3.6.9+" \
                            "or later to run this script.\n")
                    quit()
                check_pass = sha3.keccak_512(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

    def shake_full(self):
        if self.myhash == "shake128-256":
            for password in self.myfile:
                if sys.version_info < (3, 6, 8):
                    sys.stderr.write("\033[31m[!]You need python3.6.9+" \
                            "or later to run this script.\n")
                    quit()
                check_pass = sha3.shake_128(password.strip().encode()).hexdigest(config.OUTPUT32)
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "shake256-512":
            for password in self.myfile:
                if sys.version_info < (3, 6, 8):
                    sys.stderr.write("\033[31m[!]You need python3.6.9+" \
                            "or later to run this script.\n")
                    quit()
                check_pass = sha3.shake_256(password.strip().encode()).hexdigest(config.OUTPUT64)
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

    def sha3_full(self):
        if self.myhash == "sha3-224":
            for password in self.myfile:
                if sys.version_info < (3, 6, 8):
                    sys.stderr.write("\033[31m[!]You need python3.6.9+" \
                            "or later to run this script.\n")
                    quit()
                check_pass = hashlib.sha3_224(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "sha3-256":
            for password in self.myfile:
                if sys.version_info < (3, 6, 8):
                    sys.stderr.write("\033[31m[!]You need python3.6.9+" \
                            "or later to run this script.\n")
                    quit()
                check_pass = hashlib.sha3_256(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "sha3-384":
            for password in self.myfile:
                if sys.version_info < (3, 6, 8):
                    sys.stderr.write("\033[31m[!]You need python3.6.9+ " \
                            "or later to run this script.\n")
                    quit()
                check_pass = hashlib.sha3_384(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

        elif self.myhash == "sha3-512":
            for password in self.myfile:
                if sys.version_info < (3, 6, 8):
                    sys.stderr.write("\033[31m[!]You need python3.6.9+" \
                            "or later to run this script.\n")
                    quit()
                check_pass = hashlib.sha3_512(password.strip().encode()).hexdigest()
                print("Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!]Password found ---> {}".format(password))
                    print("-" * 20)
                    quit()
            else:
                print("-" * 20)
                print("[!]Hash not found ---x {}".format(self.addhash))
                print("-" * 20)
                quit()

class FoundBinary:
    """use: base64"""

    def __init__(self, myfile, a, m):
        self.myfile = myfile
        self.addhash = m
        self.myhash = a

    def base32_64(self):
        if self.myhash == "base32":
            check_pass = base64.b32decode(self.addhash.encode())
            print("-" * 20)
            print("[!]Password found ---> {}".format(check_pass))
            print("-" * 20)
            quit()

        elif self.myhash == "base64":
            check_pass = base64.b64decode(self.addhash.encode())
            print("-" * 20)
            print("[!]Password found ---> {}".format(check_pass))
            print("-" * 20)
            quit()

    def ascii85(self):
        if self.myhash == "ascii85":
            check_pass = base64.a85decode(self.addhash.encode())
            print("-" * 20)
            print("[!]Password found ---> {}".format(check_pass))
            print("-" * 20)
            quit()
