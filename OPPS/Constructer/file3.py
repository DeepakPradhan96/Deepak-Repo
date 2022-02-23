from file1 import A
from file2 import B

class C (B):
    def __init__(self):
        print('c construter')

    def cmethod(self):
        print('c method')