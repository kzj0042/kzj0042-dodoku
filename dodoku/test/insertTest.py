from unittest import TestCase
import dodoku.insert as insert 
import dodoku.create as create 

class InsertTest(TestCase):
        #happy path tests
        def test_001_ShouldCreateKeys(self):
            grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
            parms = {'op':'insert', 'cell':'r1c1', 'value':'3', 'grid':grid, 'integrity':create.calculateHash('1')}
            actualResult = insert._insert(parms)
            self.assertIn('cell', actualResult.keys())
            self.assertIn('value', actualResult.keys())
            self.assertIn('grid', actualResult.keys())
            self.assertIn('integrity', actualResult.keys())    
                
        #sad path tests
