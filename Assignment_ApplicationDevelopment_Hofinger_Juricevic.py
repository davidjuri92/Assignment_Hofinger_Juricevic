##Bike paths near bathing places in Salzburg=name
##SelectBadestellenLayer=vector
##buffer_values=string 500;300;200;100
##bufferresult=output vector

from qgis.core import*
import qgis.utils
from qgis.utils import iface
from PyQt4.QtGui import *


#We decided to add the ESRI Imagery Basemap for better orientation. 
qgis.utils.iface.addRasterLayer("http://server.arcgisonline.com/arcgis/rest/services/ESRI_Imagery_World_2D/MapServer?f=json&pretty=true","ESRI Imagery Basemap")

#Loads the Badestellen Shapefile.
layer1 = iface.addVectorLayer(r'C:\Users\s1000833\Desktop\Badestellen\Badestellen.shp', 'Salzburg Badestellen', 'ogr')

#Loads the Bike paths shapefile.
layer = iface.addVectorLayer(r'C:\Users\s1000833\Desktop\Touristische_Radwege\Touristische_Radwege.shp', 'Salzburg Radwege', 'ogr')

#If the layers can not be loaded an error message is printed. Maybe not necessary for our script, but in general its a good idea!
if not layer:
  print "Layer failed to load!Please stay calm and try to repeat the process!"
  
  
#On a large scale the bike paths layer looked like a red spot. Therefore we decided to set up scale-dependent layer visibility. The layer is only visible from 1:1 million to the maximum zoom level of the basemap. 
layer.toggleScaleBasedVisibility(True)
layer.setMinimumScale(22267.0)
layer.setMaximumScale(1000000.0)
QgsMapLayerRegistry.instance().addMapLayer(layer)

#The  bike paths layer is  added to the map layer registry.
QgsMapLayerRegistry.instance().addMapLayer(layer)

#Here the layers symbol list is accessed through the layers renderer object.
symbols = layer.rendererV2().symbols()

# The first symbol is referenced.
sym = symbols[0]

#Now the RGB color is set. We chose red for better visualisation.
sym.setColor(QColor.fromRgb(255,0,0))

#The width is changed to 1 so that the bike paths are vusualised a bit thicker.
sym.setWidth(1.0)

#The layer is repainted with the chosen color.
layer.triggerRepaint()

#Here we repeated the process described above for the Badestellen points. We chose blue als color.
QgsMapLayerRegistry.instance().addMapLayer(layer1)
symbols = layer1.rendererV2().symbols()
sym = symbols[0]
sym.setColor(QColor.fromRgb(0,0,255))
layer1.triggerRepaint()

#A loop is used to execute the buffer tool several times. The buffer size is added to the filename.
buffer_list = buffer_values.split(";")
for x in buffer_list:
 out = bufferresult[:-4] + str(x) + ".shp"
 outputs_QGISFIXEDDISTANCEBUFFER_1=processing.runalg('qgis:fixeddistancebuffer', SelectBadestellenLayer,x,5.0,False,out)
 layer1 = qgis.utils.iface.addVectorLayer(out, "buffer" + "_" + x, "ogr")
 


 
 
