#Marco Tchernychev
#mtcherny@nd.edu
import unittest
import hw6searchsrc
path = "/escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/tests/data/"
class TestClass(unittest.TestCase):
    
    def test_locPD(self): #lines of code
        self.assertEqual(len(hw6searchsrc.readFile(path+"ParamDictionary.cc")), 379)
    def test_incPD(self): #includes
        self.assertEqual(hw6searchsrc.countInclude(hw6searchsrc.readFile(path+"ParamDictionary.cc")), 3)
    def test_inclocPD(self): #local includes
        self.assertEqual(hw6searchsrc.countIncludeLocal(hw6searchsrc.readFile(path+"ParamDictionary.cc")), 1)
    def test_mfPD(self): #memberfuncs
        self.assertEqual(hw6searchsrc.countMemberFuncs(hw6searchsrc.readFile(path+"ParamDictionary.cc")), 26)
    def test_olfPD(self): #one line funcs
        self.assertEqual(hw6searchsrc.countOneLineFuncs(hw6searchsrc.readFile(path+"ParamDictionary.cc")), 10)
    def test_pathPD(self): #path
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"ParamDictionary.cc")[0], path)
    def test_filenamePD(self): #file name
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"ParamDictionary.cc")[1], "ParamDictionary.cc")

    def test_locPQ(self):
        self.assertEqual(len(hw6searchsrc.readFile(path+"PktQueue.cc")), 42)
    def test_incPQ(self):
        self.assertEqual(hw6searchsrc.countInclude(hw6searchsrc.readFile(path+"PktQueue.cc")), 1)
    def test_inclocPQ(self):
        self.assertEqual(hw6searchsrc.countIncludeLocal(hw6searchsrc.readFile(path+"PktQueue.cc")), 1)
    def test_mfPQ(self):
        self.assertEqual(hw6searchsrc.countMemberFuncs(hw6searchsrc.readFile(path+"PktQueue.cc")), 4)
    def test_olfPQ(self):
        self.assertEqual(hw6searchsrc.countOneLineFuncs(hw6searchsrc.readFile(path+"PktQueue.cc")), 4)
    def test_pathPQ(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"PktQueue.cc")[0], path)
    def test_filenamePQ(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"PktQueue.cc")[1], "PktQueue.cc")

    def test_locRP(self):
        self.assertEqual(len(hw6searchsrc.readFile(path+"RIPPS_PktPair.cc")), 607)
    def test_incRP(self):
        self.assertEqual(hw6searchsrc.countInclude(hw6searchsrc.readFile(path+"RIPPS_PktPair.cc")), 5)
    def test_inclocRP(self):
        self.assertEqual(hw6searchsrc.countIncludeLocal(hw6searchsrc.readFile(path+"RIPPS_PktPair.cc")), 3)
    def test_mfRP(self):
        self.assertEqual(hw6searchsrc.countMemberFuncs(hw6searchsrc.readFile(path+"RIPPS_PktPair.cc")), 50)
    def test_olfRP(self):
        self.assertEqual(hw6searchsrc.countOneLineFuncs(hw6searchsrc.readFile(path+"RIPPS_PktPair.cc")), 23)
    def test_pathRP(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"RIPPS_PktPair.cc")[0], path)
    def test_filenameRP(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"RIPPS_PktPair.cc")[1], "RIPPS_PktPair.cc")

    def test_locTI(self):
        self.assertEqual(len(hw6searchsrc.readFile(path+"Thread_IO.cc")), 149)
    def test_incTI(self):
        self.assertEqual(hw6searchsrc.countInclude(hw6searchsrc.readFile(path+"Thread_IO.cc")), 7)
    def test_inclocTI(self):
        self.assertEqual(hw6searchsrc.countIncludeLocal(hw6searchsrc.readFile(path+"Thread_IO.cc")), 5)
    def test_mfTI(self):
        self.assertEqual(hw6searchsrc.countMemberFuncs(hw6searchsrc.readFile(path+"Thread_IO.cc")), 0)
    def test_olfTI(self):
        self.assertEqual(hw6searchsrc.countOneLineFuncs(hw6searchsrc.readFile(path+"Thread_IO.cc")), 0)
    def test_pathTI(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"Thread_IO.cc")[0], path)
    def test_filenameTI(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"Thread_IO.cc")[1], "Thread_IO.cc")

    def test_locFM(self):
        self.assertEqual(len(hw6searchsrc.readFile(path+"fmnc_manager.cc")), 2310)
    def test_incFM(self):
        self.assertEqual(hw6searchsrc.countInclude(hw6searchsrc.readFile(path+"fmnc_manager.cc")), 18)
    def test_inclocFM(self):
        self.assertEqual(hw6searchsrc.countIncludeLocal(hw6searchsrc.readFile(path+"fmnc_manager.cc")), 11)
    def test_mfFM(self):
        self.assertEqual(hw6searchsrc.countMemberFuncs(hw6searchsrc.readFile(path+"fmnc_manager.cc")), 77)
    def test_olfFM(self):
        self.assertEqual(hw6searchsrc.countOneLineFuncs(hw6searchsrc.readFile(path+"fmnc_manager.cc")), 35)
    def test_pathFM(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"fmnc_manager.cc")[0], path)
    def test_filenameFM(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"fmnc_manager.cc")[1], "fmnc_manager.cc")

if __name__ == "__main__":
    unittest.main()