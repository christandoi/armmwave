from multilayer import *
import seaborn as sns

"aesthetics - https://xkcd.com/color/rgb/"
sns.set()
sns.set_style("darkgrid")
sns.set_context("talk", font_scale=0.75)
sns.set_palette("bright")
c1 = sns.xkcd_rgb["pale red"]
c2 = sns.xkcd_rgb["light blue"]
c3 = sns.xkcd_rgb["aquamarine"]
c4 = sns.xkcd_rgb["light yellow"]
c5 = sns.xkcd_rgb["brownish grey"]

# ###Broadband plotting
# plt.figure(figsize=(20,10))
# plt.xlabel('Frequencies (GHz)')
# plt.ylabel('Transmittance')
# plt.xscale('log')
# plt.title(f'Multi-layer ARC Porex comparison - mean transmission at {transfreqlow}/{transfreqhigh} GHz (0-loss alumina)')

# #single layer plotting
# quicksingle(porex8, 1)
# quicksingle(zitex, 2)
# quicksingle(ro3003, 1)
# quicksingle(ro3006, 1)
# quicksingle(ro3035, 1)

# #multilayer plotting
# quickplot(ro3035, 1, ro3003, 0, zitex, 0)
# quickplot(ro3035, 1, ro3003, 0, porex15, 0)
# quickplot(ro3003, 1, porex28, 0, zitex, 0)
# quickplot(ro3035, 1, porex29, 0, zitex, 0)
# quickplot(ro3006, 4, ro3035, 4, pmr15, 1)
# quickplot(ro3006, 4, ro3035, 3, porex50, 1)
# quickplot(ro3006, 0, ro3035, 1, zitex, 0)
# quickplot(ro3006, 0, ro3035, 1, ro3003, 0)
# quickplot(ro3006, 0, ro3003, 1, porex45, 0)
# quickplot(ro3006, 2, ro3003, 1, zitex, 2)
# quickplot(ro3006, 2, porex, 2, zitex, 0)

# ###Plot the CMB bands
# plt.xlim(10,400)
# plt.axvspan(25.5, 34.5, color='black', alpha=0.1)
# plt.annotate('30', xy=(30,0.5))
# plt.axvspan(34, 46, color='black', alpha=0.2)
# plt.annotate('40', xy=(40,0.5))
# plt.axvspan(95*.85, 95*1.15, color='purple', alpha=0.2)
# plt.annotate('95', xy=(95,0.5))
# plt.axvspan(150*.85, 150*1.15, color='pink', alpha=0.7)
# plt.annotate('150', xy=(150,0.5))
# plt.axvspan(220*.85, 220*1.15, color='green', alpha=0.2)
# plt.annotate('220', xy=(220,0.5))
# plt.axvspan(270*.85, 270*1.15, color='brown', alpha=0.2)
# plt.annotate('270', xy=(270,0.5))
# plt.ylim(0,1)
# plt.legend(loc='lower left')
# plt.show()

####multimean plotting (to figure out what to plot in quickplot)
fig = plt.figure(figsize=(15,10))
plt.title(f'Transmission of multi layer AR coating as function of total amount of layers at {transfreqlow}/{transfreqhigh} GHz (0-loss alumina)')
plt.ylabel('Mean transmission (%)')
plt.xlabel('Amount of physical layers')
multimean(ro3003, pmr15, zitex, 4)
multimean(ro3035, ro3003, zitex, 4)
multimean(ro3035, ro3003, pmr15, 4)
multimean(ro3035, pmr15, zitex, 4)
multimean(rod5880, pmr15, zitex, 4)
multimean(rod5880, ro3003, zitex, 4)
multimean(rod5880, ro3003, pmr15, 4)
multimean(rod5880, ro3035, zitex, 4)
multimean(rod5880, ro3035, pmr15, 4)
multimean(rod5880, ro3035, ro3003, 4)
multimean(ro3006, rod5880, pmr15, 4)
multimean(ro3006, rod5880, ro3035, 4)
multimean(ro3006, rod5880, ro3003, 4)
multimean(ro3006, rod5880, zitex, 4)
multimean(ro3006, ro3035, pmr15, 4)
multimean(ro3006, ro3035, zitex, 4)
multimean(ro3006, ro3035, ro3003, 4)
multimean(ro3006, ro3003, pmr15, 4)
multimean(ro3006, ro3003, zitex, 4)
multimean(ro3006, pmr15, zitex, 4)
plt.legend()
plt.show()

# #crunchnsave a ton of stuff at once
# #entire list is below
# crunchNsave(ro3003, pmr15, zitex)
# crunchNsave(ro3035, ro3003, zitex)
# crunchNsave(ro3035, ro3003, pmr15)
# crunchNsave(ro3035, pmr15, zitex)
# crunchNsave(rod5880, pmr15, zitex)
# crunchNsave(rod5880, ro3003, zitex)
# crunchNsave(rod5880, ro3003, pmr15)
# crunchNsave(rod5880, ro3035, zitex)
# crunchNsave(rod5880, ro3035, pmr15)
# crunchNsave(rod5880, ro3035, ro3003)
# crunchNsave(ro3006, rod5880, pmr15)
# crunchNsave(ro3006, rod5880, ro3035)
# crunchNsave(ro3006, rod5880, ro3003)
# crunchNsave(ro3006, rod5880, zitex)
# crunchNsave(ro3006, ro3035, pmr15)
# crunchNsave(ro3006, ro3035, zitex)
# crunchNsave(ro3006, ro3035, ro3003)
# crunchNsave(ro3006, ro3003, pmr15)
# crunchNsave(ro3006, ro3003, zitex)
# crunchNsave(ro3006, pmr15, zitex)