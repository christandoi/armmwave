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

###Broadband plotting
plt.figure(figsize=(20,10))
plt.xlabel('Frequencies (GHz)')
plt.ylabel('Transmittance')
plt.xscale('log')
plt.title('Single and Multi-layer ARC - mean transmission at 30/40GHz')

quicksingle(porex60, 1)
quicksingle(zitex, 4)
quicksingle(ro3003, 8)
quicksingle(ro3006, 5)
quicksingle(ro3035, 7)

quickplot(ro3035, 4, ro3003, 3, zitex, 2)
quickplot(ro3035, 4, ro3003, 3, porex15, 1)
quickplot(ro3003, 4, porex28, 1, zitex, 1)
quickplot(ro3035, 4, porex29, 1, zitex, 1)
quickplot(ro3006, 4, ro3035, 3, porex50, 1)
quickplot(ro3006, 4, ro3035, 4, zitex, 4)
quickplot(ro3006, 4, ro3035, 4, ro3003, 4)
quickplot(ro3006, 4, ro3003, 3, porex45, 1)
quickplot(ro3006, 4, ro3003, 4, zitex, 3)
quickplot(ro3006, 4, porex45, 1, zitex, 1)

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

# ####multimean plotting
# fig = plt.figure(figsize=(15,10))
# # ax = fig.gca()
# # ax.set_xticks(np.arange(0, 130, 1))
# plt.title('Transmission of multi layer AR coating as function of total amount of layers')
# plt.ylabel('Mean transmission (%)')
# plt.xlabel('Amount of physical layers')
# multimean(ro3035, ro3003, zitex, 4)
# multimean(ro3035, ro3003, porex, 4)
# multimean(ro3035, porex, zitex, 4)
# multimean(ro3003, porex, zitex, 4)
# multimean(ro3006, ro3035, porex, 4)
# multimean(ro3006, ro3035, zitex, 4)
# multimean(ro3006, ro3035, ro3003, 4)
# multimean(ro3006, ro3003, porex, 4)
# multimean(ro3006, ro3003, zitex, 4)
# multimean(ro3006, porex, zitex, 4)
# # plt.grid()
# plt.legend()
# plt.show()


###old vvvv

# #open your files
# RO3035_RO3003_Zitex = np.load(os.path.normpath(os.path.join('data', 'RO3035_RO3003_Zitex_4.npy')))
# RO3035_RO3003_Zitex = np.load(os.path.normpath(os.path.join('data', 'RO3035_RO3003_Porex_4.npy')))
# RO3035_Porex_Zitex = np.load(os.path.normpath(os.path.join('data', 'RO3035_Porex_Zitex_4.npy')))
# RO3006_RO3035_zitex = np.load(os.path.normpath(os.path.join('data', 'RO3006_RO3035_Zitex_4.npy')))
# RO3006_RO3035_RO3003 = np.load(os.path.normpath(os.path.join('data', 'RO3006_RO3035_RO3003_4.npy')))
# RO3006_RO3035_Porex = np.load(os.path.normpath(os.path.join('data', 'RO3006_RO3035_Porex_4.npy')))
# RO3006_RO3003_Zitex = np.load(os.path.normpath(os.path.join('data', 'RO3006_RO3003_Zitex_4.npy')))
# RO3006_RO3003_Porex = np.load(os.path.normpath(os.path.join('data', 'RO3006_RO3003_Porex_4.npy')))
# RO3006_Porex_Zitex = np.load(os.path.normpath(os.path.join('data', 'RO3006_Porex_Zitex_4.npy')))
# RO3003_Porex_Zitex = np.load(os.path.normpath(os.path.join('data', 'RO3003_Porex_Zitex_4.npy')))

# # ro3035_ro3003_zitex = np.load('3035_3003_zitex.npy')
# # ro3035_ro3003_porex = np.load('3035_3003_porex.npy')
# # ro3003_porex_zitex = np.load('3003_porex_zitex.npy')
# # ro3006_ro3003_porex = np.load('3006_3003_porex.npy')
# # ro3006_ro3035_ro3003 = np.load('3006_3035_ro3003.npy')
# # ro3006_ro3035_porex_2 = np.load('3006_3035_porex_2.npy')
# # ro3006_ro3035_zitex_2 = np.load('3006_3035_zitex_2.npy')
# # ro3006_porex_zitex = np.load('3006_porex_zitex.npy')
# # ro3006_ro3003_zitex = np.load('3006_3003_zitex.npy')

# #plot some stuff
# plt.figure(figsize=(18,8))
# plt.title('Transmission of multi layer AR coating')
# plt.ylabel('Mean transmission')
# plt.xlabel('Standard Deviation')
# # plt.ylim(95,100)
# # plt.xlim(0,2)
# plt.scatter(arc_stats(RO3035_RO3003_Zitex)[2], arc_stats(RO3035_RO3003_Zitex)[1], label='RO3035_RO3003_Zitex_4', alpha=0.5)
# plt.scatter(arc_stats(RO3035_RO3003_Zitex)[2], arc_stats(RO3035_RO3003_Zitex)[1], label='RO3035_RO3003_Zitex_4', alpha=0.5)
# plt.scatter(arc_stats(RO3035_Porex_Zitex)[2], arc_stats(RO3035_Porex_Zitex)[1], label='RO3035_Porex_Zitex_4', alpha=0.5)
# plt.scatter(arc_stats(RO3006_RO3035_zitex)[2], arc_stats(RO3006_RO3035_zitex)[1], label='RO3006_RO3035_zitex_4', alpha=0.5)
# plt.scatter(arc_stats(RO3006_RO3035_RO3003)[2], arc_stats(RO3006_RO3035_RO3003)[1], label='RO3006_RO3035_RO3003_4', alpha=0.5)
# plt.scatter(arc_stats(RO3006_RO3035_Porex)[2], arc_stats(RO3006_RO3035_Porex)[1], label='RO3006_RO3035_Porex_4', alpha=0.5)
# plt.scatter(arc_stats(RO3006_RO3003_Zitex)[2], arc_stats(RO3006_RO3003_Zitex)[1], label='RO3006_RO3003_Zitex_4', alpha=0.5)
# plt.scatter(arc_stats(RO3006_RO3003_Porex)[2], arc_stats(RO3006_RO3003_Porex)[1], label='RO3006_RO3003_Porex_4', alpha=0.5)
# plt.scatter(arc_stats(RO3006_Porex_Zitex)[2], arc_stats(RO3006_Porex_Zitex)[1], label='RO3006_Porex_Zitex_4', alpha=0.5)
# plt.scatter(arc_stats(RO3003_Porex_Zitex)[2], arc_stats(RO3003_Porex_Zitex)[1], label='RO3003_Porex_Zitex_4', alpha=0.5)
# plt.legend()

# # # ##annotate what we're interested in

# # for i in arc_stats(ro3006_ro3035_porex_2)[2]:
# #     plt.annotate(np.base_repr(i,5), (arc_stats(ro3006_ro3035_porex_2)[0][i], arc_stats(ro3006_ro3035_porex_2)[1][i]))

# # for i in arc_stats(ro3006_ro3035_zitex_2)[2]:
# #     plt.annotate(np.base_repr(i,5), (arc_stats(ro3006_ro3035_zitex_2)[0][i], arc_stats(ro3006_ro3035_zitex_2)[1][i]))

# # for i in arc_stats(ro3035_porex_zitex)[2]:
# #     plt.annotate(np.base_repr(i,5), (arc_stats(ro3035_porex_zitex)[0][i], arc_stats(ro3035_porex_zitex)[1][i]))

# # for i in arc_stats(ro3035_ro3003_zitex)[2]:
# #     plt.annotate(np.base_repr(i,5), (arc_stats(ro3035_ro3003_zitex)[0][i], arc_stats(ro3035_ro3003_zitex)[1][i]))

# # for i in arc_stats(ro3035_porex_zitex)[2]:
# #     plt.annotate(np.base_repr(i,5), (arc_stats(ro3035_porex_zitex)[0][i], arc_stats(ro3035_porex_zitex)[1][i]))

# # for i in arc_stats(ro3003_porex_zitex)[2]:
# #     plt.annotate(np.base_repr(i,5), (arc_stats(ro3003_porex_zitex)[0][i], arc_stats(ro3003_porex_zitex)[1][i]))

# # for i in arc_stats(ro3006_ro3003_porex)[2]:
# #     plt.annotate(np.base_repr(i,5), (arc_stats(ro3006_ro3003_porex)[0][i], arc_stats(ro3006_ro3003_porex)[1][i]))

# # for i in arc_stats(ro3006_ro3035_ro3003)[2]:
# #     plt.annotate(np.base_repr(i,5), (arc_stats(ro3006_ro3035_ro3003)[0][i], arc_stats(ro3006_ro3035_ro3003)[1][i]))

# # for i in arc_stats(ro3006_porex_zitex)[2]:
# #     plt.annotate(np.base_repr(i,5), (arc_stats(ro3006_porex_zitex)[0][i], arc_stats(ro3006_porex_zitex)[1][i]))

# # for i in arc_stats(ro3006_ro3003_zitex)[2]:
# #     plt.annotate(np.base_repr(i,5), (arc_stats(ro3006_ro3003_zitex)[0][i], arc_stats(ro3006_ro3003_zitex)[1][i]))


# plt.show()



























###########################################################################clean up below

# #single plot stuff 
# #NOTE: turn this into a function

# plt.figure(figsize=(10,10))
# plt.xlabel('Frequencies (GHz)')
# plt.ylabel('Transmittance')
# plt.title('Multi layer ARC - mean ')#+ str(round(arc_stats(ro3006_ro3035_porex)[1][533])*100,3) + 'stddev ' + str(round(arc_stats(ro3006_ro3035_porex)[0][533])*100,3))
# plt.scatter(frequencies, ro3006_ro3035_porex[533], c=c1, label='5 layers RO3006, 3 layers RO3035. 3 layers Porex')
# plt.axvspan(25.5, 34.5, color='black', alpha=0.1)
# plt.axvspan(34, 46, color='black', alpha=0.2)
# plt.ylim(0,1)
# plt.legend()
# plt.show()

# #big plots
# #NOTE: clean this up and also make a function
# numbers = []
# numbers = np.arange(0,1000,1)

# ro3003_ro3035_porex_stddev = [round(np.std(ro3003_ro3035_porex[x])*100, 2) for x in numbers]
# ro3003_ro3035_porex_mean = [round(np.mean(ro3003_ro3035_porex[x])*100, 2) for x in numbers]
# ro3003_ro3035_zitex_stddev = [round(np.std(ro3003_ro3035_zitex[x])*100, 2) for x in numbers]
# ro3003_ro3035_zitex_mean = [round(np.mean(ro3003_ro3035_zitex[x])*100, 2) for x in numbers]

# ro3006_ro3035_porex_stddev = [round(np.std(ro3006_ro3035_porex[x])*100, 2) for x in numbers]
# ro3006_ro3035_porex_mean = [round(np.mean(ro3006_ro3035_porex[x])*100, 2) for x in numbers]
# ro3006_ro3035_zitex_stddev = [round(np.std(ro3006_ro3035_zitex[x])*100, 2) for x in numbers]
# ro3006_ro3035_zitex_mean = [round(np.mean(ro3006_ro3035_zitex[x])*100, 2) for x in numbers]

# # ro3035_porex_stddev = [round(np.std(ro3035_porex[x])*100, 2) for x in numbers]
# # ro3035_porex_mean = [round(np.mean(ro3035_porex[x])*100, 2) for x in numbers]
# # ro3035_zitex_stddev = [round(np.std(ro3035_zitex[x])*100, 2) for x in numbers]
# # ro3035_zitex_mean = [round(np.mean(ro3035_zitex[x])*100, 2) for x in numbers]

# #mean and stddev as function of layers
# xaxis = np.linspace(0,1000,1000)

# plt.figure(figsize=(10,10))
# plt.plot(xaxis, ro3003_ro3035_porex_mean, label='RO3003_ro3035_Porex')
# plt.plot(xaxis, ro3003_ro3035_zitex_mean, label='RO3003_ro3035_Zitex')
# plt.plot(xaxis, ro3006_ro3035_porex_mean, label='RO3006_ro3035_Porex')
# plt.plot(xaxis, ro3006_ro3035_zitex_mean, label='RO3006_ro3035_Zitex')
# # plt.plot(xaxis, ro3035_porex_mean, label='RO3035_Porex')
# # plt.plot(xaxis, ro3035_zitex_mean, label='RO3035_Zitex')
# plt.plot(xaxis, ro3003_ro3035_porex_stddev, label='RO3003_ro3035_Porex')
# plt.plot(xaxis, ro3003_ro3035_zitex_stddev, label='RO3003_ro3035_Zitex')
# plt.plot(xaxis, ro3006_ro3035_porex_stddev, label='RO3006_ro3035_Porex')
# plt.plot(xaxis, ro3006_ro3035_zitex_stddev, label='RO3006_ro3035_Zitex')
# # plt.plot(xaxis, ro3035_porex_stddev, label='RO3035_Porex')
# # plt.plot(xaxis, ro3035_zitex_stddev, label='RO3035_Zitex')
# plt.legend()

# ##mean vs stddev
# labels = []

# plt.figure(figsize=(10,10))
# plt.title('Transmission of multi layer AR coating')
# plt.ylabel('Mean transmission')
# plt.xlabel('Standard Deviation')
# plt.ylim(95,100)
# plt.xlim(0,2)
# plt.scatter(y=ro3003_ro3035_porex_mean, x=ro3003_ro3035_porex_stddev, label='RO3003_ro3035_Porex')
# # plt.scatter(y=ro3003_ro3035_zitex_mean, x=ro3003_ro3035_zitex_stddev, label='RO3003_ro3035_Zitex')
# # plt.scatter(y=ro3006_ro3035_porex_mean, x=ro3006_ro3035_porex_stddev, label='RO3006_ro3035_Porex')
# # plt.scatter(y=ro3006_ro3035_zitex_mean, x=ro3006_ro3035_zitex_stddev, label='RO3006_ro3035_Zitex')
# # plt.scatter(y=ro3035_porex_mean, x=ro3035_porex_stddev, label='RO3035_Porex')
# # plt.scatter(y=ro3035_zitex_mean, x=ro3035_zitex_stddev, label='RO3035_Zitex')
# plt.legend()

# ##mean as a function of layers. stddev represented by errorbars
# plt.figure(figsize=(200,10))
# plt.errorbar(xaxis, ro3003_ro3035_porex_mean, yerr=ro3003_ro3035_porex_stddev, label='RO3003_Porex', fmt='o')
# # plt.errorbar(xaxis, ro3003_zitex_mean, yerr=ro3003_zitex_stddev, label='RO3003_Zitex', fmt='o')
# # plt.errorbar(xaxis, ro3006_porex_mean, yerr=ro3006_porex_stddev, label='RO3006_Porex', fmt='o')
# # plt.errorbar(xaxis, ro3006_zitex_mean, yerr=ro3006_zitex_stddev, label='RO3006_Zitex', fmt='o')
# # plt.errorbar(xaxis, ro3035_porex_mean, yerr=ro3035_porex_stddev, label='RO3035_Porex', fmt='o')
# # plt.errorbar(xaxis, ro3035_zitex_mean, yerr=ro3035_zitex_stddev, label='RO3035_Zitex', fmt='o')
# # plt.legend()