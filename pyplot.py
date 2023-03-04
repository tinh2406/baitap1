import numpy as np
import matplotlib.pyplot as plt


def huanluyen(frame,l,r):
    x = np.arange(len(frame))*0.02

    khoanglang = frame[np.logical_or(x<l,x>r)]
    tiengnoi = frame[np.logical_and(x>l,x<r)]
    print(max(khoanglang))
    return khoanglang,tiengnoi



def plot(frame,l,r,nguong_loc,nguong):
    x = np.arange(len(frame))*0.02
    # z = ['red' if i<l or i>r else 'green' for i in x]
    frame_filter=frame[np.where(frame<nguong_loc)]
    x_filter=x[np.where(frame<nguong_loc)]


    z = ['red' if i<l or i>r else 'green' for i in x_filter]
    z_new = []
    for i in range(len(z)):
        if frame_filter[i] < nguong and z[i]=='red':
            z_new.append("yellow")
        elif frame_filter[i] < nguong and z[i]=='green':
            z_new.append("blue")
        else:
            z_new.append(z[i])
    # # Vẽ đồ thị
    plt.scatter(x_filter, frame_filter,color=z_new)
    # # plt.scatter(x, frame,color=z)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Biểu đồ các điểm')




    # hist1,bin1 = np.histogram(khoanglang,bins=20)
    # hist2,bin2 = np.histogram(tiengnoi,bins=20)
    # plt.plot(bin1[0:20],hist1)
    # plt.plot(bin2[0:20],hist2)
    # plt.xlabel('STE')
    # plt.ylabel('Tan suat')

def phandoan(signal,ste,f,l,r,nguong):
    plt.figure()
    plt.plot(np.array(range(len(signal)))/f,signal)

    plt.axvline(x=l,color='green')
    plt.axvline(x=r,color='green')

    left=[]
    right=[]

    for i in range(1,len(ste)-1):
        if ste[i]<nguong and ste[i+1]>nguong and ste[i-1]<nguong:
            right.append((i+0)*0.02)
        if ste[i]<nguong and ste[i+1]<nguong and ste[i-1]>nguong:
            left.append(i*0.02)
    for i in right:
        plt.axvline(x=i,color='red')
    for i in left:
        plt.axvline(x=i,color='yellow')

    # plt.show()