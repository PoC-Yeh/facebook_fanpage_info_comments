import pickle
import facebook
import requests
import json
import progressbar
from get_info_and_posts import *


fanpage_XXX_info = fanpage_info("your_token", "fanpage_name")
show_fanpage_info(fanpage_XXX_info)


fanpage_XXX_comment = get_facebookFanPage_comment("your_token", "fanpage_name")
show_posts(fanpage_XXX_comment[0])


combine = [fanpage_XXX_info, fanpage_XXX_comment]


with open("fanpage_XXX_pickle.txt", "wb")as c:
    pickle.dump(combine, c)
