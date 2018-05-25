import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import rc, cm
plt.rc('font', size = 14)
plt.rc('axes', lw = 3)

fig = plt.figure(figsize=(15, 10))
grid_total = gridspec.GridSpec(20, 18, wspace=0.0, hspace=0.1)
grilla_lab = gridspec.GridSpecFromSubplotSpec(10, 10, subplot_spec = grid_total[2:-2,0:11], wspace=0.2, hspace=0)
grilla_permanencia = gridspec.GridSpecFromSubplotSpec(10, 10, subplot_spec = grid_total[:6,12:], wspace=0.2, hspace=0)
grilla_distancia = gridspec.GridSpecFromSubplotSpec(10, 10, subplot_spec = grid_total[7:13,12:], wspace=0.2, hspace=0)
grilla_velocidad = gridspec.GridSpecFromSubplotSpec(10, 10, subplot_spec = grid_total[14:,12:], wspace=0.2, hspace=0)

def dist_1 (x1, x2):
    return (np.abs(x1[0] -x2[0]) + np.abs(x1[1] -x2[1]))

def dist_2 (x1, x2):
    return np.sqrt((x1[0] -x2[0])**2 + (x1[1] -x2[1])**2)

poli = np.loadtxt('poli')
tray = np.loadtxt('trayectoria')

dist_px = np.loadtxt('distancia') #largo del maze en pixeles
dist_cm = 28.2 #largo del maze en centimetros
dist_conv = dist_cm / dist_px

fps = 1 #frames por segundo

tray[1] = 480 - tray[1]

################## POLIGONO ########################
x_poli = np.array([poli[i][0] for i in range(len(poli))])
y_poli = np.array([480-poli[i][1] for i in range(len(poli))])

indx_centro = np.where((np.abs(x_poli - 320)<100))[0]
xc, yc = np.mean(x_poli[indx_centro]), np.mean(y_poli[indx_centro])
radio_centro = 2*np.mean([np.abs(x_poli[indx_centro] - xc), np.abs(y_poli[indx_centro] - yc)])

ax1 = plt.subplot(grilla_lab[:,:])

ax1.plot(x_poli[np.r_[indx_centro, indx_centro[0]]], y_poli[np.r_[indx_centro, indx_centro[0]]], '--k', lw = 1.)
#ax1.plot(xc, yc, '.k', ms = 5)
ax1.plot(np.r_[x_poli, x_poli[0]], np.r_[y_poli, y_poli[0]], 'k')

ax1.plot(tray[0], tray[1], '.k', ms = 2)
ax1.plot(tray[0], tray[1], 'k', lw = 0.5)

lugares = ['A', 'B', 'C', 'D', 'E']
texto = [(40,460), (450, 460), (390, 30), (0, 30)]
[ax1.text(texto[i][0], texto[i][1], lugares[i], fontsize = 22) for i in range(4)]

ax1.axis('off')

################## TRAYECTORIA ########################
permanencia = np.zeros(5)
visitas = [np.array([]) for i in range(5)]
distancias = [dist_2(tray[:,i], tray[:,i+1]) for i in range(len(tray[0])-1)]
distancias = np.array(distancias) * dist_conv
dist_region = np.zeros(5)

flag = 48 #ninguna region, se cae si el flag esta en la misma region que la arana.

colores = np.array([(0, 51, 102), (102, 0, 51), (102, 51, 0), (0, 53, 26), (0,0,0)]) /256.

def en_region(region, flag, i):
    ax1.plot(tray[0][i], tray[1][i], '.', color = colores[region], ms = 7)
    permanencia[region] +=1
    dist_region[region]+= distancias[i]
    if (flag == region):
        visitas[region][-1] +=1
    else:
        visitas[region] = np.append(visitas[region], [1])
    return [region, permanencia, visitas]


for i in range(len(tray[0])-1):
    pto = tray[:,i]
    if (dist_1(pto, (xc, yc)) < radio_centro):
        [flag, permanencia, visitas] = en_region(4, flag, i)
    elif ((pto[0] < xc)&(pto[1] > yc)):
        [flag, permanencia, visitas] = en_region(0, flag, i)
    elif ((pto[0] > xc)&(pto[1] > yc)):
        [flag, permanencia, visitas] = en_region(1, flag, i)
    elif ((pto[0] > xc)&(pto[1] < yc)):
        [flag, permanencia, visitas] = en_region(2, flag, i)
    elif ((pto[0] < xc)&(pto[1] < yc)):
        [flag, permanencia, visitas] = en_region(3, flag, i)

permanencia_porcentaje = permanencia /float(len(tray[0])) *100

x_bar = np.arange(4)-0.5
ax2 = plt.subplot(grilla_permanencia[:, 2:])
perm = ax2.bar(x_bar, permanencia_porcentaje[0:4], width = 0.80, color = 'k')
[perm[i].set_color(colores[i]) for i in range(4)]
ax2.set_xticks(np.arange(4)-0.1)
ax2.set_xlim(-0.6, 3.4)
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
[ax2.text(x_bar[i]+.4, permanencia_porcentaje[i] + 3, '%d'%len(visitas[i]), fontsize = 12, ha = 'center') for i in range(4)]
ax2.spines['left'].set_position(('axes', -0.02))
ax2.tick_params(axis='x', direction='out', width=2, length=2, color='k', labelsize=10, pad = 2)
ax2.set_xticklabels(lugares, fontsize = 15)
ax2.set_ylabel('Permanencia (%)')

ax3 = plt.subplot(grilla_distancia[:, 2:])
dist = ax3.bar(x_bar, dist_region[0:4], width = 0.80, color = 'k')
[dist[i].set_color(colores[i]) for i in range(4)]
ax3.set_xticks(np.arange(4)-0.1)
ax3.set_xlim(-0.6, 3.4)
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.xaxis.set_ticks_position('bottom')
ax3.yaxis.set_ticks_position('left')
ax3.spines['left'].set_position(('axes', -0.02))
ax3.tick_params(axis='x', direction='out', width=2, length=2, color='k', labelsize=10, pad = 2)
ax3.set_xticklabels(lugares, fontsize = 15)
ax3.set_ylabel('Distancia (cm)')

ax4 = plt.subplot(grilla_velocidad[:, 2:])
vel = ax4.bar(x_bar, (dist_region/(permanencia/fps))[0:4], width = 0.80, color = 'k')
[vel[i].set_color(colores[i]) for i in range(4)]
ax4.set_xticks(np.arange(4)-0.1)
ax4.set_xlim(-0.6, 3.4)
ax4.spines['right'].set_color('none')
ax4.spines['top'].set_color('none')
ax4.xaxis.set_ticks_position('bottom')
ax4.yaxis.set_ticks_position('left')
ax4.spines['left'].set_position(('axes', -0.02))
ax4.tick_params(axis='x', direction='out', width=2, length=2, color='k', labelsize=10, pad = 2)
ax4.set_xticklabels(lugares, fontsize = 15)
ax4.set_ylabel('Velocidad (cm/s)')

plt.savefig('analysis.png', dpi = 200)
#plt.show()

