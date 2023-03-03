from ste import ste
from pyplot import plot,huanluyen
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
frame_length = 0.02

def chuanHoa_STE(nameFile,where="TinHieuHuanLuyen"):
    audio,f0 = sf.read("./"+where+"/"+nameFile+".wav")
    frame_size = int(frame_length*f0)

    frames = np.array_split(audio,len(audio)//frame_size)

    ste_values = np.array([ste(frame) for frame in frames])

    return (ste_values) / (np.max(ste_values))

#------------Danh cho phone_F2 ------------

kl1,tn1 = huanluyen(chuanHoa_STE('phone_F2'),1.02,4.06)

# #-------------Danh cho phone_M2---------------
kl2,tn2 = huanluyen(chuanHoa_STE('phone_M2'),0.53,2.52)

# #-------------Danh cho studio_F2---------------
kl3,tn3 = huanluyen(chuanHoa_STE('studio_F2'),0.77,2.38)

# #-------------Danh cho studio_M2---------------
kl4,tn4 = huanluyen(chuanHoa_STE('studio_M2'),0.44,1.94)

kl = np.concatenate((kl1,kl2,kl3,kl4))
tn = np.concatenate((tn1,tn2,tn3,tn4))

# bin = [i/10000000 for i in range(10000000)]
# hist1,bin1 = np.histogram(kl,bins=bin)
# hist2,bin2 = np.histogram(tn,bins=bin)
# plt.bar(bin1[np.where(hist1>0)],hist1[np.where(hist1>0)],alpha=0.5,width=0.0000001)
# plt.bar(bin2[np.where(hist2>0)],hist2[np.where(hist2>0)],alpha=0.5,width=0.0000001)


# plt.hist(tn[np.where(tn<0.01)],bins=100,alpha=0.5)
# plt.hist(kl,bins=1000,alpha=0.5)


arr = [min(tn)+i*(max(kl)-min(tn))/100 for i in range(100)]
arr1 = [np.count_nonzero(tn<i)+np.count_nonzero(kl>i) for i in arr]

x = arr[np.argmin(arr1)]
print(x)



# plt.xlabel('STE')
# plt.ylabel('Tan suat')
# plt.show()


plt.figure()
plot(chuanHoa_STE('phone_F2'),1.02,4.06,0.005,x)#0.004

# #-------------Danh cho phone_M2---------------
plt.figure()
plot(chuanHoa_STE('phone_M2'),0.53,2.52,0.005,x)#0.002

# #-------------Danh cho studio_F2---------------
plt.figure()
plot(chuanHoa_STE('studio_F2'),0.77,2.38,0.005,x)#0.0001

# #-------------Danh cho studio_M2---------------
plt.figure()
plot(chuanHoa_STE('studio_M2'),0.44,1.94,0.005,x)#0.001

plt.show()