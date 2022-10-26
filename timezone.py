
##
# Python's program to get current time MST EST UTC GMT HST
 
from datetime import datetime
import pytz
from pytz import timezone
 
mst = timezone('MST')
print("Time in MST:", datetime.now(mst))
 
est = timezone('US/Eastern')
print("Time in Eastern:", datetime.now(est))
 
cts = timezone('US/Central')
print("Time in Central:", datetime.now(cts))
 
gmt = timezone('GMT')
print("Time in GMT:", datetime.now(gmt))
 
hst = timezone('HST')
print("Time in HST:", datetime.now(hst))
