# -*- coding: utf-8 -*-
class Person():
    def setName(self,name):
        self.name=name
    def getName(self):
        return  self.name
    def greet(self):
        print  "Helllo，world！I'm %s." %self.name



foo=Person()
foo.setName('马浩')
foo.greet()