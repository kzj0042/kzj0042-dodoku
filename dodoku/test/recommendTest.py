from unittest import TestCase
import dodoku.recommend as recommend 
import dodoku.calculateHash as calculteHash

class RecommendTest(TestCase):
        #happy path
        def test_001_ShouldCreateKeys(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r7c9',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            self.assertIn('recommendation', actualResult.keys())
            self.assertIn('status', actualResult.keys())
            
        def test_002_ShouldReturnStatusListNominalRowAndColumn(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r7c9',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"ok"}
            expectedRecommendation = {"recommendation":[3,8]}
            actualStatus = {'status':actualResult['status']}
            actualRecommendation = {'recommendation':actualResult['recommendation']}
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertDictEqual(expectedRecommendation, actualRecommendation)
            
        def test_003_ShouldReturnStatusListSmallestPossibleRowAndColumn(self):
            grid = [0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c1',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"ok"}
            expectedRecommendation = {"recommendation":[]}
            actualStatus = {'status':actualResult['status']}
            actualRecommendation = {'recommendation':actualResult['recommendation']}
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertDictEqual(expectedRecommendation, actualRecommendation)      
         
        def test_004_ShouldReturnEmptyListImmutableHint(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c2',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"ok"}
            expectedRecommendation = {"recommendation":[]}
            actualStatus = {'status':actualResult['status']}
            actualRecommendation = {'recommendation':actualResult['recommendation']}
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertDictEqual(expectedRecommendation, actualRecommendation)      
            
        def test_005_ShouldReturnStatusListChangingUserInput(self):
            grid = [0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c3',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"ok"}
            expectedRecommendation = {"recommendation":[5]}
            actualStatus = {'status':actualResult['status']}
            actualRecommendation = {'recommendation':actualResult['recommendation']}
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertDictEqual(expectedRecommendation, actualRecommendation)   
            
        def test_006_ShouldReturnStatusListLargestPossibleRowAndColumn(self):
            grid = [0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,0]
            parms = {'op':'recommend', 'cell':'r15c15',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"ok"}
            expectedRecommendation = {"recommendation":[1,2,4,7]}
            actualStatus = {'status':actualResult['status']}
            actualRecommendation = {'recommendation':actualResult['recommendation']}
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertDictEqual(expectedRecommendation, actualRecommendation) 
            
        def test_007_ShouldReturnStatusListLargeRowSmallColumn(self):
            grid = [0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r15c7',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"ok"}
            expectedRecommendation = {"recommendation":[8,9]}
            actualStatus = {'status':actualResult['status']}
            actualRecommendation = {'recommendation':actualResult['recommendation']}
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertDictEqual(expectedRecommendation, actualRecommendation)    
            
        def test_008_ShouldReturnStatusListSmallRowLargeColumn(self):
            grid = [0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r7c15',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"ok"}
            expectedRecommendation = {"recommendation":[2,3,7]}
            actualStatus = {'status':actualResult['status']}
            actualRecommendation = {'recommendation':actualResult['recommendation']}
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertDictEqual(expectedRecommendation, actualRecommendation)    
            
        def test_009_ShouldReturnStatusListUpperCaseRowAndCol(self):
            grid = '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
            parms = {'op':'recommend', 'cell':'R7C9', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)              
            expectedStatus = {"status":"ok"}
            expectedRecommendation = {"recommendation":[3,8]}
            actualStatus = {'status':actualResult['status']}
            actualRecommendation = {'recommendation':actualResult['recommendation']}
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertDictEqual(expectedRecommendation, actualRecommendation)                                
        
        #sad path
        def test_100_ShouldReturnErrorOutOfBoundsCell(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c10',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: invalid cell reference"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)
        
        def test_101_ShouldReturnErrorTooHighGridValueGiven(self):
            grid = [10,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c1',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: invalid grid"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)
            
        def test_102_ShouldReturnErrorGridTooSmall(self):
            grid = [-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c1',  'grid':grid, 'integrity':'abcd1234'}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: invalid grid"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)    
            
        def test_103_ShouldReturnErrorCellNotGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: invalid cell"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)
            
        def test_104_ShouldReturnErrorGridNotGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c1', 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: invalid grid"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)  
            
        def test_105_ShouldReturnErrorIntegrityNotGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c1', 'grid':grid}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: invalid integrity"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)                        

        def test_106_ShouldReturnErrorInvalidIntegrityValue(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c1', 'grid':grid, 'integrity':'12345678'}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: integrity mismatch"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)              
            
        def test_107_ShouldReturnErrorInvalidIntegrityValueLength(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c1', 'grid':grid, 'integrity':'1234568'}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: integrity mismatch"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)
            
        def test_108_ShouldReturnErrorInvalidValueInGrid(self):
            grid = ['a',-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c2',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: invalid grid"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)
            
        def test_109_ShouldReturnErrorTooLowGridValueGiven(self):
            grid = [-10,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r7c9',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: invalid grid"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)
            
        def test_110_ShouldReturnErrorValueNegativeRow(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'recommend', 'cell':'r-1c5', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = recommend._recommend(parms)
            expectedResult = 'error: invalid cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)  
            
        def test_111_ShouldReturnErrorValueNegativeColumn(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'recommend', 'cell':'r5c-1', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = recommend._recommend(parms)
            expectedResult = 'error: invalid cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)
            
        def test_112_ShouldReturnErrorValueBigRow(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'recommend', 'cell':'r16c5', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = recommend._recommend(parms)
            expectedResult = 'error: invalid cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus) 
            
        def test_113_ShouldReturnErrorValueBigColumn(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'recommend', 'cell':'r5c16', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = recommend._recommend(parms)
            expectedResult = 'error: invalid cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)

        def test_114_ShouldReturnErrorValueRowNotGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'recommend', 'cell':'c3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = recommend._recommend(parms)
            expectedResult = 'error: missing cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)
        
        def test_115_ShouldReturnErrorColumnNotGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'recommend', 'cell':'r7', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = recommend._recommend(parms)
            expectedResult = 'error: missing cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)   
            
        def test_116_ShouldReturnErrorRowAndColumnNotGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'recommend', 'cell':'', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = recommend._recommend(parms)
            expectedResult = 'error: missing cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)          

        def test_117_ShouldReturnErrorGridTooLarge(self):
            grid = [0,0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c1',  'grid':grid, 'integrity':'abcd1234'}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: invalid grid"}
            actualStatus = {'status':actualResult['status']}
            self.assertDictEqual(expectedStatus, actualStatus)  

        def test_118_ShouldReturnErrorNonIntRowGiven(self):
            grid = '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'                                
            parms = {'op':'recommend', 'cell':'rac9', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedResult = 'error: invalid cell reference'
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)
            
        def test_119_ShouldReturnErrorNonIntColGiven(self):
            grid = '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'                                
            parms = {'op':'recommend', 'cell':'r7caa', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedResult = 'error: invalid cell reference'
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)
            
        def test_120_ShouldReturnErrorColumnBeforeRow(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'recommend', 'cell':'c5r5', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = recommend._recommend(parms)
            expectedResult = 'error: missing cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)            
        