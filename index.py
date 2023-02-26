from ste import ste
from pyplot import plot
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
frame_length = 0.02

def chuanHoa_STE(nameFile):
    audio,f0 = sf.read("./TinHieuHuanLuyen/"+nameFile+".wav")
    frame_size = int(frame_length*f0)

    frames = np.array_split(audio,len(audio)//frame_size)

    ste_values = np.array([ste(frame) for frame in frames])
    return ste_values
    return (ste_values) / (np.max(ste_values))

#------------Danh cho phone_F2 ------------

plt.figure()
plot(chuanHoa_STE('phone_F2'),1.02,4.06,0.00004)#0.004

# #-------------Danh cho phone_M2---------------
plt.figure()
plot(chuanHoa_STE('phone_M2'),0.53,2.52,0.00004)#0.002

# #-------------Danh cho studio_F2---------------
plt.figure()
plot(chuanHoa_STE('studio_F2'),0.77,2.38,0.000004)#0.0001

# #-------------Danh cho studio_M2---------------
plt.figure()
plot(chuanHoa_STE('studio_M2'),0.44,1.94,0.00001)#0.001

plt.show()