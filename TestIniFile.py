import unittest
from IniParser.ParseIni import ParseIni
class TestsIniFile(unittest.TestCase):
    def setUp(self) -> None:
        self.ini =  ParseIni('''
        [global]
        name = ahmed 
        age = 20
        [idont' have a name]
        hello = hi 
        [global]
        city = cairo  
        ''').iniResult

    def testHasSection(self):
        self.assertFalse(self.ini.HasSection("[idont' have a name]"))
        self.assertFalse(self.ini.HasSection(""))
        self.assertFalse(self.ini.HasSection("name = sds"))
        self.assertFalse(self.ini.HasSection("idont' have a name"))

    def testHasProperty(self):
        self.assertFalse(self.ini.HasProperty('global' , 'name'))
        self.assertFalse(self.ini.HasProperty('global' , 'sd'))
        self.assertFalse(self.ini.HasProperty('!global' , 'name'))

    def testDeleteProperty(self):
        self.assertFalse(self.ini.DeleteProperty('global', 'name'))
        self.assertFalse(self.ini.DeleteProperty('global', 'sd'))
        self.assertFalse(self.ini.DeleteProperty('!global', 'name'))

    def testGetProperty(self):
        self.assertEqual(str(self.ini.GetProperty('global' ,'age')) , '20')
        self.assertFalse(self.ini.GetProperty('global' ,'name'))

if __name__ == '__main__':
    unittest.main()