from unittest import TestCase
import dodoku.insert as insert
import dodoku.calculateHash as calculteHash

class InsertTest(TestCase):
        #happy path tests
        def test_001_ShouldCreateKeys(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'insert', 'cell':'r1c1', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)
            self.assertIn('status', actualResult.keys())
            self.assertIn('grid', actualResult.keys())
            self.assertIn('integrity', actualResult.keys())  
        
        def test_002_ShouldInsertIntoLevel1Grid(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'insert', 'cell':'r7c9', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid':[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,
                                    3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]}                                
            expectedStatus = {'status':'ok'}
            expectedHash = "72a87aa0938dfb1b7edf4c31cd75bb0db75e916ff3f7ea9c1671cdd569cef463"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)
        
        def test_003_ShouldInsertIntoLevel2Grid(self):
            grid = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]                                
            parms = {'op':'insert', 'cell':'r7c9', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid': [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,
                                     3,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]}
            expectedStatus = {'status':'ok'}
            expectedHash = "a0b5caf1068e80a4fa426de2ed1a84644aa0aa18ccc7c09303b727266ea41ea2"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)  
                 
        def test_004_ShouldInsertIntoLevel3Grid(self):
            grid = [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,-3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0,-7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,-9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,-6,-5,0,0,0,-7,-3,0,-5,-9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0]                                                
            parms = {'op':'insert', 'cell':'r7c9', 'value':'9', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid': [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,
                                     9,0,-3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0, -7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,-9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,-6,-5,0,0,0,-7,-3,0,-5,-9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0]}
            expectedStatus = {'status':'ok'}
            expectedHash = "b84a72fb1878046502ec90369c04b6c2a03771437f6c26b175de0e720e051bcd"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)   
        
        def test_005_ShouldInsertUpperCaseRowAndCol(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'insert', 'cell':'R7C9', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid':[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]}                                
            expectedStatus = {'status':'ok'}
            expectedHash = "72a87aa0938dfb1b7edf4c31cd75bb0db75e916ff3f7ea9c1671cdd569cef463"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)
            
        def test_006_ShouldInsertWithWarningStatusSameColumn(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
            parms = {'op':'insert', 'cell':'r7c9', 'value':'5', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid':[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,5,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,
                                    -9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]}                                
            expectedStatus = {'status':'warning'}
            expectedHash = "2a2706879b00dc00937cea6d2f057b72bd1141ab09fd1b1e8a5c53f6fb6789db"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)     
        
        def test_007_ShouldInsertWithWarningStatusSameRow(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,
                    0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
                                
            parms = {'op':'insert', 'cell':'r7c13', 'value':'2', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid':[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,
                    2,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]}                                
            expectedStatus = {'status':'warning'}
            expectedHash = "9cb5eea670e0547ab2bc25f3636782801a09e98b8f5cb9217dbcc2267057c597"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)   
        
        def test_008_ShouldInsertWithWarningSameSubGraph(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,
                    0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'insert', 'cell':'r14c14', 'value':'1', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid':[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,
                                    1,0,0,-6,0,0,-5,0,0,-3,-1]}                                
            expectedStatus = {'status':'warning'}
            expectedHash = "71cf92703993dec28d704d1e85cea9ce4f6626eca2468347fd51e8712ed69edc"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)    
        
        def test_009_ShouldInsertAtMaximumPossibleRowAndColumn(self):
            grid = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]                                
            parms = {'op':'insert', 'cell':'r15c15', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid': [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,
                                     0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,3]}
            expectedStatus = {'status':'ok'}
            expectedHash = "a6518efb6387a8f775b11305ffffe48816ad36628d8d5e8ee0641795859dff37"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)   
        
        def test_010_ShouldInsertAtMinimumPossibleRowAndColumn(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'insert', 'cell':'r1c1', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid':[3,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,
                                    0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]}                                
            expectedStatus = {'status':'ok'}
            expectedHash = "31f66be2552d8f77f2d68cb81722d7b7980e5483b9c66ce468144a8839c7ec12"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)
            
        def test_011_ShouldRemoveAtMaximumPossibleRowAndColumn(self):
            grid = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,
                    -7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,3]                                
            parms = {'op':'insert', 'cell':'r15c15', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid': [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,
                                     0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]}
            expectedStatus = {'status':'ok'}
            expectedHash = "6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)       
            
        def test_012_ShouldRemoveAtMinimumPossibleRowAndColumn(self):
            grid = [3,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'insert', 'cell':'r1c1', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid':[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,
                                    0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]}                                
            expectedStatus = {'status':'ok'}
            expectedHash = "5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)      
            
        def test_013_ShouldRemoveAtNominalRowAndColumn(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,
                                    3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'insert', 'cell':'r7c9', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid':[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,
                                    0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]}                                
            expectedStatus = {'status':'ok'}
            expectedHash = "5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd"
            actualGrid = {'grid':actualResult['grid']}
            actualStatus = {'status':actualResult['status']}
            actualHash = actualResult['integrity']
            self.assertDictEqual(expectedGrid, actualGrid)
            self.assertDictEqual(expectedStatus, actualStatus)
            self.assertIn(actualHash, expectedHash)                        
        
        #sad path tests
        def test_100_ShouldNotInsertInvalidCell(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
            parms = {'op':'insert', 'cell':'r10c1', 'value':'1', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)
            expectedResult = 'error: invalid cell reference'
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)            
            
        def test_101_ShouldNotInsertNoLocationGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
            parms = {'op':'insert', 'value':'1', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)
            expectedResult = 'error: missing cell reference'
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)            
            
        def test_102_ShouldNotInsertInvalidValue(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
            parms = {'op':'insert', 'cell':'r7c9', 'value':'a', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms) 
            expectedResult = 'error: invalid value'
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)                        

        def test_103_ShouldNotInsertOverwriteFixedHint(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
            parms = {'op':'insert', 'cell':'r7c11', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)
            expectedResult = 'error: attempt to change fixed hint'
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus) 
            
        def test_104_ShouldNotInsertInvalidGrid(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,'a',0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
            parms = {'op':'insert', 'cell':'r7c9', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms)
            expectedResult = 'error: invalid grid'
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus) 
            
        def test_105_ShouldNotInsertInvalidIntegrity(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
            parms = {'op':'insert', 'cell':'r7c9', 'value':'3', 'grid':grid, 'integrity':'abcd1234'}
            actualResult = insert._insert(parms)
            expectedResult = 'error: integrity mismatch'
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)   
            
        def test_106_ShouldNotInsertValueTooLarge(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
            parms = {'op':'insert', 'cell':'r7c9', 'value':'10', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms) 
            expectedResult = 'error: invalid value'
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)                      
            
        def test_107_ShouldNotInsertValueTooSmall(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
            parms = {'op':'insert', 'cell':'r7c9', 'value':'0', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
            actualResult = insert._insert(parms) 
            expectedResult = 'error: invalid value'
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)  
            
        def test_108_ShouldNotInsertValueNegativeRow(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'insert', 'cell':'r-1c5', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = insert._insert(parms)
            expectedResult = 'error: invalid cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)      
            
        def test_109_ShouldNotInsertValueNegativeColumn(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'insert', 'cell':'r5c-1', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = insert._insert(parms)
            expectedResult = 'error: invalid cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)   
            
        def test_110_ShouldNotInsertValueBigRow(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'insert', 'cell':'r16c5', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = insert._insert(parms)
            expectedResult = 'error: invalid cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)   
            
        def test_111_ShouldNotInsertValueBigColumn(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'insert', 'cell':'r5c16', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = insert._insert(parms)
            expectedResult = 'error: invalid cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)
            
        def test_112_ShouldNotInsertValueRowNotGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'insert', 'cell':'c3', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = insert._insert(parms)
            expectedResult = 'error: missing cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)  
            
        def test_113_ShouldNotInsertValueColumnNotGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'insert', 'cell':'r7', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = insert._insert(parms)
            expectedResult = 'error: missing cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)            
            
        def test_114_ShouldNotInsertValueRowAndColumnNotGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'insert', 'cell':'', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = insert._insert(parms)
            expectedResult = 'error: missing cell reference' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)    
            
        def test_115_ShouldNotInsertLargeGridValueGiven(self):
            grid = [10,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'insert', 'cell':'r7c9', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = insert._insert(parms)
            expectedResult = 'error: invalid grid' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)
            
        def test_116_ShouldNotInsertSmallGridValueGiven(self):
            grid = [-10,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'insert', 'cell':'r7c9', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}      
            actualResult = insert._insert(parms)
            expectedResult = 'error: invalid grid' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)   
            
        def test_117_ShouldNotInsertEightCharactersOfIntegrityNotGiven(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,
                    -2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]     
            parms = {'op':'insert', 'cell':'r7c9', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(1))}      
            actualResult = insert._insert(parms)
            expectedResult = 'error: integrity mismatch' 
            actualStatus = actualResult['status']
            self.assertEqual(expectedResult, actualStatus)                                   