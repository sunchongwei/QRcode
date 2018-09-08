import easygui as eg
import os
from ORtool  import * 
#界面交互
def jiemian():
    #选项列表
    choices=['无背景二维码','中间logo二维码','全背景二维码'] 
    #输入要加入图像的地址
    photo_url="anminal.gif"
    my_choice=eg.buttonbox(msg="功能选项：点击图像更换图像您要选择的图像",title='二维码生成器V1.1',choices=choices,image=photo_url)
    print(my_choice)

    if my_choice==choices[0] :
        #选项一,生成简单二维码
        photo_url=createSimpleQRcode() 
        return True  
    elif my_choice==choices[1] :
        #选项二，生成中间logo的二维码
        createPhotoQRcode()
        return True  
    elif my_choice==choices[2] :
        #选项三,生成带动图的二维码
        createGIFQRcode()
        return True 
    elif my_choice==photo_url :
        #点击图片不做出反应
        return True 
    else :
        print("出现未知错误，程序退出")
        return False


#采用界面的方法打开文件

while jiemian():
    pass
print("程序关闭....")
