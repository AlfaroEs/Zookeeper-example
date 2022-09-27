from genericpath import exists
import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)
    
    def test_cambio_data(self):
        tree = Ztree()
        tree.create('/node1','data vieja',False,True,15,'/')
        tree.setData('/node1','nueva data')
        self.assertEqual(tree.getData('/node1'),'nueva data')
    
    def test_busqueda_nodo(self):
        tree = Ztree()
        tree.create('/node1','data',False,True,15,'/')
        self.assertFalse(exists('/node2'))
    
    def test_eliminacion_nodo_regular(self):
        tree = Ztree()
        tree.create('/node1','data',False,True,15,'/')
        tree.delete('/node1',0)
        self.assertFalse(exists('/node1'))

    def test_eliminacion_nodo_ephemero(self):
        tree = Ztree()
        tree.create('/node1','data',True,True,15,'/')
        tree.delete('/node1',0)
        self.assertFalse(exists('/node1'))
    
    def test_eliminacion_nodo_ephemero_inactivo(self):
        tree = Ztree()
        tree.create('/node1','data',True,False,15,'/')
        tree.delete('/node1',0)
        self.assertFalse(exists('/node1'))
        
        


if __name__ == '__main__':
    unittest.main()

