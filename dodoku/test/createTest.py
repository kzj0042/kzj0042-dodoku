from unittest import TestCase
import dodoku.create as create 

class CreateTest(TestCase):
        def test_001_ShouldReturnStatusOk(self):
            expectedResult = {"status":"ok"}
            parms = {'op':'create'}
            actualResult = create._create(parms)
            self.assertDictContainsSubset(expectedResult, actualResult)

        def test_002_ShouldCreateLevel1Grid(self):
            expectedResult = {"grid":[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0], 'status':'ok'}
            parms={'op':'create'}
            actualResult = create._create(parms)
            self.assertDictEqual(expectedResult, actualResult)