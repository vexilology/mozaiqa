import zipfile

class RipArchive:
    def __init__(self, myfile, f):
        self.myfile = myfile
        self.myarchive = f

    def checkzip(self):
        for password in self.myfile.readlines():
            check_pd = password.strip().encode()
            try:
                with zipfile.ZipFile(self.myarchive) as myzip:
                    myzip.extractall(pwd=check_pd)
                    print("-" * 20)
                    print("[!] Password found! ---> {}".format(check_pd))
                    print("-" * 20)
                    break
            except:
                print("[x] Access denied ---> {}".format(check_pd))
