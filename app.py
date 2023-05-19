# -*- coding: utf-8 -*-
"""
Created on Thu May 18 00:36:05 2023

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open('diabetes_model.sav','rb'),encoding='utf-8')
heart_model=pickle.load(open('heart_model.sav','rb'),encoding='utf-8')
parkinsons_mode=pickle.load(open('parkinsons_model.sav','rb'),encoding='utf-8')

with st.sidebar:
    selected=option_menu('Multiple Diesease Predictor', ['Diabetes Prediction','Heart Diesease Prediction','Parkinsons Prediction'],
                         icons=["activity","heart-pulse",'person']
                         ,default_index=0)


if selected=='Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnencies')
        SkinThickness=st.text_input('Enter SkinThickness')
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    with col2:
        Glucose=st.text_input('Current Glucose level')
        Insulin=st.text_input('Enter Insulin value in body')
        Age=st.text_input('Enter Your Age')
    with col3:
        BloodPressure=st.text_input('Current BP')
        BMI=st.text_input('Enter BMI')
    
   
    
    diabetes_diagnosis=''
    
    if st.button('Diabetes Test Result'):
        diabetes_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(diabetes_prediction[0]==1):
            print("The person is Diabetic")
        else:
            print("The person is not diabetic")
    st.success(diabetes_diagnosis)



if selected=='Heart Diesease Prediction':
    st.title('Heart Diesease Prediction using ML')
    
    col1,col2,col3,col4=st.columns(4)
    
    with col1:
        ag=st.text_input('Enter Age')
        chol=st.text_input('Serum cholestoral in mg/dl')
        exang=st.text_input('Exercise induced angina')
    with col2:
        sex=st.text_input('Enter Sex')
        fbs=st.text_input('Fasting blood sugar')
        oldpeak=st.text_input('Oldpeak')

    with col3:
        cp=st.text_input('Chest Pain type')
        restecg=st.text_input('resting ECG results')
        slope=st.text_input('Slope ST segment')
        
    with col4:
        trestbps=st.text_input('Resting BP')
        thalach=st.text_input('Maximum heart rate')
        ca=st.text_input('No of major vessels(0-3)')
    
    thal=st.text_input('thal value,(0 = normal,1 = fixed defect;,2 = reversable defect)')
    
    
    heart_diagnosis=''
    
    if st.button('Heart diesease Test Result'):
        heart_prediction=heart_model.predict([[ag,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(heart_prediction[0]==1):
            print("The person is heart patient")
        else:
            print("The person is not heart patient")
    st.success(heart_diagnosis)
    
    
    
if selected=='Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')
    
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        MDVPFo=st.text_input('MDVP:Fo(Hz)')
        MDVPRAP=st.text_input('MDVP:RAP')
        ShimmerAPQ3=st.text_input('Shimmer:APQ3')
        HNR=st.text_input('HNR')
        D2=st.text_input('D2')
    with col2:
        MDVPFhi=st.text_input('MDVP:Fhi(Hz)')
        MDVPPPQ=st.text_input('MDVP:PPQ')
        ShimmerAPQ5=st.text_input('Shimmer:APQ5')
        RPDE=st.text_input('RPDE')
        PPE=st.text_input('PPE')
    with col3:
        MDVPFlo=st.text_input('MDVP:Flo(Hz)')
        JitterDDP=st.text_input('Jitter:DDP')
        MDVPAPQ=st.text_input('MDVP:APQ,Shimmer')
        DFA=st.text_input('DFA')
        
    with col4:
        MDVPJitter=st.text_input('MDVP:Jitter(%)')
        MDVPShimmer=st.text_input('MDVP:Shimmer')
        ShimmerDDA=st.text_input('Shimmer:DDA')
        spread1=st.text_input('spread1')
    
    with col5:
        MDVPJitter=st.text_input('MDVP:Jitter')
        MDVPShimmer=st.text_input('MDVP:Shimmer(dB)')
        NHR=st.text_input(' NHR')
        spread2=st.text_input('spread2')
    
    parkinsons_diagnosis=''
    
    if st.button('Parkinsons Test Result'):
        parkinsons_prediction=parkinsons_model.predict([[MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitter,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmer,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if(heart_prediction[0]==1):
            print("The person has parkinsons")
        else:
            print("The person has not parkinsons")
    st.success(parkinsons_diagnosis)
    
    
    