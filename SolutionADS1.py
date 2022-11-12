# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:56:33 2022

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read the excel data using pandas, specifing the sheet name and 
#extract rows and columns of interest
energy_data = pd.read_excel(r"C:\Users\USER\Desktop\Data Science Course\Applied Data Science 1\Assignment 2\ECUK_2022_End_Use_tables_10102022.xlsx", 
                      sheet_name="Table U1", 
                      skiprows=5, 
                      skipfooter=36, 
                      usecols=[0,1,3,4,5,6],
                      )


#################LINE PLOT#########################

#Extract rows within the years of interest (2012-2021) where the yearly 
#consumption totals are calculated per end-use
energy_total = energy_data.loc[energy_data["End use"] == "Total"]

energy_total = np.round(energy_total,decimals=2)  #convert all values to 2decimal places

#create line plot of dataframe properties against year of occurrence 
#using a function

def line_plot(x, y_data, label):  #define line plot function

    """
    Creates a line plot of variables

    Parameters
    ----------
    x : array or list
        Contains indexed points on the x-axis.
    y_data : array or list
        Contains plot values for the y-axis.
    label : string
          Name of the individual plotted list or array.   
    
    Returns
    -------
    fig : list of line2D
        A list of lines representing the plotted data.

    """
    fig = plt.figure(figsize=(10,6))  #define the plot environment
    plt.plot(x, y_data1, linewidth=4, label=label1)  #line plot1  
    plt.plot(x, y_data2, linewidth=4, label=label2)  #line plot 2
    plt.plot(x, y_data3, linewidth=4, label=label3)  #line plot 3
    plt.xlabel(x_axis, labelpad=7)  #set the x-axis parameters 
    plt.ylabel(y_axis, labelpad=7)  #set the y-axis parameters 
    plt.xticks()
    plt.title(title, fontdict={'fontsize': 20}, pad=(10)) #set the title parameters 
    plt.legend() #show a legend on the plot
    return fig

#Initialise the function variables
x = energy_total["Year"]  #x-axis variable
#y_axis variables
y_data1 = energy_total["Domestic"]  
y_data2 = energy_total["Service"]  
y_data3 = energy_total["Industrial"] 
#label y-axis variables
label1 = "Domestic Consumption"  
label2 = "Service Consumption"  
label3 = "Industrial Consumption" 
title = "United Kingdom Energy Consumption By End Use, 2012-2021"  
x_axis = "Years"  #label the x-axis
y_axis = "Consumption (ktoe)"  #label the y-axis

#Specify plot parameters
plt.xlim(2012,2021)  
plt.ylim(10000,46000)
plt.rc('font', size=15)  
plt.rc('axes', labelsize=18)  
plt.style.use('seaborn-whitegrid')  #specify a plot style

#Implement the plot function on the data
line_plot(x, y_data=[y_data1, y_data2, y_data3], label=[label1,label2,label3])


plt.show()


#################STACK PLOT#########################

#Plot a stacked plot for the domestic consumption rates
#Extract the Domestic column from the dataframe
domestic_data = energy_data.iloc[:, :3]
domestic_data = domestic_data.rename(columns = {"End use":"End_use", 
                                                "Domestic":"ktoe"})

def stack_plot(x, y_data, label):  #define line plot function
    """
    Creates a stacked area plot, displaying how constituent 
    parts make up a whole.

    Parameters
    ----------
    x : 1D array
        It is 1D array with N dimensions used to give 
        values to the x-axis.
    y_data : 2D array
        Represents a 2D array of M*N dimension which is unstacked.
    label : string
        Name of the individual plotted array.

    Returns
    -------
    fig : list of PolyCollection
        A list of PlyCollection instances, one for each element in 
        the stacked plot area.

    """
    fig = plt.figure(figsize=(10,6))  #define the plot environment
    plt.plot([],[], color='teal', label=label1) #set the parameters for y_data1
    plt.plot([],[], color='cyan', label =label2)  #set the parameters for y_data2
    plt.plot([],[], color='tomato', label=label3)  #set the parameters for y_data3
    plt.plot([],[], color='dodgerblue', label=label4)  #set the parameters for y_data4
    plt.stackplot(x, y_data1, y_data2, y_data3, y_data4, 
                  colors = ['teal','cyan','tomato','dodgerblue'])  #define plot properties 
    plt.title(title)  #set the title parameters 
    plt.xlabel(x_axis)  #set the x-axis parameters 
    plt.ylabel(y_axis)  #set the y-axis parameters 
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.20), shadow=True, 
                ncol=2, fontsize=16)  #set legend parameter and show legend on the plot
  
    return fig

#Initialise the function variables
space_heating = domestic_data[domestic_data.End_use == "Space heating"]
Water = domestic_data[domestic_data.End_use == "Water "]
cooking_catering = domestic_data[domestic_data.End_use == "Cooking/ Catering"]
lighting_appliances = domestic_data[domestic_data.End_use == "Lighting/ Appliances"]
x = Water["Year"] #x-axis variable
y_data1 = space_heating["ktoe"]  #1st y-axis variable
y_data2 = Water["ktoe"]  #2nd y-axis variable
y_data3 = lighting_appliances["ktoe"]  #3rd y-axis variable
y_data4 = cooking_catering["ktoe"]  #4th y-axis variable
#label y-axis variables
label1 = "Space Heating" 
label2 = "Water"  #name 
label3 = "Cooking/Catering"  
label4 = "Lighting appliances"  

#Implement the plot function on the data
stack_plot(x, y_data=[y_data1, y_data2, y_data3, y_data4], 
           label=[label1,label2,label3])

#Specify plot parameters
plt.xlim(2012, 2021)
plt.ylim(0, 45000)
plt.style.use('seaborn-whitegrid')
plt.xticks(rotation=45)
title = "United Kingdom Domestic Energy Consumption, 2012-2021"
x_axis = 'Year'
y_axis = 'Consumption (ktoe)'
plt.rc('font', size=16)  #specify the font size of x- and y- ticks
plt.rc('axes', labelsize=40)  #specify the font size of x- and y- axes labels

plt.show()




#################BAR CHART#########################


#Extract rows and columns of interest
yearly_use = energy_total.drop(["End use","Total"], axis=1)
yearly_use = yearly_use.iloc[0:6,:]
yearly_use = yearly_use.astype("int")
yearly_use = yearly_use.sort_values(by="Year")

#Transpose dataframe
yearly_use = yearly_use.transpose()

#create new columns
yearly_use["2016-2017"] = yearly_use.iloc[:,1] - yearly_use.iloc[:,0]
yearly_use["2017-2018"] = yearly_use.iloc[:,2] - yearly_use.iloc[:,1]
yearly_use["2018-2019"] = yearly_use.iloc[:,3] - yearly_use.iloc[:,2]
yearly_use["2019-2020"] = yearly_use.iloc[:,4] - yearly_use.iloc[:,3]
yearly_use["2020-2021"] = yearly_use.iloc[:,5] - yearly_use.iloc[:,4]

#Extract columns of interest
yearly_use = yearly_use.iloc[1:,6:]

#Transpose dataframe
yearly_use = yearly_use.transpose()


def bar_plot(arr, **kwargs):  #define line plot function
   
    '''
    Creates a bar chart

    Parameters
    ----------
    arr : float or array-like
        The x coordinates of bars.
    
    Returns
    -------
    fig : bar container
        Container with all the bars.

    '''
  
    fig = plt.subplots(figsize = (10, 6))  #define the plot environment
    b_width = w
    
    #define the position of the bars
    br1 = np.arange(len(arr))  #
    br2 = [x + b_width for x in br1]  
    br3 = [x + b_width for x in br2]
    
    #define plot parameters 
    plt.bar(br1, arr1, color="r", width=b_width, edgecolor="grey", 
            label=label1)
    plt.bar(br2, arr2, color="g", width=b_width, edgecolor="grey", 
            label=label2)
    plt.bar(br3, arr3, color="b", width=b_width, edgecolor="grey", 
            label=label3)
    plt.xticks([t + w for t in range(len(arr))], [a, b, c, d, e])
    
    return fig
    
   
#Initialise the function variables
w = 0.25 
arr1 = yearly_use["Domestic"]
arr2 = yearly_use["Industrial"]
arr3 = yearly_use["Service"]
label1 = "Domestic"
label2 = "Industrial"
label3 = "Service"
a = "2016 - 2017"
b = "2017 - 2018"
c = "2018 - 2019"
d = "2019 - 2020"
e = "2020 - 2021"

#Implement the plot function on the data
bar_plot(arr1)

#Specify plot parameters
plt.title("Annual Change by Sector, 2016-2021")
plt.xlabel("Year", fontsize=16)
plt.ylabel("Rate of Change (ktoe)", fontsize=16)
plt.legend(fontsize=12)
plt.rc('font', size=16)
plt.rc('axes', labelsize=13)
plt.ylim(-3000,3000)
plt.style.use('seaborn-whitegrid') 
plt.show()
