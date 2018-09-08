import qrcode  
from MyQR import myqr
import easygui as eg 
from PIL import Image 
import os 
#该模块主要完成二维码的相关操作功能

#保存照片
def saveImge(img) :
    #展示二维码
    img.show() 
    #选择保存路径,默认为当前路径
    save_path=eg.filesavebox(msg="保存路径",title="保存文件",default=".")
    img.save(save_path)
    return save_path

#输入信息
def inputMessage():
     message=eg.textbox(msg="输入要生成的信息",title="输入")
     return message 

#选择文件地址
def choiceFilePath():
    filepath=eg.fileopenbox(msg="选择要作为背景的图片",title="打开文件",default="C:/")
    return filepath 

#生成简单二维码
def createSimpleQRcode() :
    message=inputMessage()
    img=qrcode.make(message) 
    return saveImge(img)


#生成中间能够显示图片的二维码
def createPhotoQRcode() :
    message=inputMessage() 
    filepath=choiceFilePath() 
    #生成图片二维码
    qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=2)
    qr.add_data(message) 
    qr.make(fit=True) 
    img=qr.make_image() 
    img=img.convert('RGB') 
    icon = Image.open(filepath)

    img_w,img_h = img.size #获得二维码的尺寸
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor) #1/4 size
    icon_w,icon_h = icon.size
    if icon_w >size_w:#若果图像的尺寸大的话，缩小图片
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)

    w = int((img_w - icon_w)/2)
    h = int((img_h - icon_h)/2)
    icon = icon.convert("RGBA")
    img.paste(icon,(w,h),icon)
    #保存二维码
    saveImge(img)

#制造能够生成动图的二维码
def createGIFQRcode() :
    message=inputMessage()
    filename=choiceFilePath() 
    save_path=eg.filesavebox(msg="保存路径",title="保存文件",default=".")
    #分解路径
    save_dir,save_filename=os.path.split(save_path) 
    version, level, qr_name = myqr.run( words=message, # 不支持中文，支持 0~9,a~z, A~Z 以及常见的常用英文标点符号和空格 
                                       picture=filename,
                                       version=2, # 版本，从 1至 40 level='H', # 纠错等级，范围是L、M、Q、H，从左到右依次升高 picture='4e.jpg', # 文件要放在目录下 
                                       colorized=True, # True 为彩色，False 为黑白 
                                       contrast=1.0, # 对比度 
                                       brightness=1.0, # 亮度 
                                       save_name=save_filename, # 命名随便都行，格式可以是 
                                       save_dir=save_dir # 路径要存在
                                      )

