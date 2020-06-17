'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided ?as is? with no warranty of any kind and you use the applications at your own risk.

Scripted by Simon Nagel

Just paste the Scene in the Script Editor of VRED and press run.
Navigate around and you will notice that the annotations behind objects will be hidden.
Feel free to adjust annotation properties in the Annotation Module.

'''

import math
import PySide2.QtGui

timer = vrTimer()

def hideOccludedAnnotations():
    annos = vrAnnotationService.getAnnotations()
    
    for i in range(len(annos)):
        QVec = annos[i].getPosition()
        posAnno = [QVec.x(),QVec.y(),QVec.z()]
        camPos = getFrom(-1)
        rayOrigin = Pnt3f(posAnno[0],posAnno[1],posAnno[2])
        rayDirection = Vec3f(camPos.x(),camPos.y(),camPos.z())
    
        intersection = getSceneIntersection(-1, rayOrigin, rayDirection)
    
        interPos = intersection[1]
        x = (posAnno[0], posAnno[1], posAnno[2])
        y = (interPos.x(), interPos.y(), interPos.z())
        z = (camPos.x(),camPos.y(),camPos.z())
        
        distanceInter = sum([(a - b) ** 2 for a, b in zip(x, y)])
        distanceAbsolute =sum([(a - b) ** 2 for a, b in zip(x, z)])
      
        
        if distanceInter<distanceAbsolute:
            annos[i].setVisibilityFlag(0)
        else:
            annos[i].setVisibilityFlag(1)
        
    
timer.connect(hideOccludedAnnotations)
timer.setActive(true)

