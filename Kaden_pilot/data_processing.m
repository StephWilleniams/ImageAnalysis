
%% Directory/workspace prep

clear all
close all
cd '/Users/steve/Library/CloudStorage/GoogleDrive-stev3.w1l@gmail.com/My Drive/Academia/p_projects_merced/a_projects/c_theme1/d_data/Kaden_pilot'

%% Load data

data_repro = readtable("reproduction.csv");
data_surv = readtable("survival.csv");

%% OHE files


