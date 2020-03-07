from PIL import Image
for el in range(1,11):
    namebc =  "el"+str(el)+".png"
    for i in range(2,10):
        name = "el"+str(el)+str(i)+".png"
        bc = Image.new("RGB", (820,890),"white")
        border = Image.open("border.png")
        bc.paste(border,(0,0), border)
        # Main Image
        img = Image.open(namebc)
        img = img.resize((350,380))
        imgrev = img.rotate(180)
        bc.paste(img, (250,100), img)
        bc.paste(imgrev, (250,450), imgrev)
        # Number Image
        num = str(i)+".png"
        img2 = Image.open(num)
        img2 = img2.resize((150,150))
        img2rev = img2.rotate(180)
        bc.paste(img2,(10,10), img2)
        bc.paste(img2rev,(660,730), img2rev)
        bc.save("C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/"+name, quality=95)
#%%
for j in range(1,11):
    A4name="C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/elementNO"+str(j)+".pdf"
    A4 = Image.new("RGB", (2480,3580), "white")
    size = 20
    elname = 2
    el = 1
    for i in range(5,12,3):
        picname = str(elname)
        add1 = "C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/el"+str(j)+str(i-3)+".png"
        add2 = "C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/el"+str(j)+str(i-2)+".png"
        add3 = "C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/el"+str(j)+str(i-1)+".png"
        if (i==11):
            add1 = "C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/el"+str(j)+str(8)+".png"
            add2 = "C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/el"+str(j)+str(9)+".png"
            add3 = "C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/el"+str(j)+str(2)+".png"
        name = "el"+str(i)
        imp1 = Image.open(add1)
        imp2 = Image.open(add2)
        imp3 = Image.open(add3)
        A4.paste(imp1,(10,size))
        A4.paste(imp2,(830,size))
        A4.paste(imp3,(1650,size))
        size = size+890
    #        i = i + 3
        A4.save(A4name, quality=95)