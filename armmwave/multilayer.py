"""CHRIS TANDOI - APRIL 5, 2020
    this script is for simulating multiple layers of anti reflective coating
    and also to plot different things based on this data (multilayer_plotting.py)

    TO DO: 
    -consolidate arc and arcsingle into one function that is dynamic in how many
        layers you can choose (and subsequently quickplot/quicksingle)
    -better analysis for extracting less layers out of a bigger layer crunchNsave?
    (change loadmydata to truncate from a fixed file size (6 layers?) to whatever size you need)
    -get annotation working
    -write function for varying porex thickness
    -more crunchNsave: pass low/high frequencies so i can crunchnsave different frequencies at once
    -is multimean good? it's only showing the highest transmission, what if there's a lower
        transmission (0.1%) but much thinner (5 layers?)
    -probably unnecessary: change crunching to choose your range of layers. thought came up because 
        what if you already crunched 4 layers of some recipe but want to find out the 5th, 6th layers etc.
        without redoing the first 4?

"""

import os
import matplotlib.pyplot as plt
import armmwave.layer as awl
import armmwave.model as awm
import numpy as np

"set the broadband frequency range for plotting, GHz"
startfreq = 100
stopfreq = 2000
steps = 2000
frequencies = np.linspace(startfreq, stopfreq, steps)
"and the frequency range in GHz we're interested in transmission for"
transfreqlow = 850
transfreqhigh = 850

#for plotting purposes
if transfreqlow == transfreqhigh:
    transdesc = f'{transfreqlow}'
else:
    transdesc = f'{transfreqlow}/{transfreqhigh}'

"don't change these below. accounts for the +/- 15% range in wavelengths and converts Hz to GHz"
adjtransfreqlow = transfreqlow*(10**9)*.85
adjtransfreqhigh = transfreqhigh*(10**9)*1.15

"define your AR layers"
mil = 2.54e-5 #converting 1 thousandth of an inch to meters
zitex = awl.Layer(rind=1.2, tand=9e-4, thick=mil*15, desc='Zitex')
pmr15 = awl.Layer(rind=1.304, tand=9e-4, thick=mil*59, desc='PMR15') #59mil = 1.5mm
rod5880 = awl.Layer(rind=1.414, tand=0.0021, thick=mil*10, desc='5880LZ')
ro3003 = awl.Layer(rind=1.732, tand=0.001, thick=mil*5, desc='RO3003')
ro3035 = awl.Layer(rind=1.897, tand=0.0015, thick=mil*5, desc='RO3035')
ro3006 = awl.Layer(rind=2.549, tand=0.002, thick=mil*5, desc='RO3006')

"porex can be made in arbitrary thicknesses, so this is a garbage placeholder until i write a function to vary it"
porex = awl.Layer(rind=1.319, tand=9e-4, thick=mil*15, desc='PM23J') #note: discontinued? (too expensive for custom?)
porex8 = awl.Layer(rind=1.319, tand=9e-4, thick=mil*8, desc='Porex')
porex15 = awl.Layer(rind=1.319, tand=9e-4, thick=mil*15, desc='Porex')
porex28 = awl.Layer(rind=1.319, tand=9e-4, thick=mil*28, desc='Porex')
porex29 = awl.Layer(rind=1.319, tand=9e-4, thick=mil*29, desc='Porex')
porex30 = awl.Layer(rind=1.319, tand=9e-4, thick=mil*30, desc='Porex')
porex45 = awl.Layer(rind=1.319, tand=9e-4, thick=mil*45, desc='Porex')
porex50 = awl.Layer(rind=1.319, tand=9e-4, thick=mil*50, desc='PM23J')
porex60 = awl.Layer(rind=1.319, tand=9e-4, thick=mil*60, desc='Porex')

"specify a bonding layer"
ldpe = awl.Layer(rind=1.5141, tand=2.7e-4, thick=mil*1, desc='LDPE')

bond = ldpe

"specify a substrate"
alumina_lens = awl.Layer(rind=3.1, tand=1e-3, thick=mil*0, desc='Alumina lens')
silicon300k = awl.Layer(rind=3.4155, tand=6e-4, thick=0.01, desc='Silicon, 300K')
silicon1p5k = awl.Layer(rind=3.3818, tand=1.6e-4, thick=0.01, desc='Silicon, 1.5K')

substrate = silicon1p5k

"""choose up to 3 materials and the number of layers you want. bonding layers are
automatically included along with the [bookkeeping layers] and <substrate>. visualization:
[source]
material2     <--amountoflayers2  #amountoflayers2 will give you X layers of material2 and bond
bonding layer <--amountoflayers2
material1     <--amountoflayers1  #same for amountoflayers1 wrt material1
bonding layer <--amountoflayers1
<alumina lens>
[terminator]
also choose an upper and lower bound for frequencies"""

"arc is for choosing a single configuration"
def arc(material1, material2, material3, amountoflayers1, amountoflayers2, amountoflayers3, freqlow, freqhigh):
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
    model.set_freq_range(freq1=freqlow, freq2=freqhigh, nsample=steps)
    model.set_up(layers)
    return model.run()

"""arc_crunch is for going through every iteration of 0 to X layers for the materials specified
and prints out which layers are currently being simulated"""
def arc_crunch(mat1, mat2, mat3, layers):
    mat1_mat2_mat3 = []
    for i in range(layers+1):
        for j in range(layers+1):
            for k in range(layers+1):
                mat1_mat2_mat3.append(arc(mat1, mat2, mat3, i, j, k, adjtransfreqlow, adjtransfreqhigh)['transmittance'])
                print(f'{i} {j} {k}')
    return mat1_mat2_mat3

"""crunchNsave will save your crunch to file (in /data/ directory) so you don't have to crunch more than once
note: only crunches for the frequency band you're interested in (e.g. 30/40 or 220/270) that you specify at the top"""
def crunchNsave(mat1, mat2, mat3, layers=4):
    np.save(os.path.join('data', f'{mat1.desc}_{mat2.desc}_{mat3.desc}_{layers}_{transfreqlow}_{transfreqhigh}_{substrate.desc}_{substrate.tand}_{substrate.thick}'), arc_crunch(mat1, mat2, mat3, layers))

"inverse of crunchNsave: loads your saved crunch to a variable that you can call for analysis later"
def loadmydata(mat1, mat2, mat3, layers=4):
    return np.load(os.path.normpath(os.path.join('data', f'{mat1.desc}_{mat2.desc}_{mat3.desc}_{layers}_{transfreqlow}_{transfreqhigh}_{substrate.desc}_{substrate.tand}_{substrate.thick}.npy')))

"statistics setup for analysis"
def arc_stats(crunched_model):
    stddev = [round(np.std(crunched_model[x])*100, 2) for x in range(len(crunched_model))]
    mean = [round(np.mean(crunched_model[x])*100, 2) for x in range(len(crunched_model))]
    location = range(len(crunched_model))
    return stddev, mean, location

"plotting function to include label"
def quickplot(mat1, mat2, mat3, amount1, amount2, amount3, freqlow=10e9, freqhigh=400e9, ls='-'):
    broadband = arc(mat1, mat2, mat3, amount1, amount2, amount3, freqlow, freqhigh)['transmittance']
    crunchrange = arc(mat1, mat2, mat3, amount1, amount2, amount3, adjtransfreqlow, adjtransfreqhigh)['transmittance']
    label = f'{round(amount1 * mat1.thick * 39370)}mil {mat1.desc}, {round(amount2 * mat2.thick * 39370)}mil {mat2.desc}, {round(amount3 * mat3.thick * 39370)}mil {mat3.desc}, {round(np.mean(crunchrange)*100, 2)}% transmission'
    return plt.plot(frequencies, broadband, label=label, linestyle=ls)

"arc crunch for only single layer of material"
def arcsingle(material, amountoflayers, freqlow, freqhigh):
    layers = [awl.Source(),]
    for number in range(amountoflayers):
        layers.append(material)
        layers.append(bond)
    layers.append(substrate)
    layers.append(awl.Terminator(vac=False))
    model = awm.Model()
    model.set_freq_range(freq1=freqlow, freq2=freqhigh, nsample=steps)
    model.set_up(layers)
    return model.run()

"""plotting for arcsingle
broadband is for the overall picture (here: 10 to 400GHz)
crunchrange is the specific brand we care about (here: 30/40GHz)"""
def quicksingle(mat, amount, freqlow=10e9, freqhigh=400e9, ls='-'):
    broadband = arcsingle(mat, amount, freqlow, freqhigh)['transmittance']
    crunchrange = arcsingle(mat, amount, adjtransfreqlow, adjtransfreqhigh)['transmittance']
    label = f'{round(amount * mat.thick * 39370)}mil {mat.desc}, {round(np.mean(crunchrange)*100, 2)}% transmission'
    return plt.plot(frequencies, broadband, label=label, linestyle=ls)

"""for plotting the maximum mean transmission value for each combination of layers
i.e.: best transmission at 1 layer of material, 2 layers, 3 layers, 4, 5, 6, etc."""
def multimean(mat1, mat2, mat3, layers=4):
    file = loadmydata(mat1, mat2, mat3, layers=4)
    mean = arc_stats(file)[1]
    location = arc_stats(file)[2]
    base5loc = []
    "convert location to base 5 (or however many layers you choose, just adjust) for actual amount of layer values"
    for place in location:
        base5loc.append(np.base_repr(place,5))
    "add up each amount layers (i.e. 304 = 3 + 0 + 4 = 7)"
    total_layers = []
    for amountoflayers in base5loc:
        total_layers.append(sum(int(x) for x in amountoflayers))
    # total_layers_dict = dict(zip(mean, total_layers))
    max_pos = mean.index(max(mean))
    label = f'{mat1.desc}_{mat2.desc}_{mat3.desc}_{base5loc[max_pos]}'
    plotting = plt.scatter(total_layers[max_pos], mean[max_pos], label=label, alpha=1)
    return plotting

"""for plotting every mean value for each layer combination of a specific recipe"""
def all_layers_mean(mat1, mat2, mat3, layers=4):
    file = loadmydata(mat1, mat2, mat3, layers=4)
    mean = arc_stats(file)[1]
    location = arc_stats(file)[2]
    base5loc = []
    "convert location to base 5 (or however many layers you choose, just adjust) for actual amount of layer values"
    for place in location:
        base5loc.append(np.base_repr(place,5))
    "add up each amount layers (i.e. 304 = 3 + 0 + 4 = 7)"
    total_layers = []
    for amountoflayers in base5loc:
        total_layers.append(sum(int(x) for x in amountoflayers))
    ### need to annotate each individual point?
    # labels = []
    # for configuration in range(len(mean)):
    #     labels.append(f'{mat1.desc}_{mat2.desc}_{mat3.desc}_{base5loc[configuration]}')
    label = f'{mat1.desc}_{mat2.desc}_{mat3.desc}'
    plotting = plt.scatter(total_layers, mean, label=label, alpha=1)
    return plotting

"placeholder for annotation function"
# def annotation(file):
#     for i in arc_stats(ro3006_ro3003_zitex)[2]:
#         plt.annotate(np.base_repr(i,5), (arc_stats(ro3006_ro3003_zitex)[0][i], arc_stats(ro3006_ro3003_zitex)[1][i]))