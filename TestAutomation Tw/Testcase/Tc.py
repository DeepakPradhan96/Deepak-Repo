'''import Library.CommonModul   # diretry.py file(All class Import)

objA=Library.CommonModul.A()# diretry.modul.clss
objA.startBroswerA()

objB=Library.CommonModul.B()
objB.startBroswerB()'''

'''from Library.CommonModul import  A,B  #only mension class import 2. No need diretry.modul name
objB=B()
objB.startBroswerB()

obj=A()
obj.startBroswerA()'''

'''import Pages.login.abc # sub directry
obj=Pages.login.abc.C()
obj.test()'''

from Pages.login.abc import C

objC=C()
objC.test()