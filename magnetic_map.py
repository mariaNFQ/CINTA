# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:41:54 2017

@author: Maria.Ramirez
"""
# REVISAR COMO SE HACE ESTO EN PYTHON
if nargin ~= 2:
    [mag_data] = load_mag_map
    loc_pointer = 4
    
import panda as pd
import matplotlib import pyplot as plt
import math
from PIL import Image


datos = pd.read_excel('mag_data.xls', header=0, delim_whitespace=True) # archivo está en el mismo directorio del script y 
# suponemos que el separador del fichero es un espacio en blanco en todo el archivo

Num = datos.ix[:,0]
Day = datos.ix[:,1]                     
Mon = datos.ix[:,2]            
Yea = datos.ix[:,3]
Hou = datos.ix[:,4]
Min = datos.ix[:,5]
Sec = datos.ix[:,6]
Lon = datos.ix[:,7]
Lat = datos.ix[:,8]
Alt = datos.ix[:,9]
Hea_GPS = datos.ix[:,10]
Pit_GPS = datos.ix[:,11]
Rol_GPS = datos.ix[:,12]
Bx0 = datos.ix[:,13]
By0 = datos.ix[:,14]
Bz0 = datos.ix[:,15]
H0 = datos.ix[:,16]
F0 = datos.ix[:,17]
Bx1 = datos.ix[:,18]
By1 = datos.ix[:,19]
Bz1 = datos.ix[:,20]
H1 = datos.ix[:,21]
F1 = datos.ix[:,22]

## GRAPHICS: HEADING + F (MAGNETIC FIELD STRENGTH) 

plt.ion()
plt.figure('Heading vs. Magnetic Field Strength, (N(0º), W(90º), S(180º), E(270º))')
plt.plot(Num, Heading, linestyle='-', color='b', label='Heading')
plt.xlabel('Num')
plt.ylabel('ax(1), Heading (º)')

plt.twinx()

plt.plot(Num, F0, marker='o', linestyle='-', color='', label='$\F_0')
plt.hold()
plt.plot(Num, F1, marker='o', linestyle='-', color='', label='$\F_1')
plt.ylabel('ax(2), Magnetic Field Strength (uT)')

plt.legend()


# GEOMAGNETIC MODEL

# Falta por implementar una forma automática para calcular el modelo magnético a partir de Lon,Lat,Alt.
# Mientras tanto se trabaja con los valores específicos de cada ejemplo 

if loc_pointer == 1:
    # Values in uT
    By = (1.5958) * ones(size(By0))
    Bx = (18.9423) * ones(size(Bx0))
    Bz = (-17.5769) * ones(size(Bz0))
    H = (19.0094) * ones(size(H0))
    F = (25.8903) * ones(size(F0))
    
elif loc_pointer == 2:
    # Values in uT
    By = (1.6322) * ones(size(By0))
    Bx = (18.9923) * ones(size(Bx0))
    Bz = (-17.3671) * ones(size(Bz0))
    H = (19.0623) * ones(size(H0))
    F = (25.7874) * ones(size(F0))

    imagegame = 'grafica.png' # Revisar como se hace esto el python, NO LO ENTIENDO
    x_axis_graph_min = -67.962576
    x_axis_graph_max = -67.886015
    y_axis_graph_min = -42.322173
    y_axis_graph_max = -42.272654
    
elif loc_pointer == 3:
    # Values in uT
    By = (4.2155) * ones(size(By0))
    Bx = (19.6764) * ones(size(Bx0))
    Bz = (-23.1593) * ones(size(Bz0))
    H = (20.1229) * ones(size(H0))
    F = (30.6804) * ones(size(F0))

    imagegame = 'Pali Aike vlarge.png' # Revisar como se hace esto el python, NO LO ENTIENDO
    x_axis_graph_min = -69.717856
    x_axis_graph_max = -69.700818
    y_axis_graph_min = -52.120662
    y_axis_graph_max = -52.109647

elif loc_pointer == 4
    # Values in uT
    By = (1.6006 - 0.0503*5) * ones(size(By0))
    Bx = (19.2960 - 0.0612*5) * ones(size(Bx0))
    Bz = (-16.0382 + 0.0148*5) * ones(size(Bz0))
    H = (19.3622 - 0.0651*5) * ones(size(H0))
    F = (25.1420 - 0.0595*5) * ones(size(F0))

    imagegame = 'Barda Negra large.png' # Revisar como se hace esto el python, NO LO ENTIENDO
    x_axis_graph_min = -69.900225
    x_axis_graph_max = -69.859885
    y_axis_graph_min = -39.193524
    y_axis_graph_max = -39.163317
    
elif loc_pointer == 5:
    # Values in uT
    By = (1.6156 - 0.0468*5) * ones(size(By0))
    Bx = (18.9796 - 0.0624*5) * ones(size(Bx0))
    Bz = (-17.3628 + 0.0172*5) * ones(size(Bz0))
    H = (19.0482 - 0.0661*5) * ones(size(H0))
    F = (25.7740 - 0.0605*5) * ones(size(F0))

    imagegame = 'Bajo Honda.png' # Revisar como se hace esto el python, NO LO ENTIENDO
    x_axis_graph_min = -67.962576
    x_axis_graph_max = -67.886015
    y_axis_graph_min = -42.322173
    y_axis_graph_max = -42.272654
    
# Magnetic Field Measured - Magnetic Field Model    
    Bx0_b = Bx0 - Bx
    By0_b = By0 - By
    Bz0_b = Bz0 - Bz
    H0_b = math.sqrt(Bx0_b**2 + By0_b**2)
    F0_b = math.sqrt(Bx0_b**2 + By0_b**2 + Bz0_b**2)
    
    Bx1_b = Bx1 - Bx
    By1_b = By1 - By
    Bz1_b = Bz1 - Bz
    H1_b = math.sqrt(Bx1_b**2 + By1_b**2)
    F1_b = math.sqrt(Bx1_b**2 + By1_b**2 + Bz1_b**2)    
    
## GRAPHICS: MAGNETIC FIELD WITH GEOMAGNETIC MODEL

plt.figure('Magnetic Field Components')
plt.subplot(3, 1, 1)
plt.plot((Bx0, Bx1, Bx))
plt.ylabel('North (uT)')
legend('$\B_x_0', '$\B_x_1', '$\B_x')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot((By0, By1, By))
plt.ylabel('East (uT)')
legend('$\B_y_0', '$\B_y_1', '$\B_y')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot((Bz0, Bz1, Bz))
plt.ylabel('Vertical (down) (uT)')
legend('$\B_z_0', '$\B_z_1', '$\B_z')
plt.grid()

plt.figure('Magnetic Field Strength: Horizontal and Total')
plt.subplot(2, 1, 1)
plt.plot((H0, H1, H))
plt.ylabel('Horizontal Strength (uT)')
legend('$\H_0', '$\H_1', 'H model')
plt.hold()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot((F0, F1, F))
plt.ylabel('Total Strength (uT)')
legend('$\F_0', '$\F_1', 'F model')
plt.grid()


## GRAPHICS: MAGNETIC FIELD MINUS GEOMAGNETIC MODEL
plt.figure('Magnetic Field Components - Anomaly')
plt.subplot(3, 1, 1)
plt.plot((Bx0_b, Bx1_b))
plt.ylabel('North (uT)')
plt.grid()
legend('$\B_x_0 anomaly', '$\B_x_1 anomaly')

plt.subplot(3, 1, 2)
plt.plot((By0_b, By1_b))
plt.ylabel('East (uT)')
plt.grid()
legend('$\B_y_0 anomaly', '$\B_y_1 anomaly')

plt.subplot(3, 1, 3)
plt.plot((Bz0_b, Bz1_b))
plt.ylabel('Vertical (down) (uT)')
plt.grid()
legend('$\B_z_0 anomaly', '$\B_z_1 anomaly')


plt.figure('Magnetic Field Strength: Horizontrtal and Total - Anomaly')
plt.subplot(2, 1, 1)
plt.plot((H0_b, H1_b))
plt.ylabel('Horizontal Strength (uT)')
plt.hold()
plt.grid()
legend('$\H_0 anomaly', '$\H_1 anomaly')

plt.subplot(2, 1, 2)
plt.plot((F0_b, F1_b))
plt.ylabel('Total Strength (uT)')
plt.hold()
plt.grid()
legend('$\F_0 anomaly', '$\F_1 anomaly')

## GRAPH: MEASUREMENTS OVER MAP - SCATTER

img_directory= '' # mirar como se pone un path en Python

# INTENSIDAD TOTAL 

min_F0 = min(F0)
min_F1 = min(F1)
min_F = min(min_F0, min_F1)
max_F0 = max(F0)
max_F1 = max(F1)
max_F = max(max_F0)

plt.figure()
plt.subplot(2, 1, 1)
img = 
plt.hold() 
plt.grid()