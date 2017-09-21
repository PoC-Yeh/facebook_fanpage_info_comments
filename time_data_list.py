from datetime import datetime
from datetime import timedelta
import progressbar


def time_post_data_list(fanpage_data):
    #posts created_time, likes_count, comments_count, message
    posts_list = []
    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
    page_count = 1
    
    for p in fanpage_data:
        inside = []

        #time converting
        datetime_object = datetime.strptime(p["created_time"], '%Y-%m-%dT%H:%M:%S%z')
        new_time = datetime_object + timedelta(hours = 8)
        new_time = new_time.isoformat(" ")[:-6]
        inside.append(new_time)

        #likes_count
        try:
            inside.append(len(p["likes"]["data"]))
        except:
            inside.append(0)

        #comments_count
        if "comments" in p:
            inside.append(len(p["comments"]["data"]))
        else:
            inside.append(0)

        #message
        try:
            inside.append(p["message"])
        except:
            inside.append("none")
        
        posts_list.append(inside)
        bar.update(page_count)
        page_count += 1

    return(posts_list)
