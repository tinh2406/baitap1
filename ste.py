import numpy as np

def ste(frame):
    """
    Tính Short-Time Energy (STE) trên một khung âm thanh.
    
    Args:
        frame (numpy array): mảng chứa các mẫu âm thanh trong khung
        
    Returns:
        energy (float): giá trị STE của khung âm thanh đó
    """
    # tính tổng bình phương của các mẫu trong khung
    energy = np.sum(frame**2)
    
    # chuẩn hóa năng lượng bằng cách chia tổng bình phương cho số mẫu trong khung
    energy = energy / len(frame)
    
    return energy