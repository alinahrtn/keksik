# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i_LTbEyRTWpo70bIVNso2xLNWDEiH6Fa
"""

n = int(input())
m = int(input())
k = int(input())
if k<n*m and k%n==0 or k%m==0:
  print("YES")
else:
  print("NO")