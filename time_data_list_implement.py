from datetime import datetime
from datetime import timedelta
import progressbar
import pickle
from time_data_list import *


with open("filename", "rb")as c:
    fanpage_data = pickle.load(c)

fanpage_data_list = time_post_data_list(fanpage_data)


with open("filename2", "wb")as c:
    pickle.dump(fanpage_data_list, c)
    
    
    
