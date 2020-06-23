import os
files =os.listdir()
files.remove("file.py")


def createIfNotExist(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def Move(folder_name,files):
    for file in files:

        os.replace(file, f"{folder_name}/{file}")


createIfNotExist('Images')
createIfNotExist('Documents')
createIfNotExist('Medias')
createIfNotExist('others')
createIfNotExist('Programs')

imgExts =[".png",".jpg",".jpeg"]
Images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docsExts =[".pdf",".pptx",".docx","doc","txt"]
Documents = [file for file in files if os.path.splitext(file)[1].lower() in docsExts]

mediaExts =[".mp4",".mp3",".flv"]
Medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

programExts =[".php",".c"]
Programs = [file for file in files if os.path.splitext(file)[1].lower() in programExts]


others=[]
for file in files:
    ext =os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in imgExts) and (ext not in docsExts) and (ext not in programExts) and os.path.isfile(file):
        others.append(file)


Move("Medias", Medias)
Move("Images", Images)
Move("Documents", Documents)
Move("others",others)
Move("Programs", Programs)
