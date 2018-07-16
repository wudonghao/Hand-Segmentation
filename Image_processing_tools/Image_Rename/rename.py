
 
##############################################  
# 作者：Yohanan  
# 功能：实现文件夹名/文件名/文件内容的关键字查找替换  
##############################################  
  
import os  
import re  
  
#替换文件夹的名字，包括文件夹的字符串含有子字符串  
def replaceDirName(rootDir, oldStr, newStr):  
    for dirpath, dirNames, fileNames in os.walk(rootDir, topdown = False):  
        for dirName in dirNames:  
            if oldStr in dirName:  
                dirNameOld = os.path.join(dirpath,dirName)  
                dirNameNew = os.path.join(dirpath,dirName.replace(oldStr,newStr))  
                print(dirNameOld + ' --> '+ dirNameNew)  
                os.rename(dirNameOld, dirNameNew)  
  
#替换文件名  
def replaceFileName(rootDir, oldStr, newStr):  
    for dirpath, dirNames, fileNames in os.walk(rootDir):  
        for fileName in fileNames:  
            if oldStr in fileName:  
                fileNameOld = os.path.join(dirpath, fileName)  
                fileNameNew = os.path.join(dirpath,fileName.replace(oldStr, newStr))  
                print(fileNameOld + ' --> '+ fileName)  
                os.renames(fileNameOld, fileNameNew)  
  
#替换文件中的内容  
def replaceFileContent(rootDir,oldStr,newStr):  
    for dirpath,dirNames,fileNames in os.walk(rootDir):  
        for fileName in fileNames:  
            fileObj = os.path.join(dirpath,fileName)  
            f = open(fileObj,'r+')  
            all_the_lines=f.readlines()  
            f.seek(0)  
            f.truncate()  
            for line in all_the_lines:  
                f.write(line.replace(oldStr,newStr))  
            f.close()  
  
#执行流  
if __name__ == '__main__':  
    try:  
  
        # rootDir = r"E:\python\test2\FileTest"  
        # oldStr = "doc"  
        # newStr = "new"  
        # replaceDirName(rootDir, oldStr, newStr)  
  
        rootDir = r"/home/wdh/DataSets/hand-segmentation/From Cai/Resize/Masks/yin_pizza"  
        oldStr = ".png"  
        newStr = "yin_pizza.png"  
        replaceFileName(rootDir, oldStr, newStr)  
        pass  
    except Exception as e:  
        print(e)
