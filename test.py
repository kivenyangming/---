import os
import cv2
from GetImageName import GetName


class Template():
    def __init__(self):
        # 图像路径
        self.targetPath = "./TargetImg/"  # 模板库图像
        self.ReturnPath = "C:/Users/kiven/Desktop/CO/ReturnImg/"  # 存储识别到的图像
        # 模板名称
        self.method1 = eval('cv2.TM_CCOEFF')  # 系数匹配法
        self.method2 = eval('cv2.TM_CCOEFF_NORMED')  # 相关系数匹配法
        self.method3 = eval('cv2.TM_CCORR')  # 相关匹配法
        self.method4 = eval('cv2.TM_CCORR_NORMED')  # 归一化相关匹配法
        self.method5 = eval('cv2.TM_SQDIFF')  # 平方差匹配法
        self.method6 = eval('cv2.TM_SQDIFF_NORMED')  # 归一化平方差匹配法

    def template(self, img):
        ReturnImg = img.copy()
        TemplLine = os.listdir(self.targetPath)
        ImgName = None
        for TemplImgNames in TemplLine:  # 遍历文件夹下所有的人脸模板
            TemplImg = cv2.imread(self.targetPath + TemplImgNames)  # 读取待测图像
            height, width, Channel = TemplImg.shape
            results = cv2.matchTemplate(ReturnImg, TemplImg, self.method6)  # 进行模板匹配
            # 获取匹配结果中的最小值、最大值、最小值坐标和最大值坐标
            minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(results)  # 获取匹配结果

            ImgThreshold = (minValue + maxValue) / 2  # 获取匹配的阈值=（最小值+最大值）/2

            if ImgThreshold > 0.45:  # 当阈值大于0.45 则进行下面的（ 当修改匹配method 需要修改阈值计算方式）
                resultPoint1 = minLoc
                resultPoint2 = (resultPoint1[0] + width, resultPoint1[1] + height)
                cv2.rectangle(ReturnImg, resultPoint1, resultPoint2, (255, 0, 0), 1)
                ImgName = TemplImgNames

                # # 给图像命名
                # ImgName = str(uuid.uuid1())
                # cv2.imwrite(self.ReturnPath + "%s.jpg" % ImgName, img)

        return ReturnImg, ImgName


if __name__ == '__main__':
    capture = cv2.VideoCapture(0)
    test = Template()
    GetImageName = GetName()
    while True:
        # 读取某一帧
        ref, frame = capture.read()
        frame = cv2.resize(frame, (1920, 980))  #
        # 进行检测
        frame, ImgName = test.template(frame)
        FaceNames = GetImageName.ImgName2FaceName(ImgName)
        # print(FaceNames)
        frame = cv2.putText(frame, "FaceName= %s" % str(FaceNames), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("video", frame)
        c = cv2.waitKey(1) & 0xff
        if c == 27:
            capture.release()
            break
    capture.release()
    cv2.destroyAllWindows()