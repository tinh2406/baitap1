import numpy as np
import matplotlib.pyplot as plt

def plot(frame,l,r,nguong_loc):
    x = np.arange(len(frame))*0.02
    # z = ['red' if i<l or i>r else 'green' for i in x]
    frame_filter=frame[np.where(frame<nguong_loc)]
    x_filter=x[np.where(frame<nguong_loc)]
    z = ['red' if i<l or i>r else 'green' for i in x_filter]
    # Vẽ đồ thị
    plt.scatter(x_filter, frame_filter,color=z)
    # plt.scatter(x, frame,color=z)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Biểu đồ các điểm')
    # plt.show()
