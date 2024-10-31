import unittest
import hw6searchsrc
path = "/escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/tests/data/"
class TestClass(unittest.TestCase):
    def test_locfmnc(self):
        self.assertEqual(len(hw6searchsrc.readFile(path+"fmnc_manager.cc")), 2310)
    def test_pathfmnc(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"fmnc_manager.cc")[0], path)
    def test_filenamefmnc(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"fmnc_manager.cc")[1],"fmnc_manager.cc")
    
    def test_loc   (self):
        self.assertEqual(len(hw6searchsrc.readFile(path+   )),   )
    def test_inc   (self):
        self.assertEqual(hw6searchsrc.countInclude(hw6searchsrc.readFile(path+   )),   )
    def test_incloc   (self):
        self.assertEqual(hw6searchsrc.countIncludeLocal(hw6searchsrc.readFile(path+   )),   )
    def test_mf  (self):
        self.assertEqual(hw6searchsrc.countMemberFuncs(hw6searchsrc.readFile(path+   )),   )
    def test_path   (self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+   )[0], path)
    def test_filename (self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+   )[1],)

if __name__ == "__main__":
    unittest.main()