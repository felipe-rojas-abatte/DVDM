#size of the dots in scatter plot
dots=10
#Create the features of the colorbar
bounds=np.linspace(-7,5,13,endpoint=True)
lim_inf = np.log10(0.0000001)
lim_sup = np.log10(100)

Mvchar = np.linspace(10, 2000, 1000) 
mu_sup_new = np.linspace(0.99+0.14,0.99+0.14,1000) 
mu_inf_new = np.linspace(0.99-0.14,0.99-0.14,1000)

bounds_l2=np.linspace(-10,10,21,endpoint=True)
lim_inf_l2 = -10
lim_sup_l2 = 10

#Define the quantity of colors in colorbar
cmap = plt.get_cmap('jet') 

current_dir = os.getcwd()
new_folder = current_dir+'/Systematic_cuts/'+cuts

if not os.path.exists(new_folder):
    os.makedirs(new_folder)


#----------- Plot 1 Mv1-ld345-Omega-------------------------
fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(Mv1[cut_planck], lamL[cut_planck], c='gray', s=dots, edgecolor='', rasterized=True)
ax.scatter(Mv1[cut_todo], lamL[cut_todo], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes 
plt.xlabel("Mv$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\lambda_L$", fontsize=20)
plt.xlim(10,80)
#plt.xlim(10,2000)
#plt.xscale('log')
plt.ylim(-1,1)
fig.tight_layout()
plt.savefig(new_folder+'/Mv1_lamL_Omega_'+cuts+'.pdf')


#----------- Plot 1 Mv1-ld345-Omega-------------------------
fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(Mv1[cut_planck], lamL[cut_planck], c='gray', s=dots, edgecolor='', rasterized=True)
ax.scatter(Mv1[cut_todo], lamL[cut_todo], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes 
plt.xlabel("Mv$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\lambda_L$", fontsize=20)
plt.xlim(50,80)
#plt.xlim(10,2000)
#plt.xscale('log')
plt.ylim(-0.1,0.1)
fig.tight_layout()
plt.savefig(new_folder+'/Mv1_lamL_Omega_zoom_'+cuts+'.pdf')


# ---------- Plot 2 Mv1-Mv2-Omega --------------------------
fig2, ax2 = plt.subplots(figsize=(6,4))
ax2.scatter(Mv1[cut_planck], Mv2[cut_planck], c='gray', s=dots, edgecolor='', rasterized=True)
ax2.scatter(Mv1[cut_todo], Mv2[cut_todo], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("Mv$_2$ (GeV)",fontsize=15)
#plt.xlim(10,100)
plt.xlim(10,2000)
plt.ylim(10,2000)
plt.xscale('log')
plt.yscale('log')
fig2.tight_layout()
plt.savefig(new_folder+'/Mv1_Mv2_Omega_'+cuts+'.pdf')


# ---------- Plot 3 Mv1-Mvp-Omega --------------------------
fig3, ax3 = plt.subplots(figsize=(6,4))
ax3.scatter(Mv1[cut_planck], Mvp[cut_planck], c='gray', s=dots, edgecolor='', rasterized=True)
ax3.scatter(Mv1[cut_todo], Mvp[cut_todo], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("M$_{v^{\\pm}}$ (GeV)",fontsize=15)
#plt.xlim(10,100)
plt.xlim(10,2000)
plt.ylim(10,2000)
plt.xscale('log')
plt.yscale('log')
fig3.tight_layout()
plt.savefig(new_folder+'/Mv1_Mvp_Omega_'+cuts+'.pdf')

# ---------- Plot 4 Mv2-Mvp-Omega --------------------------
fig4, ax4 = plt.subplots(figsize=(6,4))
ax4.scatter(Mv2[cut_planck], Mvp[cut_planck], c='gray', s=dots, edgecolor='', rasterized=True)
ax4.scatter(Mv2[cut_todo], Mvp[cut_todo], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("Mv$_2$ (GeV)",fontsize=15)
plt.ylabel("M$_{v^{\\pm}}$ (GeV)",fontsize=15)
plt.xlim(10,2000)
plt.ylim(10,2000)
plt.xscale('log')
plt.yscale('log')
fig4.tight_layout()
plt.savefig(new_folder+'/Mv2_Mvp_Omega_'+cuts+'.pdf')


# ---------- Plot 8 RAA-Mvp-Omega --------------------------
fig8, ax8 = plt.subplots(figsize=(6,4))
ax8.scatter(Mvp[cut_planck], RAA[cut_planck], c='gray', s=dots, edgecolor='', rasterized=True)
ax8.scatter(Mvp[cut_todo], RAA[cut_todo], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("M$_{V^{\\pm}}$ (GeV)",fontsize=15)
plt.ylabel("$\\mu_{\\gamma \\gamma}$ ",fontsize=15)
plt.xlim(10,1000)
plt.ylim(0.1,10)
plt.xscale('log')
plt.yscale('log')
plt.plot(Mvchar, mu_sup_new, color='r',linewidth=2)
plt.plot(Mvchar, mu_inf_new, color='r',linewidth=2)
fig8.tight_layout()
plt.savefig(new_folder+'/RAA_Mvp_Omega_'+cuts+'.pdf')

# ---------- Plot 9 RAA-Mvp-Omega --------------------------
fig9, ax9 = plt.subplots(figsize=(6,4))
ax9.scatter(Mv1[cut_planck], RAA[cut_planck], c='gray', s=dots, edgecolor='', rasterized=True)
ax9.scatter(Mv1[cut_todo], RAA[cut_todo], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("$\\mu_{\\gamma \\gamma}$ ",fontsize=15)
plt.xlim(10,100)
#plt.ylim(0,2)
plt.ylim(min(RAA),5)
#plt.yscale('log')
plt.plot(Mvchar, mu_sup_new, color='r',linewidth=2)
plt.plot(Mvchar, mu_inf_new, color='r',linewidth=2)
fig9.tight_layout()
plt.savefig(new_folder+'/RAA_Mv1_Omega_'+cuts+'.pdf')


plt.close('all')

