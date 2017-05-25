#!/usr/bin/env python3

def loader_data(data_file):
    with open(data_file,'r') as file:
        line = file.readline()
    titles = line.split()
    data = np.loadtxt(data_file, skiprows=1).transpose()
    return titles, data


def plotting(data, titles, bar=False, scattor=False, save=False, save_fig_name='fig.png'):
    #determine how many subplot from data
    x = data[0]
    subp = data.shape[0]//2
    #determine one or two columm of figure are need.
    if data.shape[0] == 2: #data contains x and only y value
        col = 10
    else:
        col = 20

    if save:
        fig = plt.figure(figsize=(6, 8), dpi=300)
    else:
        fig = plt.figure(figsize=(6, 8))

    fig.subplots_adjust(wspace=0.5, bottom=0.2)
    ymax, ymin = data[1:].max()+.5, data[1:].min()-.5

    if scattor==True:
        if 0<=data.shape[1]<=50:
            marker_size = 5
        elif 51<=data.shape[1]<=100:
            marker_size = 4
        elif 10<=data.shape[1]<=1000:
            marker_size = 3
        elif data.shape[1]>=1000:
            marker_size =1.5

    for i in range(1,data.shape[0]):
        plt.subplot(subp*100+col+i)
        if bar == True:
            plt.bar(x,data[i], 0.25, color='steelblue', edgecolor='k', linewidth=0.5)
        elif scattor == True:
            plt.plot(x,data[i], marker='o', linewidth=0, markersize=marker_size)
        else:
            plt.plot(x,data[i], color='steelblue')
    #    plt.title(titles[i])
        plt.xlabel(titles[0], fontsize=10)
        plt.ylabel(titles[i], fontsize=10)
        plt.gca().set_ylim([ymin,ymax])
    plt.tight_layout()
    if save:
        fig.savefig(save_fig_name, dpi=300, bbox_inches='tight')
        print('plot has been save to %s' %save_fig_name)
    else:
        plt.show()

if __name__=='__main__':
    import argparse, sys
    import numpy as np
    parser = argparse.ArgumentParser(description='''General plot function based on matplotlib''')
    parser.add_argument('-i', help='the input dlg file.')
    parser.add_argument('-bar', action="store_true", help='plot bar chart')
    parser.add_argument('-scattor', action="store_true", help='plot scattor')
    parser.add_argument('-save', action="store_true", help="instead of showing plot, save the figure with supplied name.")
    args = parser.parse_args()
    save = args.save
    data_file = args.i
    if data_file:
        save_fig_name = data_file.split('.')[0]+'.png'
    else:
        print("usage: plot.py [-h] [-i I] [-bar] [-scattor] [-save]")
        sys.exit()
    bar = args.bar
    scattor = args.scattor
    try:
        if save == True:
            import matplotlib as matplotlib
            matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print('Unabel to import matplotlib!')
        raise
    plt.style.use('ggplot') #using 'R' like style
    titles, data =loader_data(data_file)
    plotting(data, titles, bar, scattor, save, save_fig_name)