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

ans=[]
foldernames=[]

for root,dirs,files in os.walk(cwd):
    foldername=root.split(os.path.sep)[-1]
    if dirs==[] and not foldername=="output":
        if len(files)>10:
            files.sort()
            imagedir=os.path.join(root,files[0])
            print(foldername)
            foldernames.append(foldername)
            subprocess.call(["xdg-open", imagedir])
            temp=input("ans:")
            while temp != "1" and temp != "2":
                print("error! please input 1 or 2")
                temp=input("ans:")
            ans.append(temp)
print(ans)
print(foldernames)

temp=0

for i in range(len(foldernames)):
    config["img"][str(temp)]=ans[i]
    temp=temp+1
with open('config.ini', 'w') as f:
    config.write(f)

