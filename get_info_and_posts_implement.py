import pickle
import facebook
import requests
import json
import progressbar
from get_info_and_posts import *


fanpage_XXX_comment = get_facebookFanPage_comment("your_token", "fanpage_name")
show_posts(fanpage_XXX_comment[0])


fanpage_XXX_info = fanpage_info("your_token", "fanpage_name")
show_fanpage_info(fanpage_XXX_info)


with open("fanpage_XXX_comment_pickle.txt", "wb")as c:
    pickle.dump(fanpage_XXX_comment, c)
  
with open("fanpage_XXX_info_pickle.txt", "wb")as c:
    pickle.dump(fanpage_XXX_info, c)
