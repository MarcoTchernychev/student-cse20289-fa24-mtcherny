import unittest
import hw6searchdir
import subprocess
path = "/escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/ex-tests/"
class TestClass(unittest.TestCase):
    
    def test_nrd1(self):
        result = subprocess.run(["python3", "hw6searcdir.py", path+"nrd-1/"], stdout = subprocess.PIPE)
        self.assertEqual(result, path+"nrd-1/, ParamDictionary.cc, 379 LOC, 3 I, 1 LI, 26 MF, 10 OLF\n"
                                    +path+"nrd-1/, PktQueue.cc, 42 LOC, 1 I, 1 LI, 4 MF, 4 OLF\n"
                                    +path+"nrd-1/, RIPPS_PktPair.cc, 607 LOC, 5 I, 3 LI, 50 MF, 23 OLF\n"
                                    +path+"nrd-1/, Thread_IO.cc, 149 LOC, 7 I, 5 LI, 0 MF, 0 OLF\n"
                                    +path+"nrd-1/, fmnc_manager.cc, 2310 LOC, 18 I, 11 LI, 77 MF, 35 OLF\n")
    #def test_nrd2(self):
    #    self.assertEqual()
    #def test_nrd3(self):
    #    self.assertEqual()
    #def test_rd1(self):
    #    self.assertEqual()
    #def test_rd2(self):
    #    self.assertEqual()
    #def test_rd3(self):
    #    self.assertEqual()
    #def test_rd4(self):
    #    self.assertEqual()

if __name__ == "__main__":
    unittest.main()