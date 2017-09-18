import facebook
import requests
import json
import progressbar


def fanpage_info(token_string, fan_page_name):
    token = token_string
    graph = facebook.GraphAPI(access_token = token, version = 2.7)
    id_string = '%s?fields=id,name,fan_count,birthday,likes'%(fan_page_name)
    post = graph.get_object(id = id_string)
    return(post)
    
    
def show_fanpage_info(post):
    fan_page_id = post["id"]
    fan_page_name = post["name"]
    fan_page_fan_count = post["fan_count"]
    fan_page_birthday = post["birthday"]

    print("ID : ", fan_page_id)
    print("Name : ", fan_page_name)
    print("Fan count : ", fan_page_fan_count)
    print("Fan page created date : ", fan_page_birthday)
    print(" ")
    print("********likes********")
    fan_page_like_fan_page = post["likes"]["data"]
    for info in fan_page_like_fan_page:
        print(info["id"], " : ", info["name"])
        

def get_facebookFanPage_comment(token_string, fan_page_name):
    token = token_string
    graph = facebook.GraphAPI(access_token = token, version = 2.7)
    id_string = "%s?fields=posts{comments{id,message,created_time,like_count,reactions{username},from},created_time,message,likes}"%(fan_page_name)
    post = graph.get_object(id = id_string)
    
    #create list containing all posts messages, comments, etc.
    posts_list = []
    for p in post["posts"]["data"]: #page1
        posts_list.append(p)
    
    post2 = requests.get(post["posts"]['paging']['next']).json() #page2
    for p in post2["data"]:
        posts_list.append(p)

    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength) #page2~end
    post2_end = post2
    page_count = 3
    while True:
        if "paging" in post2_end:
            new_page = requests.get(post2_end['paging']['next']).json()
            for data in new_page["data"]:
                posts_list.append(data)
            bar.update(page_count)
            page_count += 1
            post2_end = new_page
        else:
            break
    return(posts_list)
    
    
def show_facebookFanPage_comment(d):   
    post_created_time = d["created_time"]
    print(post_created_time)

    likes = d["likes"]["data"]
    post_like_count = len(likes)
    print("like count : ", post_like_count)
    #for person in likes:
    #    print(person["id"], person["name"])

    if "message" in d.keys():
        message = d["message"]
        print("message : ", message, "\n")
    if "comments" in d.keys():
        comment = d["comments"]["data"]
        for c in comment:
            fan_name = c["from"]["name"]
            fan_id = c["from"]["id"]
            fan_comment = c["message"]
            fan_comment_time = c["created_time"]
            fan_like = c["like_count"]

            print("name : ", fan_name)
            print("id : ", fan_id)
            print("comment : ", fan_comment)
            print("time : ", fan_comment_time)
            print("like : ", fan_like, "\n")
            #print(c)

    print("   ")
    print("=================")
    #print(list(d.keys()))    
