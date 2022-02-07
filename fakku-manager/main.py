import os,subprocess,platform,img2pdf

operating_system=platform.system()
cwd=os.getcwd()
print("cwd:"+cwd)
input("press any key to continue or ctrl+c to suspend")

while(1):
    compress_ans=input("Compress output files or not?(y/n)")
    if compress_ans =="y" or compress_ans == "n":
        break
    else:
	print("please input y or n.")

ans=[]
counter=0
temp=0


def open_image(imagedir):
    if operating_system=="Linux":
        subprocess.call(["xdg-open", imagedir])
    elif operating_system=="Windows":
        os.startfile(imagedir)

for root,dirs,files in os.walk(cwd):
    dirs.sort()
    foldername=root.split(os.path.sep)[-1]
    if dirs==[]:
        files.sort()
        imagedir=os.path.join(root,files[0])
        print(foldername)
        open_image(imagedir)

        temp=input("ans:")
        while temp != "1" and temp != "2":
            print("error! please input 1 or 2")
            open_image(imagedir)
            temp=input("ans:")
        ans.append([temp,root])
        counter=counter+1


#manager.py
if operating_system=="Windows":
    temp="\\"
elif operating_system=="Linux":
    temp="/"

for i in range(len(os.getcwd().split(temp))-1,0,-1):
    if "fakku" in os.getcwd().split(temp)[i]:
        title=os.getcwd().split(temp)[i]
        title.replace(" ","_")
        break
    
counter=0
num=0
passed=False
ls=[]
for root,dirs,files in os.walk(os.getcwd()):
    dirs.sort()
    foldername=root.split(os.path.sep)[-1]
    if dirs==[]:
        if ans[num][0]=="1":
            counter=counter+1
            print("process:"+str(counter))
            files.sort()
            for i in files:
                ls.append(os.path.join(root,i))
        num=num+1

with open(title+".pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in ls if i.endswith(".png")],compress=True))        

print("Merger finished.")

if compress_and == "y":
    compression_cmd='gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4  -dPDFSETTINGS="default" -dNOPAUSE -dQUIET -dBATCH -sOutputFile=./'+title+"_compressed.pdf"+" "+title+".pdf"
    os.system(compression_cmd)
    os.remove(title+".pdf")
    print("Compression finished.")
print("Process ends.")
