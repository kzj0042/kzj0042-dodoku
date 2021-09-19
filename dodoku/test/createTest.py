from unittest import TestCase
import dodoku.create as create 

class CreateTest(TestCase):
        def test_001_ShouldReturnStatusOk(self):
            expectedResult = {"status":"ok"}
            parms = {'op':'create'}
            actualResult = create._create(parms)
            self.assertDictEqual(expectedResult, actualResult)
