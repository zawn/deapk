# -*- coding: GBK -*-

import os
import shutil   
import re     
import zipfile
import time
import shutil
import subprocess
import sys
import win32process
import win32gui
from keyinput.action_base       import ActionBase
from keyinput.action_key        import Key
from keyinput.window_mgr        import WindowMgr

def tests():
    print "ִ�����sds"
    return False

class KeyOpenWindows:

    def __init__ (self, winName = None, action = None, result = None, wait = 5, repeat = 0,name = "None"):
        """Constructor"""
        assert isinstance(action, ActionBase)
        self._action = action
        self._winName = winName
        self._result = result
        self._wait = wait
        self._repeat = repeat
        self._name = name



    def openwindows(self):
	print "\n���ڽ���:"+self._name
        if self.test_openwindows(self._winName):
            sys.stdout.write('|')
            time.sleep(0.1)
            sys.stdout.write('.')
            self._action.execute()
            time.sleep(0.1)
            sys.stdout.write('.')
            if not self.test_openwindows(self._result):
                if self._repeat > 0 :
                    print "\n���Բ���:"+ self._name+str(self._repeat)
                    self._repeat = self._repeat -1
                    self.openwindows();
                else:
                    print "\n����ʧ��:"+ self._name
                    return False
            time.sleep(0.1)
           # print "\n�����ɹ�:" +self._name
            return True
        else:
            print "\n����ʧ��:"+self._name
            return False
        
    def test_openwindows(self,fun):
        sys.stdout.write('|')
        if isinstance(fun, str):
            return self.wait_and_fore(fun)
        else:
            return fun()

    def wait_and_fore(self,title):
        w = WindowMgr()
        i= self._wait *10
        while w._handle == None:
            i = i-1
            if i < 0:
                sys.stdout.write("\nδ�ҵ�����:"+title)
                return False
            w.find_window_wildcard(title+".*")
            time.sleep(0.1)
            sys.stdout.write('.')   
        w.set_foreground()
        time.sleep(0.1)
        if not win32gui.IsWindowEnabled(w._handle):
            print "\n���ڲ�����,���ڲ��ҹ�������"
            hwnds = w.get_hwnds_for_hwnd()
            for hwnd in  hwnds:
                print hwnd, "=>", win32gui.GetWindowText (hwnd)
            print "���ر����´���"    
            for hwnd in  hwnds:
                if hwnd != w._handle:
                    print hwnd, "=>", win32gui.GetWindowText (hwnd)
                    win32gui.SetForegroundWindow(hwnd)
                    time.sleep(0.1)
                    Key("a-f4").execute()
            return self.wait_and_fore(title)
        return True
        


