import sys
import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = 'Arial'


def plot_2drmsd(data_file, titles, save=False, save_fig_name='fig.png'):

    with open(data_file,'r') as f:
        line = f.readline()                 #x value in 1st line.
    x = [float(i) for i in line.split()[1:]]

    data = np.loadtxt(data_file, skiprows=0)
    y = data[:,0]                          #y data in 1st column
    rmsd = data[:,1:]

    if save:
        fig = plt.figure(figsize=(5, 4), dpi=300)
    else:
        fig = plt.figure(figsize=(5, 4))

    fig.subplots_adjust(wspace=0.25, bottom=0.2)
    ax1 = plt.subplot(111)

    #creat a color bat
#    norm = matplotlib.colors.Normalize(vmin=0, vmax=5.0)
    levels = np.arange(0, rmsd.max(), 0.5)
    cp = plt.contourf(x,y,rmsd, cmap='RdYlBu', vmin = 0, vmax = rmsd.max(), levels = levels, corner_mask = True)
    colorbar = plt.colorbar(cp)
    for text in colorbar.ax.get_yticklabels():
        text.set_fontsize(12)

    plt.xlabel('#Frame',fontsize=14)
    plt.ylabel('#Frame',fontsize=14)
    plt.title(titles,fontsize=14)

    plt.tight_layout()
    if save:
        fig.savefig(save_fig_name, dpi=300, bbox_inches='tight')
        print('plot has been save to %s' %save_fig_name)
    else:
        plt.show()

if __name__=='__main__':
    import argparse, sys
    import numpy as np
    parser = argparse.ArgumentParser(description='''Plot 2D RMSD''')
    parser.add_argument('-i', help='the input data file.')
    parser.add_argument('-save', action="store_true", help="instead of showing plot, save the figure with supplied name.")
    args = parser.parse_args()
    save = args.save
    data_file = args.i
    if data_file:
        save_fig_name = data_file.split('.')[0]+'.png'
        titles = data_file.split('.')[0]
    else:
        print("usage: plot.py [-h] [-i I] [-save]")
        sys.exit()
    try:
        if save == True:
            import matplotlib as matplotlib
            matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print('Unabel to import matplotlib!')
        raise
    plot_2drmsd(data_file, titles, save, save_fig_name)