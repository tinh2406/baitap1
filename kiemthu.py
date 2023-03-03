from index import chuanHoa_STE
import matplotlib.pyplot as plt
from pyplot import plot

x=0.0008663765389061455

plt.figure()
plot(chuanHoa_STE('phone_F1',where="TinHieuKiemThu"),0.53,2.75,0.005,x)#0.004

# #-------------Danh cho phone_M2---------------
plt.figure()
plot(chuanHoa_STE('phone_M1',where="TinHieuKiemThu"),0.46,3.52,0.005,x)#0.002

# #-------------Danh cho studio_F2---------------
plt.figure()
plot(chuanHoa_STE('studio_F1',where="TinHieuKiemThu"),0.68,2.15,0.005,x)#0.0001

# #-------------Danh cho studio_M2---------------
plt.figure()
plot(chuanHoa_STE('studio_M1',where="TinHieuKiemThu"),0.87,2.06,0.005,x)#0.001

plt.show()