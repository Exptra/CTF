import os
import sys
 

flag = 105, 100, 120, 123, 111, 106, 111, 95, 108, 97, 108, 105, 95, 110, 103, 111, 112, 105, 95, 110, 100, 97, 107, 95, 109, 117, 109, 101, 116, 125
decode = "".join([chr(i) for i in flag])
print (decode)
idx = input("Masukin flag nya mhank: ")

if (idx == flag):
    print("Zeeb Mhank, udah sangar!")
else:
    print("Masih belum zeeb nih mhank!")
