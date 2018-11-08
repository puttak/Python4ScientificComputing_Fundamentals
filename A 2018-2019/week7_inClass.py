# -*- coding: utf-8 -*-
"""
Created on Thu Nov 08 13:41:45 2018

@author: behzad
"""

import numpy as np
import pandas as pd

A1=np.array([2,5.2,1.8,5])

S1 = pd.Series([2,5.2,1.8,5],["a","b","c","d"])
S2 = pd.Series([2,5.2,1.8,5],index= ["a","b","c","d"])

S2["c"]

Q_heating = pd.Series([1150,1240,120],index=["wall","ceiling","door"])

# Were you will probabely make mistakes !
# remember that Series (starts with capital S)
# remember the first item ia list you should0nt write it like this: pd.Series(1,3,3,2)
Q_heating["door"]

# of course we can repeat the same procedure we did with arrays

Opaque_item_list = ["wall", "ceiling","door"]

Opaque_U_list = [0.438,0.25,1.78]
opaque_U_Series = pd.Series(Opaque_U_list,index=Opaque_item_list)
opaque_area_list = [105.8,200,2.2]
opaque_area_Series=  pd.Series(opaque_area_list,index=Opaque_item_list)

T_inside_heating= 20
T_outside_heating = -4.8
DeltaT_heating= T_inside_heating-T_outside_heating

opaque_HF_Series = DeltaT_heating*opaque_U_Series
opaque_Q_Series = opaque_HF_Series*opaque_area_Series

# one of very useful pandas capabilities is the apply function !!
def toKwGenerator(inputVal):
    outputVal = inputVal/1000
    return outputVal

Q_heating_kw = opaque_Q_Series.apply(toKwGenerator)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%
#It is a better idea to use a dataframe
Opaque_U_list = [0.438,0.25,1.78]
opaque_area_list = [105.8,200,2.2]
Opaque_item_list = ["wall", "ceiling","door"]
T_inside_heating= 20
T_outside_heating = -4.8
DeltaT_heating= T_inside_heating-T_outside_heating


DF_opaque = pd.DataFrame([Opaque_U_list,opaque_area_list],index=["U","Area"],columns=Opaque_item_list)
DF_opaque.iloc[0,:] # first way
DF_opaque.loc["U",:] # second way
DF_opaque.loc["HF",:] = DF_opaque.loc["U",:]*DeltaT_heating
DF_opaque.loc["Q",:] = DF_opaque.loc["HF",:]*DF_opaque.loc["Area",:]
DF_opaque.loc["Q_kW",:] = 