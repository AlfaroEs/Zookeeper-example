import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):       
        
    def test_crear_arbol(self):
        tree=Ztree()
        tree.create('/nodo1','contenido1',False,True,0,'/')
        tree.create('/nodo2','contenido2',True,True,20,'/nodo1')
        tree.create('/nodo3','contenido3',True,True,10,'/nodo1')
        tree.create('/nodo4','contenido4',False,True,0,'/nodo3')
        tree.showTree()
    def test_borrar_nodo(self):
        tree = Ztree()
        tree.create('/nodo1','contenido1',False,True,0,'/')
        tree.create('/nodo2','contenido2',True,True,20,'/nodo1')
        tree.create('/nodo3','contenido3',True,True,10,'/nodo1')
        tree.create('/nodo4','contenido4',False,True,0,'/nodo3')
        tree.showTree()
        tree.delete('//nodo1/nodo3',0)
        tree.showTree()

    def test_obtener_hijos(self):
        tree = Ztree()
        tree.create('/nodo1','contenido1',False,True,0,'/')
        tree.create('/nodo2','contenido2',True,True,20,'/nodo1')
        tree.create('/nodo3','contenido3',True,True,10,'/nodo1')
        tree.create('/nodo4','contenido4',False,True,0,'/nodo3')
        tree.getChildren('/nodo1')

if __name__ == '__main__':
    unittest.main()
