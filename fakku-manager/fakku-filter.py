import os,sys,configparser,subprocess


cwd=os.getcwd()
print("cwd:"+cwd)
print()
input("press any key to continue or ctrl+c to suspend")




if(os.path.isfile(cwd+"/config.ini"))==False:
    f=open("config.ini","a")
    f.write("[img]")
    f.close()

config = configparser.ConfigParser()
config.read('config.ini')
ls=config.items("img")
print(len(ls))

ans=[]
foldernames=[]
counter=0
temp=0


def save():
    for i in range(len(foldernames)):
        config["img"][str(temp)]=ans[i]
        temp=temp+1


for root,dirs,files in os.walk(cwd):
    dirs.sort()
    if counter>len(ls):
        foldername=root.split(os.path.sep)[-1]
        if dirs==[]:
            files.sort()
            imagedir=os.path.join(root,files[0])
            print(foldername)
            foldernames.append(foldername)
            subprocess.call(["xdg-open", imagedir])
            temp=input("ans:")
            while temp != "1" and temp != "2":
                print("error! please input 1 or 2")
                temp=input("ans:")
            config["img"][str(counter-1)]=str(temp)
            with open('config.ini', 'w') as f:
                config.write(f)
    counter=counter+1



