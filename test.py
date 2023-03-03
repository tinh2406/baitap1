from pyplot import phandoan
import soundfile as sf
from index import chuanHoa_STE

audio,f0 = sf.read("./TinHieuKiemThu/"+"studio_F1"+".wav")

x=0.0008663765389061455


phandoan(audio,chuanHoa_STE("studio_F1","TinHieuKiemThu"),f0,0.68,2.15,x)
