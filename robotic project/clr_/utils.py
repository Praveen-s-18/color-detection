
import numpy as np

def get_limits(color_name):
    hsv_ranges = {
        "red1": ([0, 140, 80], [10, 255, 255]),       # Lower red (avoiding orange)
        "red2": ([170, 140, 80], [180, 255, 255]),    # Upper red
        "blue": ([100, 150, 80], [130, 255, 255]),    # Blue (excluding violet)
        "green": ([40, 100, 50], [85, 255, 255]),     # Green (more sensitivity)
        "yellow": ([20, 150, 100], [35, 255, 255]),   # Yellow (avoiding skin tones)
    }

    lower = np.array(hsv_ranges[color_name][0], dtype=np.uint8)
    upper = np.array(hsv_ranges[color_name][1], dtype=np.uint8)
    
    return lower, upper

