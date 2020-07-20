from zipfile import ZipFile

class RipArchive:
    def __init__(self, myfile, f):
        self.myfile = myfile
        self.myarchive = f

    def checkzip(self):
        for password in self.myfile.readlines():
            check_pd_encode = password.strip().encode("utf-8")
            check_pd_decode = check_pd_encode.decode("utf-8")
            try:
                with ZipFile(self.myarchive) as myzip:
                    myzip.extractall(pwd=check_pd_encode)
                    print("-" * 20)
                    print("[!] Password found! ---> {}".format(check_pd_decode))
                    print("-" * 20)
                    break
            except:
                print("[x] Access denied ---> {}".format(check_pd_decode))
