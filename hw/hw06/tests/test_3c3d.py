#Marco Tchernychev
#mtcherny@nd.edu
import unittest
import hw6searchsrc
import subprocess
path = "/escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/tests/data/"

class TestClass(unittest.TestCase):
    
    def test_none(self): #no optional args given
        self.assertEqual(subprocess.run(["python3", "hw6searchsrc.py", path+"fmnc_manager.cc"], stdout = subprocess.PIPE).stdout.decode('utf-8'),"path: /escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/tests/data/\n"
                                                                                                                                                    +"file: fmnc_manager.cc\n"
                                                                                                                                                    +"lines: 2310\n")
    def test_include(self): #only include (one arg)
        self.assertEqual(subprocess.run(["python3", "hw6searchsrc.py", path+"fmnc_manager.cc", "--include"], stdout = subprocess.PIPE).stdout.decode('utf-8'),"path: /escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/tests/data/\n"
                                                                                                                                                                                                            +"file: fmnc_manager.cc\n"
                                                                                                                                                                                                            +"lines: 2310\n"
                                                                                                                                                                                                            +"include: 18\n")
    def test_reorder1(self): #permutation of a few args
        self.assertEqual(subprocess.run(["python3", "hw6searchsrc.py", path+"fmnc_manager.cc", "--onelinefuncs", "--includelocal", "--include"], stdout = subprocess.PIPE).stdout.decode('utf-8'),"path: /escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/tests/data/\n"
                                                                                                                                                                                                            +"file: fmnc_manager.cc\n"
                                                                                                                                                                                                            +"lines: 2310\n"
                                                                                                                                                                                                            +"include: 18\n"
                                                                                                                                                                                                            +"includelocal: 11\n"
                                                                                                                                                                                                            +"onelinefuncs: 35\n")
    def test_reorder2(self): #permuation of another set of args
        self.assertEqual(subprocess.run(["python3", "hw6searchsrc.py", path+"fmnc_manager.cc", "--includelocal", "--onelinefuncs", "--memberfuncs"], stdout = subprocess.PIPE).stdout.decode('utf-8'),"path: /escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/tests/data/\n"
                                                                                                                                                                                                                    +"file: fmnc_manager.cc\n"
                                                                                                                                                                                                                    +"lines: 2310\n"
                                                                                                                                                                                                                    +"includelocal: 11\n"
                                                                                                                                                                                                                    +"memberfuncs: 77\n"
                                                                                                                                                                                                                    +"onelinefuncs: 35\n")
    def test_all(self): #testing all of the args
        self.assertEqual(subprocess.run(["python3", "hw6searchsrc.py", path+"fmnc_manager.cc", "--include", "--includelocal", "--memberfuncs","--onelinefuncs"], stdout = subprocess.PIPE).stdout.decode('utf-8'),"path: /escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/tests/data/\n"
                                                                                                                                                                                                                    +"file: fmnc_manager.cc\n"
                                                                                                                                                                                                                    +"lines: 2310\n"
                                                                                                                                                                                                                    +"include: 18\n"
                                                                                                                                                                                                                    +"includelocal: 11\n"
                                                                                                                                                                                                                    +"memberfuncs: 77\n"
                                                                                                                                                                                                                    +"onelinefuncs: 35\n")
    def test_nofile(self): #if no file specified
        result = subprocess.run(["python3", "hw6searchsrc.py", "--include", "--includelocal", "--memberfuncs","--onelinefuncs"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stderr.decode('utf-8')
        self.assertTrue("the following arguments are required" in result)

    def test_noexistfile(self): #if the file doesn't exist
        result = subprocess.run(["python3", "hw6searchsrc.py", path+"fmnc_mngr.cc", "--include", "--includelocal", "--memberfuncs","--onelinefuncs"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stderr.decode('utf-8')
        self.assertTrue("FileNotFoundError" in result)
    
    def test_notcc(self): #if no cc files exist
        result = subprocess.run(["python3", "hw6searchsrc.py", path+"fmnc_manager.cc", "--include", "--includelocal", "--memberfuncs","--onelinefuncs"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertTrue(".cc" in result)
    
    def test_isadir(self): #if a directory and not a file
        result = subprocess.run(["python3", "hw6searchsrc.py", path, "--include", "--includelocal", "--memberfuncs","--onelinefuncs"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stderr.decode('utf-8')
        self.assertTrue("IsADirectoryError" in result)
    
    def test_invalidarg(self): #if an argument is not valid
        result = subprocess.run(["python3", "hw6searchsrc.py", path+"fmnc_mngr.cc", "--inclu", "--includelocal", "--memberfuncs","--onelinefuncs"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stderr.decode('utf-8')
        self.assertTrue("ambiguous option" in result)

if __name__ == "__main__":
    unittest.main()