#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

def setup():
    shelltools.system("unzip android-studio-ide-182.5199772-linux.zip")

def install():
    pisitools.insinto("/opt/android-studio", "android-studio/*")
    pisitools.dosym("/opt/android-studio/bin/studio.sh", "/usr/bin/android-studio")
