#CHRIS TANDOI - JANUARY 26, 2020
#   this script is for simulating multiple layers of anti reflective coating
#   and also to plot different things based on this data
#
#   TO DO: 
#   -consolidate arc and arcsingle into one function that is dynamic in how many
#       layers you can choose (and subsequently quickplot/quicksingle)
#   -clean up plotting (more)
#
####

import os
import armmwave.layer as awl
import armmwave.model as awm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#aesthetics - https://xkcd.com/color/rgb/
sns.set()
sns.set_style("darkgrid")
sns.set_context("talk")
sns.set_palette("bright")
# c1 = sns.xkcd_rgb["pale red"]
# c2 = sns.xkcd_rgb["light blue"]
# c3 = sns.xkcd_rgb["aquamarine"]
# c4 = sns.xkcd_rgb["light yellow"]
# c5 = sns.xkcd_rgb["brownish grey"]

#set the broadband frequency range for plotting
#(here is 10GHz to 400GHz)
frequencies = np.linspace(10, 400, 1000)
#and the frequency range we're interested in transmission for
#(here is 30/40GHz +/- 15%)
frequencylow = 30e9*.85
frequencyhigh = 40e9*1.15

#define your AR layers
zitex = awl.Layer(rind=1.2, tand=9e-4, thick=3.81e-4, desc='Zitex')
porex = awl.Layer(rind=1.319, tand=9e-4, thick=3.81e-4, desc='Porex')
ro3003 = awl.Layer(rind=1.732, tand=0.001, thick=1.27e-4, desc='RO3003')
ro3035 = awl.Layer(rind=1.897, tand=0.0015, thick=1.27e-4, desc='RO3035')
ro3006 = awl.Layer(rind=2.549, tand=0.002, thick=1.27e-4, desc='RO3006')

#specify a bonding layer
ldpe = awl.Layer(rind=1.5141, tand=2.7e-4, thick=2.54e-5, desc='LDPE')
bond = ldpe

#specify a substrate
alumina_lens = awl.Layer(rind=3.1, tand=9e-4, thick=2e-3, desc='Alumina lens')
substrate = alumina_lens

# choose up to 3 materials and the number of layers you want. bonding layers are
# automatically included along with the [bookkeeping layers] and <substrate>. visualization:
# [source]
# material2     <--amountoflayers2  #amountoflayers2 will give you X layers of material2 and bond
# bonding layer <--amountoflayers2
# material1     <--amountoflayers1  #same for amountoflayers1 wrt material1
# bonding layer <--amountoflayers1
# <alumina lens>
# [terminator]
# also choose an upper and lower bound for frequencies

#arc is for choosing a single configuration
def arc(material1, amountoflayers1, material2, amountoflayers2, material3, amountoflayers3, freqlow, freqhigh):
    layers = [awl.Source(),]
    for i in range(amountoflayers3):
        layers.append(material3)
        layers.append(bond)
    for j in range(amountoflayers2):
        layers.append(material2)
        layers.append(bond)
    for k in range(amountoflayers1):
        layers.append(material1)
        layers.append(bond)
    layers.append(substrate)
    layers.append(awl.Terminator(vac=False))
    model = awm.Model()
    model.set_freq_range(freq1=freqlow, freq2=freqhigh)
    model.set_up(layers)
    return model.run()

#arc_crunch is for going through every iteration of 0 to X layers for the materials specified
#and prints out which layers are currently being simulated
def arc_crunch(mat1, mat2, mat3, layers):
    mat1_mat2_mat3 = []
    for i in range(layers):
        for j in range(layers):
            for k in range(layers):
                mat1_mat2_mat3.append(arc(mat1, i, mat2, j, mat3, k, frequencylow, frequencyhigh)['transmittance'])
                print(f'{i} {j} {k}')
    return mat1_mat2_mat3

#crunchNsave will save your crunch to file (in /data/ directory) so you don't have to crunch more
#than once. can save time on lots of layers
def crunchNsave(mat1, mat2, mat3, layers):
    np.save(os.path.join('data', f'{mat1.desc}_{mat2.desc}_{mat3.desc}_{layers}'), arc_crunch(mat1, mat2, mat3, layers))

#inverse of crunchNsave: loads your saved crunch to a variable that you can call for
#analysis later
def loadmydata(mat1, mat2, mat3, layers):
    return np.load(f'{mat1.desc}_{mat2.desc}_{mat3.desc}_{layers}.npy')

#statistics setup for analysis
def arc_stats(crunched_model):
    mean = [round(np.mean(crunched_model[x])*100, 2) for x in range(len(crunched_model))]
    stddev = [round(np.std(crunched_model[x])*100, 2) for x in range(len(crunched_model))]
    location = range(len(crunched_model))
    return stddev, mean, location

#plotting function to include label
def quickplot(mat1, amount1, mat2, amount2, mat3, amount3, freqlow, freqhigh, linestyle):
    broadband = arc(mat1, amount1, mat2, amount2, mat3, amount3, freqlow, freqhigh)['transmittance']
    crunchrange = arc(mat1, amount1, mat2, amount2, mat3, amount3, frequencylow, frequencyhigh)['transmittance']
    label = f'{round(amount1 * mat1.thick * 39370)}mil {mat1.desc}, {round(amount2 * mat2.thick * 39370)}mil {mat2.desc}, {round(amount3 * mat3.thick * 39370)}mil {mat3.desc}, {round(np.mean(data)*100, 2)}% mean transmission'
    return plt.plot(frequencies, broadband, label=label, ls=linestyle)

#arc crunch for only single layer of material
def arcsingle(material, amountoflayers, freqlow, freqhigh):
    layers = [awl.Source(),]
    for number in range(amountoflayers):
        layers.append(material)
        layers.append(bond)
    layers.append(substrate)
    layers.append(awl.Terminator(vac=False))
    model = awm.Model()
    model.set_freq_range(freq1=freqlow, freq2=freqhigh)
    model.set_up(layers)
    return model.run()

#plotting for arcsingle
#broadband is for the overall picture (here: 10 to 400GHz)
#crunchrange is the specific brand we care about (here: 30/40GHz)
def quicksingle(mat, amount, freqlow=10e9, freqhigh=400e9, ls='-'):
    broadband = arcsingle(mat, amount, freqlow, freqhigh)['transmittance']
    crunchrange = arcsingle(mat, amount, frequencylow, frequencyhigh)['transmittance']
    label = f'{round(amount * mat.thick * 39370)}mil {mat.desc}, {round(np.mean(crunchrange)*100, 2)}% transmission'
    return plt.plot(frequencies, broadband, label=label, linestyle=ls)

#####Broadband plotting
plt.figure(figsize=(20,10))
plt.xlabel('Frequencies (GHz)')
plt.ylabel('Transmittance')
plt.xscale('log')
plt.title('Single layer ARC - mean transmission at 30/40GHz')
quicksingle(porex, 4)
quicksingle(zitex, 4)
quicksingle(ro3003, 8)
quicksingle(ro3006, 5)
quicksingle(ro3035, 7)
# quickplot(ro3006, 5, ro3035, 3, porex, 3, 10e9, 400e9)
# quickplot(ro3006, 4, ro3035, 4, porex, 3, 10e9, 400e9)
# quickplot(ro3006, 4, ro3035, 3, porex, 3, 10e9, 400e9)
# quickplot(ro3006, 6, porex, 2, ro3035, 3, 10e9, 400e9)
# quickplot(ro3006, 3, ro3035, 5, zitex, 3, 10e9, 400e9)
plt.xlim(10,400)
plt.axvspan(25.5, 34.5, color='black', alpha=0.1)
plt.annotate('30', xy=(30,0.5))
plt.axvspan(34, 46, color='black', alpha=0.2)
plt.annotate('40', xy=(40,0.5))
plt.axvspan(95*.85, 95*1.15, color='purple', alpha=0.2)
plt.annotate('95', xy=(95,0.5))
plt.axvspan(150*.85, 150*1.15, color='pink', alpha=0.7)
plt.annotate('150', xy=(150,0.5))
plt.axvspan(220*.85, 220*1.15, color='green', alpha=0.2)
plt.annotate('220', xy=(220,0.5))
plt.axvspan(270*.85, 270*1.15, color='brown', alpha=0.2)
plt.annotate('270', xy=(270,0.5))
plt.ylim(0,1)
plt.legend()
plt.show()