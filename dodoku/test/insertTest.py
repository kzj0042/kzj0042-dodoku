from unittest import TestCase
import dodoku.insert as insert 
import dodoku.create as create 

class InsertTest(TestCase):
        #happy path tests
        def test_001_ShouldCreateKeys(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'insert', 'cell':'r1c1', 'value':'3', 'grid':grid, 'integrity':create.calculateHash(grid)}
            actualResult = insert._insert(parms)
            self.assertIn('status', actualResult.keys())
            self.assertIn('grid', actualResult.keys())
            self.assertIn('integrity', actualResult.keys())  
        
        def test_002_ShouldInsertIntoLevel1Grid(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'insert', 'cell':'r7c9', 'value':'3', 'grid':grid, 'integrity':create.calculateHash(grid)}
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
        
        def test_003_ShouldInsertIntoLevel2Grid(self):
            grid = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]                                
            parms = {'op':'insert', 'cell':'r7c9', 'value':'3', 'grid':grid, 'integrity':create.calculateHash(grid)}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid': [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,3,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]}
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
            parms = {'op':'insert', 'cell':'r7c9', 'value':'9', 'grid':grid, 'integrity':create.calculateHash(grid)}
            actualResult = insert._insert(parms)              
            expectedGrid = {'grid': [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,9,0,-3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0,
                                     -7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,-9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,-6,-5,0,0,0,-7,-3,0,-5,-9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0]}
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
            parms = {'op':'insert', 'cell':'R7C9', 'value':'3', 'grid':grid, 'integrity':create.calculateHash(grid)}
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
            parms = {'op':'insert', 'cell':'r7c9', 'value':'5', 'grid':grid, 'integrity':create.calculateHash(grid)}
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
                                
            parms = {'op':'insert', 'cell':'r7c13', 'value':'2', 'grid':grid, 'integrity':create.calculateHash(grid)}
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
        
        #sad path tests
