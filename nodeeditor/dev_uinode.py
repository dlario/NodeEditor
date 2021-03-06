# gui for nodes deveopment
from PyFlow.UI.Canvas.UINodeBase import UINodeBase
from PyFlow.UI.Canvas.UICommon import NodeActionButtonInfo

from nodeeditor.say import *

# the methods

if 1:


    def f4(self):
        sayl()
        #self._rawNode.refresh()
        say("done")

    def deleteNode(self):
        self._rawNode.kill()

    def debug(self):
        try:
            self._rawNode._debug = not self._rawNode._debug
        except:
            self._rawNode._debug = True

    def bake(self,*args,**kvargs):
        #say("bake from gui not implemented - use for test icons")
        s=self._rawNode.getPinObject('Shape_out')
        try: 
            s=self._rawNode.getPinObject('Shape_out')
        except:
            say("nothing to bake")
            return
     
        
        f = FreeCAD.ActiveDocument.addObject('Part::Feature','baked')
        f.Shape=s



#the add action

def addActions(self,RESOURCES_DIR):
        
        actionAddOut2 = self._menu.addAction("show node")
        actionAddOut2.setData(NodeActionButtonInfo(RESOURCES_DIR + "/show.svg"))
        actionAddOut2.setToolTip("show internal data of the node")
        actionAddOut2.triggered.connect(self._rawNode.show)

        actionAddOut3 = self._menu.addAction("compute node")
        actionAddOut3.setData(NodeActionButtonInfo(RESOURCES_DIR + "/compute.svg"))
        actionAddOut3.setToolTip("compute node")
        actionAddOut3.triggered.connect(self._rawNode.compute)

        # methods for the contextmenu
        self._menu.addAction("visualize").triggered.connect(self.visualize)
        self._menu.addAction("delete node").triggered.connect(self.deleteNode)
        self._menu.addAction("debug mode").triggered.connect(self.debug)
        self._menu.addAction("bake mode").triggered.connect(self.bake)


#        typ=self._rawNode.__class__.__name__
        
        # erzeuge abhaengig vond e pins methoden
        # wenn shape_out, dann visualizer, baker
        #  



import os

def loadimage(self,RESOURCES_DIR):
    '''load the icon for a node'''

    image=RESOURCES_DIR + "/"+ str(self._rawNode.__class__.__name__).lower()+".svg"
    if os.path.exists(image):
        self.image = image
        self.svgIcon.setElementId("ALL")

        self.svgIcon.setElementId("layer1")
    else:
        self.image = RESOURCES_DIR + "/freecad.svg"
        self.svgIcon.setElementId("layer1")

    self.svgIcon.setScale(0.5)
    self.svgIcon.setPos(-20, -20)



