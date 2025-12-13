print("sinh vien : bui hin xu")

print("ma so sv :245751030110041")

print("#############################")
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ" # Corrected from "NO" in the image
aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())

