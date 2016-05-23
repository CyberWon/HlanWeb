import unittest
import sys
import hlan
from ext.conf import BASE_DIR


class Testmain(unittest.TestCase):
    
    def test_init(self):
        li=['','my.shell.disk']
        hlan.main(li)
    def test_aa(self):
        print('aa')
        
if __name__=='__main__':
    sys.path.append(BASE_DIR)
    unittest.main()