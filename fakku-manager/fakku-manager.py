import os,img2pdf,time,configparser
from PyPDF2 import PdfFileMerger

if(os.path.isfile(os.getcwd()+"/config.ini"))==False:
    print("config.ini doesn't exist.")
else:
    
    print("cwd:"+os.getcwd())
    title=input("please enter title for the output files:")

    if title=="":
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

    if not os.path.exists(os.getcwd()+"/output"):
        os.mkdir(os.getcwd()+"/output")
    for root,dirs,files in os.walk(os.getcwd()):
        ls=[]
        foldername=root.split(os.path.sep)[-1]
        if foldername=="output":
            passed=True
        if dirs==[] and not foldername=="output":
            if passed==True:
                temp=num-1
            else:
            	temp=num
            	
            if config["img"][str(temp)]=="1":
                counter=counter+1
                print("process:"+str(counter))
                files.sort()
                for i in files:
                    #print(os.path.join(root,i))
                    ls.append(os.path.join(root,i))
                print(foldername)
                #time.sleep(5)
                with open("./output/"+foldername+".pdf", "wb") as f:
                    f.write(img2pdf.convert([i for i in ls if i.endswith(".png")],compress=True))
                #time.sleep(5)
            num=num+1
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

