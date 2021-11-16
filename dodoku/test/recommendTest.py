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
            
        def test_002_ShouldReturnStatusListNominal(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r7c9',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"ok"}
            expectedRecommendation = {"recommendation":[3,8]}
            actualStatus = {'status':actualResult['status']}
            actualRecommendation = {'recommendation':actualResult['recommendation']}
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertDictEqual(expectedRecommendation, actualRecommendation)
            
        def test_003_ShouldReturnStatusListEmptyList(self):
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
        
        #sad path
        def test_100_ShouldReturnErrorOutOfBoundsCell(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'recommend', 'cell':'r1c10',  'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = recommend._recommend(parms)
            expectedStatus = {"status":"error: invalid cell"}
            expectedRecommendation = {"recommendation":[]}
            actualStatus = {'status':actualResult['status']}
            actualRecommendation = {'recommendation':actualResult['recommendation']}
            self.assertDictEqual(expectedStatus, actualStatus)
               