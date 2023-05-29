#!/usr/bin/env python
# -*-coding:Latin-1 -*
# arbitrary precision python
import math,numpy 
from mpmath  import *
mp.dps=50
for i in range (1,400):
#	print(i,(10)**(-i))
	print(i,mpf(1)+mpf(10)**(-i))
