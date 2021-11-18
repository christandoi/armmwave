from multilayer import *
# import seaborn as sns

# "aesthetics - https://xkcd.com/color/rgb/"
# sns.set()
# sns.set_style("darkgrid")
# sns.set_context("talk", font_scale=0.75)
# sns.set_palette("bright")
# c1 = sns.xkcd_rgb["pale red"]
# c2 = sns.xkcd_rgb["light blue"]
# c3 = sns.xkcd_rgb["aquamarine"]
# c4 = sns.xkcd_rgb["light yellow"]
# c5 = sns.xkcd_rgb["brownish grey"]


###Broadband plotting
plt.figure(figsize=(14,7))
plt.xlabel('Frequencies (GHz)')
plt.ylabel('Transmittance')
plt.xscale('log')
plt.title(f'Anti-reflective coating comparison - mean transmission at {transdesc} GHz \n \
     Substrate: {substrate.desc}, {substrate.tand} loss tangent, {round(substrate.thick,4)}m thick \
          Bonding: {bond.desc}, {bond.tand} loss tangent, {bond.thick/mil} mil thick')

# ###single layer plotting
# # quicksingle(zitex, 1)
# # quicksingle(pmr15, 1)
# # quicksingle(rod5880, 1)
# quicksingle(ro3003, 1)
# quicksingle(ro3035, 1)
# # quicksingle(ro3006, 1)

###multilayer plotting
# quickplot(ro3006, ro3035, ro3003, 2, 2, 4)
quickplot(ro3006, ro3035, pmr15, 4, 4, 3)
quickplot(ro3006, ro3035, zitex, 4, 3, 3)
quickplot(ro3006, ro3003, pmr15, 4, 3, 1)
quickplot(ro3006, ro3003, zitex, 4, 3, 3)
# quickplot(ro3006, pmr15, zitex, 1, 1, 1)
# quickplot(ro3035, ro3003, pmr15, 4, 4, 0)
# quickplot(ro3035, ro3003, zitex, 3, 4, 1)
# quickplot(ro3035, pmr15, zitex, 4, 0, 3)
# quickplot(ro3003, pmr15, zitex, 1, 0, 0)


## Plot the CMB bands
plt.xlim(startfreq, stopfreq)
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
plt.axvspan(850*.85, 850*1.15, color='cyan', alpha=0.2)
plt.annotate('850', xy=(850,0.5))
plt.ylim(0,1)
plt.legend(loc='lower left')
# plt.tight_layout()
plt.savefig(f'./plots/{transdesc}GHz_{substrate.desc}_{substrate.tand}-loss_{round(substrate.thick,4)}-thick.png')
plt.show()


#####################################################################################################


# ##multimean plotting (to figure out what to plot in quickplot)
# fig = plt.figure(figsize=(15,10))
# plt.title(f'Transmission of multi layer AR coating as function of total amount of layers at {transfreqlow}/{transfreqhigh} GHz (0-loss alumina)')
# plt.ylabel('Mean transmission (%)')
# plt.xlabel('Amount of physical layers')

# multimean(ro3006, ro3035, ro3003,3)
# multimean(ro3006, ro3035, pmr15,3)
# multimean(ro3006, ro3035, zitex,3)
# multimean(ro3006, ro3003, pmr15,3)
# multimean(ro3006, ro3003, zitex,3)
# multimean(ro3006, pmr15, zitex,3)

# multimean(ro3035, ro3003, pmr15,3)
# multimean(ro3035, ro3003, zitex,3)
# multimean(ro3035, pmr15, zitex,3)

# multimean(ro3003, pmr15, zitex,3)

# # plt.ylim(90,100)
# # plt.legend()
# plt.show()

# ##to make sure multimean is efficent
# all_layers_mean(ro3006, ro3035, ro3003)
# plt.show()
# all_layers_mean(ro3006, ro3035, pmr15)
# plt.show()
# all_layers_mean(ro3006, ro3035, zitex)
# plt.show()
# all_layers_mean(ro3006, ro3003, pmr15)
# plt.show()
# all_layers_mean(ro3006, ro3003, zitex)
# plt.show()
# all_layers_mean(ro3006, pmr15, zitex)
# plt.show()
# all_layers_mean(ro3035, ro3003, pmr15)
# plt.show()
# all_layers_mean(ro3035, ro3003, zitex)
# plt.show()
# all_layers_mean(ro3035, pmr15, zitex)
# plt.show()
# all_layers_mean(ro3003, pmr15, zitex)
# plt.show()

# i=1
# #crunchnsave a ton of stuff at once
# print(i)
# i+=1
# crunchNsave(ro3006,ro3035,ro3003,3)
# print(i)
# i+=1
# crunchNsave(ro3006,ro3035,pmr15,3)
# print(i)
# i+=1
# crunchNsave(ro3006,ro3035,zitex,3)
# print(i)
# i+=1
# crunchNsave(ro3006,ro3003,pmr15,3)
# print(i)
# i+=1
# crunchNsave(ro3006,ro3003,zitex,3)
# print(i)
# i+=1
# crunchNsave(ro3006,pmr15,zitex,3)
# print(i)
# i+=1

# crunchNsave(ro3035,ro3003,pmr15,3)
# print(i)
# i+=1
# crunchNsave(ro3035,ro3003,zitex,3)
# print(i)
# i+=1
# crunchNsave(ro3035,pmr15,zitex,3)
# print(i)
# i+=1

# crunchNsave(ro3003,pmr15,zitex,3)
# print(i)
# i+=1

# crunchNsave(ro3035)
# crunchNsave(ro3003)
# crunchNsave(ro3006)
# crunchNsave(pmr15)
# crunchNsave(zitex)