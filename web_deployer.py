# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 21:52:44 2023

@author: ASUS
"""

import numpy as np
import pickle
import streamlit as sl

loadie=pickle.load(open("/saver.sav","rb"))

def depredic(inputda):
    inputdaas=np.asarray(inputda)
    inputdar=inputdaas.reshape(1,-1)
    predictie=loadie.predict(inputdar)
    print("The price of the car might be:",predictie)
    return predictie

def main():
    sl.title("Car price predictor")
    wheel=sl.text_input("Wheelbase")
    engine=sl.text_input("Engine size")
    bore=sl.text_input("Bore ratio")
    stroke=sl.text_input('stroke')
    cr=sl.text_input("Compression Ratio")
    hp=sl.text_input("Horse power")
    rpm=sl.text_input("Peak rpm")
    city=sl.slider("City mpg",1,100)
    high=sl.slider("Highway mpg",1,100)
    
    
    if(sl.button("predict the price")):
        af=depredic([wheel,engine,bore,stroke,cr,hp,rpm,city,high])
        rf=af*79
        sl.subheader("Therefore The predicted output price of the car is....")
        sl.success(af)
        sl.subheader("Therefore The predicted output price of the car in Indian value is....")
        sl.warning(rf)
    sl.markdown('<div style="text-align: right;">Developed by</div>', unsafe_allow_html=True)
    sl.markdown('<div style="text-align: right;">Kavin V</div>', unsafe_allow_html=True)
    sl.markdown('<div style="text-align: right;">Harshit S</div>', unsafe_allow_html=True)  
        
if __name__=='__main__':
    main()
    
