"""
    Created on September 29, 2021
    
    @author: Kyle Julien
"""
from unittest import TestCase
import dodoku.create as create 
import dodoku.calculateHash as calculateHash

class CreateTest(TestCase):
        #happy path tests
        def test_001_ShouldCreateKeys(self):
            parms={'op':'create', 'level':'1'}
            actualResult = create._create(parms)
            self.assertIn('grid', actualResult.keys())
            self.assertIn('status', actualResult.keys())
            self.assertIn('integrity', actualResult.keys())
            
        def test_002_ShouldCreateLevel1Grid(self):
            expectedGrid = {"grid":[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-
9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-
9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-
5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1] }
            expectedStatus = {'status':'ok'}
            expectedHash = '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
            parms={'op':'create', 'level':'1'}
            actualResult = create._create(parms)
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)
            
        def test_003_ShouldCreateLevel2Grid(self):
            expectedGrid = {"grid": [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-
6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-
9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-
1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0] }
            expectedStatus = {'status':'ok'}
            expectedHash = '6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a'
            parms={'op':'create', 'level':'2'}
            actualResult = create._create(parms)
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)
                        
        def test_004_ShouldCreateLevel3Grid(self):
            expectedGrid = {"grid":[0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-
5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,-3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0,-
7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,-9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,-
6,-5,0,0,0,-7,-3,0,-5,-9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0]}
            expectedStatus = {'status':'ok'}
            expectedHash = 'eb572835ffe2015c731057f94d46fa77430ad6fd332abb0d7dd39d5f2ccadea9'
            parms={'op':'create', 'level':'3'}
            actualResult = create._create(parms)
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)
                        
        def test_005_shouldCreateDefaultLevel(self):
            expectedGrid = {"grid":[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-
9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-
9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-
5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1] }
            expectedStatus = {'status':'ok'}
            expectedHash = '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'           
            parms={'op':'create', 'level':''}
            actualResult = create._create(parms)
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)
                    
        def test_006_shouldCreateSha256HashLevel1(self):
            expectedResult = '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
            actualResult = calculateHash.getEightCharactersOfHash(calculateHash.calculateHash('1'))
            self.assertIn(actualResult, expectedResult)
            
        def test_007_shouldCreateSha256HashLevel2(self):
            expectedResult = '6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a'
            grid = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-
6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-
9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-
1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]
            actualResult = calculateHash.getEightCharactersOfHash(calculateHash.calculateHash(grid))
            self.assertIn(actualResult, expectedResult)

        def test_008_shouldCreateSha256HashLevel3(self):
            expectedResult = 'eb572835ffe2015c731057f94d46fa77430ad6fd332abb0d7dd39d5f2ccadea9'
            grid = [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-
5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,-3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0,-
7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,-9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,-
6,-5,0,0,0,-7,-3,0,-5,-9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0]
            actualResult = calculateHash.getEightCharactersOfHash(calculateHash.calculateHash(grid))
            self.assertIn(actualResult, expectedResult)
            
        def test_009_ShouldCreateLevelWithNoLevelParameter(self):
            expectedGrid = {"grid":[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-
9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-
9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-
5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1] }
            expectedStatus = {'status':'ok'}
            expectedHash = '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
            parms={'op':'create'}
            actualResult = create._create(parms)
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)
            
        def test_010_ShouldCreateLevelWithCapitalLevel(self):
            expectedGrid = {"grid":[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-
9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-
9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-
5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1] }
            expectedStatus = {'status':'ok'}
            expectedHash = '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
            parms={'op':'create', 'LeVeL':'3'}
            actualResult = create._create(parms)
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)
            
         #sad path tests   
        def test_101_ShouldCauseErrorInvalidLevel(self):
            expectedResult = {'status':'error: invalid level'}
            parms={'op':'create', 'level':'a'}
            actualResult = create._create(parms)
            self.assertDictEqual(expectedResult, actualResult)
            
        def test_103_ShouldCauseErrorInvalidHighLevelGiven(self):
            expectedResult = {'status':'error: invalid level'}
            parms = {'op':'create', 'level':'10'}
            actualResult = create._create(parms)
            self.assertDictEqual(expectedResult, actualResult)
            
        def test_104_ShouldCauseErrorInvalidLowLevelGiven(self):
            expectedResult = {'status':'error: invalid level'}
            parms = {'op':'create', 'level':'0'}
            actualResult = create._create(parms)
            self.assertDictEqual(expectedResult, actualResult)
            