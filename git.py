#Modules
import os

def clone(link):
    os.system('git clone {}'.format(link))

def commit(msg):
    os.system('git commit -m {}'.format(msg))
    
def push(name, branch):
    os.system('git push -u {} {}'.format(name) .format(branch))
    
def add(f):
    os.system('git add {}'.format(f))
    
def remote(type, name, link):
    os.system('git remote {} {} {}' .format(type) .format(name) .format(link))
    
