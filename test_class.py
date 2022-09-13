import pytest

class TestClassList:

    def test_li(self):
        myList = [-100,-1,0,1,100]
        for x in (myList):
            if x % 2 == 0:
                print ('is even')
            else:
                print ('is odd')
        assert len(myList) == 5

    def test_float(self):
        myList = [-100,-1,0,1,100]
        assert test_li(myList)
