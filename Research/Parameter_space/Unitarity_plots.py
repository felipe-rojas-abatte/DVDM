#size of the dots in scatter plot
dots=6

#Define the quantity of colors in colorbar
cmap = plt.get_cmap('jet') 

current_dir = os.getcwd()
new_folder = current_dir+'/Unitarity/'+cuts

if not os.path.exists(new_folder):
    os.makedirs(new_folder)


#----------- Plot 1 Mv1-ld345-Omega-------------------------
fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(Mv1[cut2], lamL[cut2], c='r', s=dots, edgecolor='', rasterized=True, label='Excluded')
ax.scatter(Mv1[cut1], lamL[cut1], c='g', s=dots, edgecolor='', rasterized=True, label='Accepted')

#Name of axes 
plt.xlabel("Mv$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\lambda_L$", fontsize=20)
plt.title('Energy cut-off $\\Lambda=$'+energy+' (TeV)')
plt.xlim(min(Mv1),max(Mv1))
plt.xscale('log')
#plt.xlim(min(Mh1),200)
plt.ylim(min(lamL),max(lamL))

legend1b = plt.legend( loc="upper left", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend1b)

fig.tight_layout()
plt.savefig(new_folder+'/Mv1_lamL_Omega_'+cuts+'.pdf')


# ---------- Plot 2 Mv1-Mv2-Omega --------------------------
fig2, ax2 = plt.subplots(figsize=(6,4))
ax2.scatter(Mv1[cut2], Mv2[cut2], c='r', s=dots, edgecolor='', rasterized=True, label='Excluded')
ax2.scatter(Mv1[cut1], Mv2[cut1], c='g', s=dots, edgecolor='', rasterized=True, label='Accepted')

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("Mv$_2$ (GeV)",fontsize=15)
plt.title('Energy cut-off $\\Lambda=$'+energy+' (TeV)')
plt.xlim(min(Mv1),max(Mv1))
plt.ylim(min(Mv2),max(Mv2))
plt.xscale('log')
plt.yscale('log')

legend1b = plt.legend( loc="upper left", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend1b)

fig2.tight_layout()
plt.savefig(new_folder+'/Mv1_Mv2_Omega_'+cuts+'.pdf')

# ---------- Plot 3 Mv1-Mvp-Omega --------------------------
fig3, ax3 = plt.subplots(figsize=(6,4))
ax3.scatter(Mv1[cut2], Mvp[cut2], c='r', s=dots, edgecolor='', rasterized=True, label='Excluded')
ax3.scatter(Mv1[cut1], Mvp[cut1], c='g', s=dots, edgecolor='', rasterized=True, label='Accepted')

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("M$_{v^{\\pm}}$ (GeV)",fontsize=15)
plt.title('Energy cut-off $\\Lambda=$'+energy+' (TeV)')
plt.xlim(min(Mv1),max(Mv1))
plt.ylim(min(Mvp),max(Mvp))
plt.xscale('log')
plt.yscale('log')

legend1b = plt.legend( loc="upper left", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend1b)

fig3.tight_layout()
plt.savefig(new_folder+'/Mv1_Mvp_Omega_'+cuts+'.pdf')

# ---------- Plot 4 Mv2-Mvp-Omega --------------------------
fig4, ax4 = plt.subplots(figsize=(6,4))
ax4.scatter(Mv2[cut2], Mvp[cut2], c='r', s=dots, edgecolor='', rasterized=True, label='Excluded')
ax4.scatter(Mv2[cut1], Mvp[cut1], c='g', s=dots, edgecolor='', rasterized=True, label='Accepted')

#Name of axes
plt.xlabel("Mv$_2$ (GeV)",fontsize=15)
plt.ylabel("M$_{v^{\\pm}}$ (GeV)",fontsize=15)
plt.title('Energy cut-off $\\Lambda=$'+energy+' (TeV)')
plt.xlim(min(Mv2),max(Mv2))
plt.ylim(min(Mvp),max(Mvp))
plt.xscale('log')
plt.yscale('log')

legend1b = plt.legend( loc="upper left", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend1b)

fig4.tight_layout()
plt.savefig(new_folder+'/Mv2_Mvp_Omega_'+cuts+'.pdf')

plt.close('all')

