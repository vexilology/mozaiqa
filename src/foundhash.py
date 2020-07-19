import config
import hashlib
from hashlib import blake2s, blake2b

class FoundHash:
    def __init__(self, myfile, a, m):
        self.myfile = myfile
        self.addhash = m
        self.myhash = a

    def md4(self):
        if self.myhash == "md4":
            for password in self.myfile:
                check_pass = hashlib.new("md4", (
                    password.strip().encode())).hexdigest()
                print("[?] Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!] Password found ---> {}".format(password))
                    print("-" * 20)
                    exit(0)
                else:
                    continue
            return print("[x] Hash not found ---> {}".format(self.addhash))

    def md5(self):
        if self.myhash == "md5":
            for password in self.myfile:
                check_pass = hashlib.md5(password.strip().encode()).hexdigest()
                print("[?] Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!] Password found ---> {}".format(password))
                    print("-" * 20)
                    exit(0)
                else:
                    continue
            return print("[x] Hash not found ---> {}".format(self.addhash))

    def sha_full(self):
        if self.myhash == "sha1":
            for password in self.myfile:
                check_pass = hashlib.sha1(password.strip().encode()).hexdigest()
                print("[?] Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!] Password found ---> {}".format(password))
                    print("-" * 20)
                    exit(0)
                else:
                    continue
            return print("[x] Hash not found ---> {}".format(self.addhash))

        elif self.myhash == "sha224":
            for password in self.myfile:
                check_pass = hashlib.sha224(password.strip().encode()).hexdigest()
                print("[?] Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!] Password found ---> {}".format(password))
                    print("-" * 20)
                    exit(0)
                else:
                    continue
            return print("[x] Hash not found ---> {}".format(self.addhash))

        elif self.myhash == "sha256":
            for password in self.myfile:
                check_pass = hashlib.sha256(password.strip().encode()).hexdigest()
                print("[?] Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!] Password found ---> {}".format(password))
                    print("-" * 20)
                    exit(0)
                else:
                    continue
            return print("[x] Hash not found ---> {}".format(self.addhash))

        elif self.myhash == "sha384":
            for password in self.myfile:
                check_pass = hashlib.sha384(password.strip().encode()).hexdigest()
                print("[?] Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!] Password found ---> {}".format(password))
                    print("-" * 20)
                    exit(0)
                else:
                    continue
            return print("[x] Hash not found ---> {}".format(self.addhash))

        elif self.myhash == "sha512":
            for password in self.myfile:
                check_pass = hashlib.sha512(password.strip().encode()).hexdigest()
                print("[?] Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!] Password found ---> {}".format(password))
                    print("-" * 20)
                    exit(0)
                else:
                    continue
            return print("[x] Hash not found ---> {}".format(self.addhash))

    def ripemd160(self):
        if self.myhash == "ripemd160":
            for password in self.myfile:
                check_pass = hashlib.new("ripemd160",
                        (password.strip().encode())).hexdigest()
                print("[?] Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!] Password found ---> {}".format(password))
                    print("-" * 20)
                    exit(0)
                else:
                    continue
            return print("[x] Hash not found ---> {}".format(self.addhash))

    def blake2(self):
        if self.myhash == "blake2s-256":
            for password in self.myfile:
                check_pass = blake2s(password.strip().encode()).hexdigest()
                print("[?] Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!] Password found ---> {}".format(password))
                    print("-" * 20)
                    exit(0)
                else:
                    continue
            return print("[x] Hash not found ---> {}".format(self.addhash))

        elif self.myhash == "blake2b-512":
            for password in self.myfile:
                check_pass = blake2b(password.strip().encode()).hexdigest()
                print("[?] Password ---> {}".format(password.strip()))
                if check_pass == self.addhash:
                    print("-" * 20)
                    print("\n[!] Password found ---> {}".format(password))
                    print("-" * 20)
                    exit(0)
                else:
                    continue
            return print("[x] Hash not found ---> {}".format(self.addhash))
