from unittest import TestCase
import dodoku.create as create 

class CreateTest(TestCase):
        def test_002_ShouldCreateLevel1Grid(self):
            expectedResult = {"grid":[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0], 'status':'ok'}
            parms={'op':'create&level=1'}
            actualResult = create._create(parms)
            self.assertDictEqual(expectedResult, actualResult)
            
        def test_003_ShouldCreateLevel2Grid(self):
            expectedResult = {"grid":[0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,-8,0,-4,0,0,-1,0,0,0,0,-9,0,0,0,0,0,0,0,0,0,0,0,-7,0,-5,-8,0,0,0,-2,0,0,0,-6,-1,0], 'status':'ok'}
            parms={'op':'create&level=2'}
            actualResult = create._create(parms)
            self.assertDictEqual(expectedResult, actualResult)
            
        def test_004_ShouldCreateLevel3Grid(self):
            expectedResult = {"grid":[0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,0,0,-6,0,-4,0,0,0,0,0,0,0,-5,0,0,0,0,0,-9,-8,-2,0,0,0,-4,-3,0,0,-7,0,0,0,0,0,0], 'status':'ok'}
            parms={'op':'create&level=3'}
            actualResult = create._create(parms)
            self.assertDictEqual(expectedResult, actualResult)