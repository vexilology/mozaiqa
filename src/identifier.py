import config

class Identifier:
    def __init__(self, i):
        self.ident = i

    def md4(hash, alg_name):
        t_hash = "a2acde400e61410e79dacbdfc3413151"
        if len(hash) == len(t_hash) and hash.isalpha(
            ) == False and hash.isalnum() == True:
            alg_name.append("106040")

    def md5(hash, alg_name):
        t_hash = "ae11fd697ec92c7c98de3fac23aba525"
        if len(hash) == len(t_hash) and hash.isalpha(
            ) == False and hash.isalnum() == True:
            alg_name.append("106080")

    def sha1(hash, alg_name):
        t_hash = "4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333"
        if len(hash) == len(t_hash) and hash.isalpha(
            ) == False and hash.isalnum() == True:
            alg_name.append("109020")

    def sha224(hash, alg_name):
        t_hash = "e301f414993d5ec2bd1d780688d37fe41512f8b57f6923d054ef8e59"
        if len(hash) == len(t_hash) and hash.isalpha(
            ) == False and hash.isalnum() == True:
            alg_name.append("114020")

    def sha256(hash, alg_name):
        t_hash = "2c740d20dab7f14ec30510a11f8fd78b82bc3a711abe8a993acdb323e78e6d5e"
        if len(hash) == len(t_hash) and hash.isalpha(
            ) == False and hash.isalnum() == True:
            alg_name.append("115020")

    def sha384(hash, alg_name):
        t_hash = "3b21c44f8d830fa55ee9328a7713c6aad548fe6d7a4a438723a0da67c48c485220081a2fbc3e8c17fd9bd65f8d4b4e6b"
        if len(hash) == len(t_hash) and hash.isalpha(
            ) == False and hash.isalnum() == True:
            alg_name.append("119040")

    def sha512(hash, alg_name):
        t_hash = "ea8e6f0935b34e2e6573b89c0856c81b831ef2cadfdee9f44eb9aa0955155ba5e8dd97f85c73f030666846773c91404fb0e12fb38936c56f8cf38a33ac89a24e"
        if len(hash) == len(t_hash) and hash.isalpha(
            ) == False and hash.isalnum() == True:
            alg_name.append("122060")

    def ripemd160(hash, alg_name):
        t_hash = "dc65552812c66997ea7320ddfb51f5625d74721b"
        if len(hash) == len(t_hash) and hash.isalpha(
            ) == False and hash.isalnum() == True:
            alg_name.append("109120")

    def blake2s256(hash, alg_name):
        t_hash = "6665ec809bc89daf21ec9e77ebac6b817e49673cf7db2bbede072564f84b46d9"
        if len(hash) == len(t_hash) and hash.isalpha(
            ) == False and hash.isalnum() == True:
            alg_name.append("112055")

    def blake2b512(hash, alg_name):
        t_hash = "91850ff29412930625ef0723731914104fc9b3b84b62c5e42f43390d8c09fef3618b42f03dfb2e9b9f08b32a5037b00f4c2728bdfa5bb737de56fadc2cbba4be"
        if len(hash) == len(t_hash) and hash.isalpha(
            ) == False and hash.isalnum() == True:
            alg_name.append("112056")

    def timetofound(self):
        alg_name = []
        h_name = self.ident

        Identifier.md4(h_name, alg_name); Identifier.md5(h_name, alg_name);
        Identifier.sha1(h_name, alg_name); Identifier.sha224(h_name, alg_name);
        Identifier.sha256(h_name, alg_name); Identifier.sha384(h_name, alg_name);
        Identifier.sha512(h_name, alg_name); Identifier.ripemd160(h_name, alg_name);
        Identifier.blake2s256(h_name, alg_name); Identifier.blake2b512(h_name, alg_name)

        if len(alg_name) == 0:
            print("[x] Not found.")
            exit(0)
        elif len(alg_name) > 2:
            alg_name.sort()
            print("~" * 50)
            print("[?] -> " + str(config.id_algorithms[alg_name[0]]))
            print("[?] -> " + str(config.id_algorithms[alg_name[1]]))
            print("\nLeast Possible:")
            for a in range(int(len(alg_name)) - 2):
                print("[?] " + str(config.id_algorithms[alg_name[a + 2]]))
        else:
            alg_name.sort()
            print("~" * 50)
            for a in range(len(alg_name)):
                print("[?] -> " + str(config.id_algorithms[alg_name[a]]))
