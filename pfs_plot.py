'''
This is a collection of useful subfunctions that I use across my analyses for plotting

To use these functions in an analysis in another folder, use the following at the beginning of the python session:
import sys
sys.path.append(path_to_this_file)
import pfs_plot
call a function using pfs_plot.save_fig_to_folder, etc...

PFS, U. Michigan, 2017
'''
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
import os

def save_fig_to_folder(fig_filename,fig_folder='fig'):
    """
    Summary: Save .png of current matplotlib plot to fig_folder / fig_filename
    Code will check to make sure fig_folder exists. If not, create folder then save .png to folder
    
    Require: fig_filename
    Modify: fig_folder, set to folder name, or to None to save to cwd
    Effect: Saves figure to file in fig_folder    
    """
    # If saving to same folder
    if fig_folder == None:
        plt.savefig(fig_filename)
    # If saving to a subfolder
    else:
        try:
            os.stat(fig_folder)
        except:
            os.mkdir(fig_folder)
        plt.savefig(fig_folder+'/'+fig_filename)  