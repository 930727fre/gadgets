import os,img2pdf,time,configparser
from PyPDF2 import PdfFileMerger

if(os.path.isfile(os.getcwd()+"/config.ini"))==False:
    print("config.ini doesn't exist.")
else:
    title=input("please enter title for the output files:")
    if (title==""):
        for i in range(len(os.getcwd().split("/"))-1,0,-1):
            if "fakku" in os.getcwd().split("/")[i]:
                title=os.getcwd().split("/")[i]
                break
    print("title:"+title)
    input("press any key to continue or ctrl+c to suspend")
    config = configparser.ConfigParser()
    config.read('config.ini')
    start=time.time()
    counter=0
    num=0
    passed=False
    for root,dirs,files in os.walk(os.getcwd()):
        dirs.sort()
        ls=[]
        foldername=root.split(os.path.sep)[-1]
        if dirs==[]:
            if config["img"][str(num)]=="1":
                counter=counter+1
                print("process:"+str(counter))
                files.sort()
                for i in files:
                    ls.append(os.path.join(root,i))
                print(foldername)
                with open(foldername+".pdf", "wb") as f:
                    f.write(img2pdf.convert([i for i in ls if i.endswith(".png")],compress=True))
            num=num+1
    merger = PdfFileMerger()
    outputpath=os.getcwd()
    ls=[]
    for root,dirs,files in os.walk(outputpath):
        for i in files:
            ls.append(i)
    merge=[]
    for pdf in ls:
        if(".pdf" in pdf and pdf!=title+"_all.pdf"):
            merger.append(pdf)
            merge.append(pdf)
    merger.write(title+"_all.pdf")
    merger.close()
    for j in range(int(len(merge)/10)+1):
        merger = PdfFileMerger()
        for k in range(10):
            index=k+j*10
            if index==len(merge):
                break
            merger.append(merge[index])
        merger.write(title+"_pt."+str(j+1)+".pdf")
        merger.close()
    end=time.time()
    print("it takes "+str(int(end-start))+" seconds to finish the process.")

