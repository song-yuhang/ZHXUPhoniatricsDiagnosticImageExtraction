"""
读取 img 中的所有图片，进行检测，取得结果放入 result。
结果包含： 
    -声带闭合模式
    -声门上代偿情况
    -声带垂直水平面比较
    -杓状关节运动情况
"""
from cnocr import CnOcr



img_fp = './img/example.png'
ocr = CnOcr()  # 所有参数都使用默认值
out = ocr.ocr(img_fp)
print(out)
