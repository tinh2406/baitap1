from pyplot import phandoan
import soundfile as sf
from index import chuanHoa_STE
import matplotlib.pyplot as plt
x=0.0006601470772844891



audio,f0 = sf.read("./TinHieuHuanLuyen/"+"phone_F2"+".wav")
phandoan(audio,chuanHoa_STE("phone_F2","TinHieuHuanLuyen"),f0,1.02,4.04,x)

audio,f0 = sf.read("./TinHieuHuanLuyen/"+"phone_M2"+".wav")
phandoan(audio,chuanHoa_STE("phone_M2","TinHieuHuanLuyen"),f0,0.52,2.52,x)

audio,f0 = sf.read("./TinHieuHuanLuyen/"+"studio_F2"+".wav")
phandoan(audio,chuanHoa_STE("studio_F2","TinHieuHuanLuyen"),f0,0.77,2.37,x)

audio,f0 = sf.read("./TinHieuHuanLuyen/"+"studio_M2"+".wav")
phandoan(audio,chuanHoa_STE("studio_M2","TinHieuHuanLuyen"),f0,0.45,1.93,x)

plt.show()
