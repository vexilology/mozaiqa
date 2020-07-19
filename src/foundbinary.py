import base64

class FoundBinary:
    def __init__(self, myfile, a, m):
        self.myfile = myfile
        self.addhash = m
        self.myhash = a

    def base32_64(self):
        if self.myhash == "base32":
            e_bytes = self.addhash.encode("utf-8")
            d_bytes = base64.b32decode(e_bytes)
            check_pass = d_bytes.decode("utf-8")
            print("-" * 20)
            print("[!] Password found ---> {}".format(check_pass))
            print("-" * 20)

        elif self.myhash == "base64":
            e_bytes = self.addhash.encode("utf-8")
            d_bytes = base64.b64decode(e_bytes)
            check_pass = d_bytes.decode("utf-8")
            print("-" * 20)
            print("[!] Password found ---> {}".format(check_pass))
            print("-" * 20)

        elif self.myhash == "ascii85":
            e_bytes = self.addhash.encode("utf-8")
            d_bytes = base64.a85decode(e_bytes)
            check_pass = d_bytes.decode("utf-8")
            print("-" * 20)
            print("[!] Password found ---> {}".format(check_pass))
            print("-" * 20)
