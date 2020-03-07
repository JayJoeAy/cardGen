from PIL import Image
for el in range(1,11):
    namebc =  "el"+str(el)+".png"
    for i in range(2,10):
        name = "el"+str(el)+str(i)+".png"
        bc = Image.new("RGB", (240,350),"white")
        border = Image.open("border.png")
        bc.paste(border,(0,0), border)
        # Main Image
        img = Image.open(namebc)
        img = img.resize((120,120))
        imgrev = img.rotate(180)
        bc.paste(img, (70,65), img)
        bc.paste(imgrev, (70,180), imgrev)
        # Number Image
        num = str(i)+".png"
        img2 = Image.open(num)
        img2 = img2.resize((50,50))
        img2rev = img2.rotate(180)
        bc.paste(img2,(10,10), img2)
        bc.paste(img2rev,(180,290), img2rev)
        bc.save("C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/"+name, quality=95)
#%%
A4 = Image.new("RGB", (2480,3580), "white")
imp1 = Image.open("C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/el14.png")
imp2 = Image.open("C:/Users/Erfan/Desktop/Erfan/Dead_mans_draw/hook/el15.png")
A4.paste(imp1,(10,20))
A4.paste(imp2,(250,20))
A4.save("A4.png", quality=95)