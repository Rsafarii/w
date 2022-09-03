# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:07:45 2022

@author: www.markazi.co
"""
import time
import webbrowser as web
from datetime import datetime
from re import fullmatch
from urllib.parse import quote
import pyautogui as pg
import pywhatkit as pyw
from pywhatkit.core import core, exceptions, log
import streamlit as st
import time
import pandas as pd
import numpy as np
import streamlit.components.v1 as components


st.set_page_config(page_title='Wsender', page_icon='whatsapp_PNG21.png', layout="centered", initial_sidebar_state="auto", menu_items=None)
#@st.cache(suppress_st_warning=True,persist=True,allow_output_mutation=True) 
def TITLE():
    components.html(
'''              
<style>  
p{
text-align: center;
color:#ff944d;
font-family:TimesNewRoman, Times, serif;
font-size:20px;

}              
   body {
	margin: 0;
	height: 100px;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color:#fff;
}

</style>

<div> 
  <p>  Whatssapp Sender </p>
</div>

''',height=100,)

#@st.cache(suppress_st_warning=True,persist=True,allow_output_mutation=True) 
def TITLE_SIDEBAR():
     components.html(
'''
                
<style>  
         
   body {
	margin: 0;
	height: 100px;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color:#fff;
}

.loader {
    width: 120px;
    height: 120px;
    font-size: 10px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.loader .face {
    position: absolute;
    border-radius: 50%;
    border-style: solid;
    animation: animate 3s linear infinite;
}

.loader .face:nth-child(1) {
    width: 80%;
    height: 80%;
    color: gold;
    border-color: currentColor transparent transparent currentColor;
    border-width: 0.2em 0.2em 0em 0em;
    --deg: -45deg;
    animation-direction: normal;
}

.loader .face:nth-child(2) {
    width: 70%;
    height: 70%;
    color: lime;
    border-color: currentColor currentColor transparent transparent;
    border-width: 0.2em 0em 0em 0.2em;
    --deg: -135deg;
    animation-direction: reverse;
}

.loader .face .circle {
    position: absolute;
    width: 50%;
    height: 0.1em;
    top: 50%;
    left: 50%;
    background-color: transparent;
    transform: rotate(var(--deg));
    transform-origin: left;
}

.loader .face .circle::before {
    position: absolute;
    top: -0.5em;
    right: -0.5em;
    content: '';
    width: 1em;
    height: 1em;
    background-color: currentColor;
    border-radius: 50%;
    box-shadow: 0 0 2em,
                0 0 4em,
                0 0 6em,
                0 0 8em,
                0 0 10em,
                0 0 0 0.5em rgba(255, 255, 0, 0.1);
}

@keyframes animate {
    to {
        transform: rotate(1turn);
    }
}

</style>

	<div class="loader">
  <div class="face">
    <div class="circle"></div>
  </div>
  <div class="face">
    <div class="circle"></div>
  </div>
  <div>
  <p align='center' style='font-size:15px; color:red;'>  YASHIL </p>
</div>

</div>

''',height=100,)
TITLE()
TITLE_SIDEBAR()
uploaded_file = st.file_uploader("Choose a exel file") 
placeholder0 = st.empty()
if uploaded_file is not None:
    dataframe = pd.read_excel(uploaded_file,)
    placeholder0.write(dataframe)
    Data = dataframe.values
    r , w = Data.shape
    
col11, col21, col31 = st.columns([4,1,4])
cost = 200000
with col11:
    if uploaded_file is not None:
        cost = 200000+r*100
    st.write(f"WE DO THIS JUST WITH:  {cost}  Rials")
with col21:
    placeholder111 = st.empty()
    KEYpay = placeholder111.button('pay',key='key11') 
with col31:
    st.header(" ")
    
col1, col2, col3 = st.columns([4,1,4])

with col1:
    st.header(" ")
   

with col2:
    st.header(" ")
    placeholder1 = st.empty()
    KEY = placeholder1.button('start',key='key1') 
    

with col3:
    st.header(" ")
    


itr=0

if KEY and uploaded_file is not None:
    placeholder0.empty()
    placeholder1.empty()
    placeholder = st.empty()
    with placeholder.container():
        components.html('''
 <style>
* {
  border: 0;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  font-size: calc(16px + (24 - 16)*(100vw - 320px)/ (1280 - 320));
}

body, .preloader {
  display: flex;
}

body {
  background:  #ffffff;
  color: #3df1f1;
  font: 1em Dosis, sans-serif;
  height: 100vh;
  line-height: 1.5;
  perspective: 40em;
}

.preloader {
  animation: tiltSpin 8s linear infinite;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: auto;
  width: 17em;
  height: 17em;
}
.preloader, .preloader__ring {
  transform-style: preserve-3d;
}
.preloader__ring {
  animation-name: spin;
  animation-duration: 4s;
  animation-timing-function: inherit;
  animation-iteration-count: inherit;
  font-size: 2em;
  position: relative;
  height: 3rem;
  width: 1.5rem;
}
.preloader__ring:nth-child(even) {
  animation-direction: reverse;
}
.preloader__sector {
  font-weight: 600;
  position: absolute;
  top: 0;
  left: 0;
  text-align: center;
  text-transform: uppercase;
  transform: translateZ(7rem);
}
.preloader__sector, .preloader__sector:empty:before {
  display: inline-block;
  width: 100%;
  height: 100%;
}
.preloader__sector:empty:before {
  background: linear-gradient(transparent 45%, currentColor 45% 55%, transparent 55%);
  content: "";
}
.preloader__sector:nth-child(2) {
  transform: rotateY(12deg) translateZ(7rem);
}
.preloader__sector:nth-child(3) {
  transform: rotateY(24deg) translateZ(7rem);
}
.preloader__sector:nth-child(4) {
  transform: rotateY(36deg) translateZ(7rem);
}
.preloader__sector:nth-child(5) {
  transform: rotateY(48deg) translateZ(7rem);
}
.preloader__sector:nth-child(6) {
  transform: rotateY(60deg) translateZ(7rem);
}
.preloader__sector:nth-child(7) {
  transform: rotateY(72deg) translateZ(7rem);
}
.preloader__sector:nth-child(8) {
  transform: rotateY(84deg) translateZ(7rem);
}
.preloader__sector:nth-child(9) {
  transform: rotateY(96deg) translateZ(7rem);
}
.preloader__sector:nth-child(10) {
  transform: rotateY(108deg) translateZ(7rem);
}
.preloader__sector:nth-child(11) {
  transform: rotateY(120deg) translateZ(7rem);
}
.preloader__sector:nth-child(12) {
  transform: rotateY(132deg) translateZ(7rem);
}
.preloader__sector:nth-child(13) {
  transform: rotateY(144deg) translateZ(7rem);
}
.preloader__sector:nth-child(14) {
  transform: rotateY(156deg) translateZ(7rem);
}
.preloader__sector:nth-child(15) {
  transform: rotateY(168deg) translateZ(7rem);
}
.preloader__sector:nth-child(16) {
  transform: rotateY(180deg) translateZ(7rem);
}
.preloader__sector:nth-child(17) {
  transform: rotateY(192deg) translateZ(7rem);
}
.preloader__sector:nth-child(18) {
  transform: rotateY(204deg) translateZ(7rem);
}
.preloader__sector:nth-child(19) {
  transform: rotateY(216deg) translateZ(7rem);
}
.preloader__sector:nth-child(20) {
  transform: rotateY(228deg) translateZ(7rem);
}
.preloader__sector:nth-child(21) {
  transform: rotateY(240deg) translateZ(7rem);
}
.preloader__sector:nth-child(22) {
  transform: rotateY(252deg) translateZ(7rem);
}
.preloader__sector:nth-child(23) {
  transform: rotateY(264deg) translateZ(7rem);
}
.preloader__sector:nth-child(24) {
  transform: rotateY(276deg) translateZ(7rem);
}
.preloader__sector:nth-child(25) {
  transform: rotateY(288deg) translateZ(7rem);
}
.preloader__sector:nth-child(26) {
  transform: rotateY(300deg) translateZ(7rem);
}
.preloader__sector:nth-child(27) {
  transform: rotateY(312deg) translateZ(7rem);
}
.preloader__sector:nth-child(28) {
  transform: rotateY(324deg) translateZ(7rem);
}
.preloader__sector:nth-child(29) {
  transform: rotateY(336deg) translateZ(7rem);
}
.preloader__sector:nth-child(30) {
  transform: rotateY(348deg) translateZ(7rem);
}

/* Animations */
@keyframes tiltSpin {
  from {
    transform: rotateY(0) rotateX(30deg);
  }
  to {
    transform: rotateY(1turn) rotateX(30deg);
  }
}
@keyframes spin {
  from {
    transform: rotateY(0);
  }
  to {
    transform: rotateY(1turn);
  }
}
</style>
<div class="preloader">
  <div class="preloader__ring">
    <div class="preloader__sector">Y</div>
    <div class="preloader__sector">A</div>
    <div class="preloader__sector">S</div>
    <div class="preloader__sector">H</div>
    <div class="preloader__sector">I</div>
    <div class="preloader__sector">L</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
  </div>
  <div class="preloader__ring">
    <div class="preloader__sector">W</div>
    <div class="preloader__sector">H</div>
    <div class="preloader__sector">A</div>
    <div class="preloader__sector">T</div>
    <div class="preloader__sector">S</div>
    <div class="preloader__sector">W</div>
    <div class="preloader__sector">E</div>
    <div class="preloader__sector">B</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
  </div>
</div>                           
''',height=260,) 
    my_bar = st.progress(0)
    while itr<int(r):
         phone_no = "+98" + str(Data[itr-1][0])
         message = str(Data[itr][1])
         time.sleep(1)
         if pg.getActiveWindow().title[0:8] != 'WhatsApp' :
             web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}",1,False)
             time.sleep(7)
             if pg.getActiveWindow().title[0:8] == 'WhatsApp' :
                 time.sleep(1)
                 #pg.click(core.WIDTH / 2, core.HEIGHT / 2)
                 pg.press("enter")
                 time.sleep(0.1)
                 itr += 1
                 my_bar.progress(itr/r)
                 #st.info(f'{itr/r*100}% ...', icon="ℹ️")

                 time.sleep(0.1)
         elif pg.getActiveWindow().title[0:8] == 'WhatsApp':
              core.close_tab(0)
    else:
        placeholder.empty()
        st.session_state.get('key1')
        if pg.getActiveWindow().title[0:8] == 'WhatsApp' :   
            core.close_tab(0)
        col4, col5, col6 = st.columns([1,10,1])
        from PIL import Image
        image1 = Image.open('R.png')
        with col4:
            st.image(image1,use_column_width='always')
        with col5:
            st.success('ALL MESSAGES WERE SENT!')    
         
        with col6:
            st.image(image1,use_column_width='always')
       
        st.snow()

    

