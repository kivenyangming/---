class GetName():
    def __init__(self):
        self.FaceName0 = "查无此人"
        self.FaceName1 = "zhang"
        self.FaceName2 = "li"
        self.FaceName3 = "hong"
        self.FaceName4 = "peng"

    def ImgName2FaceName(self, ImgName):
        DictFace = {
            None  :self.FaceName0,
            '1.jpg': self.FaceName1,
            '2.jpg': self.FaceName2,
            '3.jpg': self.FaceName3,
            '4.jpg': self.FaceName4,
        }
        return DictFace[ImgName]

