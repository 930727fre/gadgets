import os
import img2pdf
import time
from PyPDF2 import PdfFileMerger



print("cwd:"+os.getcwd())
input("press any key to continue or ctrl+c to suspend")
title=input("please enter title for the output files:")

if title=="auto":
    print
    for i in range(len(os.getcwd().split("/"))):
        if "fakku" in os.getcwd().split("/")[i]:
            title=os.getcwd().split("/")[i]
            break

    
start=time.time()

counter=0

if not os.path.exists(os.getcwd()+"/output"):
    os.mkdir("output")
    
for root,dirs,files in os.walk(os.getcwd()):
    ls=[]
    foldername=root.split(os.path.sep)[-1]
    if dirs==[] and not foldername=="output":
        if len(files)>10:
            counter=int(counter)+1
            print("process:"+str(counter))
            files.sort()
            for i in files:
                #print(os.path.join(root,i))
                ls.append(os.path.join(root,i))
            print(foldername)
            with open("./output/"+foldername+".pdf", "wb") as f:
                f.write(img2pdf.convert([i for i in ls if i.endswith(".png")],compress=True))
                
merger = PdfFileMerger()

outputpath=os.getcwd()+"/output"

ls=[]

for root,dirs,files in os.walk(outputpath):
    for i in files:
        ls.append("./output/"+i)


for pdf in ls:
    merger.append(pdf)

merger.write(title+"_all.pdf")
merger.close()



for j in range(int(len(ls)/10)+1):
    merger = PdfFileMerger()
    
    
    for k in range(10):
        index=k+j*10
        if index==len(ls):
            break
        merger.append(ls[index])
    merger.write(title+"_pt."+str(j+1)+".pdf")
    merger.close()
        


end=time.time()
print(end-start)
print("it takes "+str(int(end-start))+" seconds to finish the process.")

