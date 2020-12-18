import json


try:
    with open("hash_examples.json") as hash_exmp, open(
              "id_algorithms.json") as id_alg:
        parse_hash = json.load(hash_exmp)
        parse_id = json.load(id_alg)
except:
    print("Can't open json.")
    exit(1)

class Identifier:
    def __init__(self, i):
        self.ident = i

    def md4(hash, a_name):
        t_hash = parse_hash["md4"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("1")

    def md5(hash, a_name):
        t_hash = parse_hash["md5"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("2")

    def sha1(hash, a_name):
        t_hash = parse_hash["sha1"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("3")

    def sha224(hash, a_name):
        t_hash = parse_hash["sha224"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("4")

    def sha256(hash, a_name):
        t_hash = parse_hash["sha256"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("5")

    def sha384(hash, a_name):
        t_hash = parse_hash["sha384"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("6")

    def sha512(hash, a_name):
        t_hash = parse_hash["sha512"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("7")

    def ripemd160(hash, a_name):
        t_hash = parse_hash["ripemd160"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("8")

    def blake2s256(hash, a_name):
        t_hash = parse_hash["blake2s"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("9")

    def blake2b512(hash, a_name):
        t_hash = parse_hash["blake2b"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("10")

    def sha3_224(hash, a_name):
        t_hash = parse_hash["sha3_224"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("11")

    def sha3_256(hash, a_name):
        t_hash = parse_hash["sha3_256"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("12")

    def sha3_384(hash, a_name):
        t_hash = parse_hash["sha3_384"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("13")

    def sha3_512(hash, a_name):
        t_hash = parse_hash["sha3_512"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("14")

    def shake128_224(hash, a_name):
        t_hash = parse_hash["shake128_224"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("15")

    def shake128_256(hash, a_name):
        t_hash = parse_hash["shake128_256"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("16")

    def shake128_384(hash, a_name):
        t_hash = parse_hash["shake128_384"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == false and hash.isalnum() == true:
            a_name.append("17")

    def shake128_512(hash, a_name):
        t_hash = parse_hash["shake128_512"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("18")

    def shake256_224(hash, a_name):
        t_hash = parse_hash["shake256_224"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("19")

    def shake256_256(hash, a_name):
        t_hash = parse_hash["shake256_256"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("20")

    def shake256_384(hash, a_name):
        t_hash = parse_hash["shake256_384"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == false and hash.isalnum() == true:
            a_name.append("21")

    def shake256_512(hash, a_name):
        t_hash = parse_hash["shake256_512"]
        if len(hash) == len(t_hash) and hash.isalpha(
                ) == False and hash.isalnum() == True:
            a_name.append("22")

    def timetofound(self):
        a_name = []
        h_name = self.ident

        Identifier.md4(h_name, a_name)
        Identifier.md5(h_name, a_name)
        Identifier.sha1(h_name, a_name)
        Identifier.sha224(h_name, a_name)
        Identifier.sha256(h_name, a_name)
        Identifier.sha384(h_name, a_name)
        Identifier.sha512(h_name, a_name)
        Identifier.ripemd160(h_name, a_name)
        Identifier.blake2s256(h_name, a_name)
        Identifier.blake2b512(h_name, a_name)
        Identifier.sha3_224(h_name, a_name)
        Identifier.sha3_256(h_name, a_name)
        Identifier.sha3_384(h_name, a_name)
        Identifier.sha3_512(h_name, a_name)
        Identifier.shake128_224(h_name, a_name)
        Identifier.shake128_256(h_name, a_name)
        Identifier.shake128_384(h_name, a_name)
        Identifier.shake128_512(h_name, a_name)
        Identifier.shake256_224(h_name, a_name)
        Identifier.shake256_256(h_name, a_name)
        Identifier.shake256_384(h_name, a_name)
        Identifier.shake256_512(h_name, a_name)

        if len(a_name) == 0:
            print("[x] Not found.")
            exit(0)
        elif len(a_name) > 4:
            a_name.sort()
            print("[?] :: " + str(parse_id[a_name[0]]))
            print("[?] :: " + str(parse_id[a_name[1]]))
            print("[?] :: " + str(parse_id[a_name[2]]))
            print("[?] :: " + str(parse_id[a_name[3]]))
            print("Least Possible:")
            for a in range(int(len(a_name))-4):
                print("[?] :: " + str(parse_id[a_name[a+4]]))
        else:
            a_name.sort()
            for a in range(len(a_name)):
                print("[?] :: " + str(parse_id[a_name[a]]))
