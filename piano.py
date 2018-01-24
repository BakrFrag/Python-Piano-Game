from Tkinter import *;
import pygame;
#import Tkmessagebox;
import sys;
from playsound import playsound
pygame.init();
pygame.mixer.init();
def value1():
    num1.set("C#");
    sound=pygame.mixer.Sound("bk_1.wav");
    sound.play();
    return;
def value2():
    num1.set("D#");
    sound=pygame.mixer.Sound("bk_2.wav");
    sound.play();
    return;
def value3():
    num1.set("E#");
    sound=pygame.mixer.Sound("bk_3.wav");
    sound.play();
    return;
def value4():
    num1.set("F#");
    sound=pygame.mixer.Sound("bk_4.wav");
    sound.play();
    return;
def value5():
    num1.set("G#");
    sound=pygame.mixer.Sound("bk_5.wav");
    sound.play();
    return;
def value6():
    num1.set("H#");
    sound=pygame.mixer.Sound("bk_6.wav");
    sound.play();
    return;
def value7():
    num1.set("I#");
    sound=pygame.mixer.Sound("bk_7.wav");
    sound.play();
    return;
def value8():
    num1.set("C");
    sound=pygame.mixer.Sound("bk_8.wav");
    sound.play();
    return;
def value9():
    num1.set("D");
    sound=pygame.mixer.Sound("bk_9.wav");
    sound.play();
    return;
def value10():
    num1.set("E");
    sound=pygame.mixer.Sound("bk_10.wav");
    sound.play();
    return;
def value11():
    num1.set("F");
    sound=pygame.mixer.Sound("bk_11.wav");
    sound.play();
    return;
def value12():
    num1.set("G");
    sound=pygame.mixer.Sound("bk_12.wav");
    sound.play();
    return;
def value13():
    num1.set("H");
    sound=pygame.mixer.Sound("bk_13.wav");
    sound.play();
    return;
def value14():
    num1.set("I");
    sound=pygame.mixer.Sound("bk_14.wav");
    sound.play();
    return;
def value15():
    num1.set("J");
    sound=pygame.mixer.Sound("bk_15.wav");
    sound.play();
    return;
def value16():
    num1.set("K");
    sound=pygame.mixer.Sound("bk_16.wav");
    sound.play();
    return;
def value17():
    num1.set("L");
    sound=pygame.mixer.Sound("bk_17.wav");
    sound.play();
    return;
root=Tk();
root.title("Piano Music");
root.resizable(0,0);
num1=StringVar();
frame1=Frame(root);
frame1.pack(side=TOP);
frame2=Frame(root);
frame2.pack(side=BOTTOM);
text=Entry(frame1,textvariable=num1,bd=20,width=4,justify="center");
text.pack(side=TOP);
button1=Button(frame1,command=value1,padx=8,pady=8,height=6,fg="white",bg="black",text="C#");
button1.pack(side="left");
button2=Button(frame1,command=value2,padx=8,pady=8,height=6,fg="white",bg="black",text="D#");
button2.pack(side="left");
button3=Button(frame1,command=value3,padx=8,pady=8,height=6,fg="white",bg="black",text="E#");
button3.pack(side="left");
button4=Button(frame1,command=value4,padx=8,pady=8,height=6,fg="white",bg="black",text="F#");
button4.pack(side="left");
button5=Button(frame1,command=value5,padx=8,pady=8,height=6,fg="white",bg="black",text="G#");
button5.pack(side="left");
button6=Button(frame1,command=value6,padx=8,pady=8,height=6,fg="white",bg="black",text="H#");
button6.pack(side="left");
button7=Button(frame1,command=value7,padx=8,pady=8,height=6,fg="white",bg="black",text="I#");
button7.pack(side="left");
######bottom frame
button8=Button(frame2,command=value8,padx=16,pady=16,height=8,fg="white",bd=8,bg="black",text="A");
button8.pack(side="left");
button9=Button(frame2,command=value9,padx=16,pady=16,height=8,bd=8,fg="white",bg="black",text="B");
button9.pack(side="left");
button10=Button(frame2,command=value10,padx=16,pady=16,bd=8,height=8,fg="white",bg="black",text="C");
button10.pack(side="left");
button11=Button(frame2,command=value11,padx=16,pady=16,height=8,bd=8,fg="white",bg="black",text="D");
button11.pack(side="left");
button12=Button(frame2,command=value12,padx=16,pady=16,bd=8,height=8,fg="white",bg="black",text="E");
button12.pack(side="left");
button13=Button(frame2,command=value13,padx=16,pady=16,height=8,bd=8,fg="white",bg="black",text="F");
button13.pack(side="left");
button14=Button(frame2,command=value14,padx=16,pady=16,height=8,bd=8,fg="white",bg="black",text="G");
button14.pack(side="left");
button15=Button(frame2,command=value15,padx=16,bd=8,pady=16,height=8,fg="white",bg="black",text="H");
button15.pack(side="left");
button16=Button(frame2,command=value16,padx=16,pady=16,bd=8,height=8,fg="white",bg="black",text="I");
button16.pack(side="left");
button17=Button(frame2,command=value17,padx=16,pady=16,bd=8,height=8,fg="white",bg="black",text="J");
button17.pack(side="left");
root.mainloop();


