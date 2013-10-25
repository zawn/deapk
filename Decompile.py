# -*- coding: GBK -*-

import os
import shutil   
import re     
import zipfile
import time
import shutil

ISOTIMEFORMAT="%Y-%m-%d %X"
apktool_bat="lib\\apktool1.5.1\\apktool.bat"
dex2jar_bat="lib\\dex2jar-0.0.9.13\\d2j-dex2jar.bat"
jd_gui_exe="lib\\jd-gui-0.3.5\\jd-gui.exe"
apk_dir="apk"


def execCmd(cmd):
    print "ִ������:"+cmd
    r = os.popen(cmd)
    text = r.readlines()
    r.close()
    return text

def getAPK():
    files = os.listdir(apk_dir);
    results = []
##    print len(files)
    for apkfile in files:
        sufix = os.path.splitext(apkfile)[1]
        if sufix == ".apk":
            results.append(apkfile)
    return results  
    
def decompileApk(distdir,apkfilename,logdir):
    distApkDir = distdir+ os.sep +os.path.splitext(apkfilename)[0]
    print "Apk�ļ�:"+apkfilename
    print "���Ŀ¼:"+distApkDir
    text =  execCmd(apktool_bat + " d -s -f -b \""+ apk_dir + os.sep + apkfilename +"\" \""+distApkDir+"\"")
    for f in text:
        print f
    text =  execCmd(dex2jar_bat + " -f "+"\""+ distApkDir+ os.sep + "classes.dex"+"\""+" -o "+"\""+distApkDir+ os.sep +"classes.jar"+"\""+" -e "+"\""+distApkDir+ os.sep +"classes_error.zip"+"\"")
    for f in text:
        print f
    text =  execCmd(jd_gui_exe + " "+"\""+distApkDir+ os.sep +"classes.jar"+"\"")
    for f in text:
        print f
		
def main():
    starttime =  time.strftime( ISOTIMEFORMAT, time.localtime() )
    print("��ʼʱ��:"+starttime+"\n")
    currentDir =  os.getcwd()
    apks = getAPK()
    if len(apks)>0 :        
##       print("�ϼ�Ŀ¼:"+os.path.abspath(os.pardir )+"\n")
        print("��ǰĿ¼:"+currentDir+"\n")
        distdir = os.path.abspath(currentDir)+ os.sep  +"dist"
        print("���Ŀ¼:"+distdir+"\n")
        if os.path.exists(distdir):
            shutil.rmtree(distdir)
        os.makedirs(distdir)
        logdir = os.path.abspath(currentDir)+ os.sep  +"dist_log"
        print("��־Ŀ¼:"+logdir+"\n")
        if os.path.exists(logdir):
            shutil.rmtree(logdir)
        os.makedirs(logdir)
        i = 0
        length =  len(apks)
        for f in apks:
            i = i +1
            print str(i)+"/"+str(length)
            decompileApk(distdir,f,logdir)
        print("����ʱ��:"+time.strftime( ISOTIMEFORMAT, time.localtime())+"\n")
    else :
        print("û���ҵ��κ�APK�ļ���Ŀ¼:"+os.path.abspath(currentDir)+ os.sep  + apk_dir +"\n")
    raw_input("Press any key to exit")
main()
        
