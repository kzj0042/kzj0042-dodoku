import unittest
import dodoku.info as info

class InfoTest(unittest.TestCase):
    
    def test_Info_001_ShouldReturnMyUserName(self):
        expectedResult = {'info':'kzj0042'}
        parms = {'op':'info'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)