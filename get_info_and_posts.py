import facebook
import requests
import json
import progressbar


##################fanpge info
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
        

        

###################comments
#p1_po1_likes = post["posts"]["data"][1]["likes"]
#next_page_data(p1_po1_likes)

def next_page_data(input_key): 
    all_data_list = []
    
    for i in input_key["data"]:
        all_data_list.append(i)
    
    if "paging" in input_key.keys():
        while True:
            if "next" in input_key["paging"]:
                new_page = requests.get(input_key['paging']['next']).json()
                if "data" in new_page.keys():
                    for n in new_page["data"]:
                        all_data_list.append(n)
                input_key = new_page
            else:
                break
                
    return(all_data_list)


def update_likes_or_comments(input_key, all_data_list):  #all_data_list = next_page_data(input_key)
    input_key["data"] = all_data_list
    if "paging" in input_key.keys():
        del input_key["paging"]
        

def update(p):
    #update likes data of each post
    if "likes" in p.keys():
        p_likes = p["likes"]
        all_likes = next_page_data(p_likes)
        update_likes_or_comments(p_likes, all_likes)
    
        #update comments data of each post
    if "comments" in p.keys():
        p_comments = p["comments"]
        all_comments = next_page_data(p_comments)
        update_likes_or_comments(p_comments, all_comments)

        
def get_facebookFanPage_comment(token_string, fan_page_name):
    token = token_string
    graph = facebook.GraphAPI(access_token = token, version = 2.7)
    id_string = "%s?fields=posts{comments{id,message,created_time,like_count,reactions{username},from},created_time,message,likes}"%(fan_page_name)
    post = graph.get_object(id = id_string)
    
    #create list containing all posts messages, comments, etc.
    posts_list = []
    for p in post["posts"]["data"]: #page1
        update(p) #update likes and comments data of each post
        posts_list.append(p)
    print("posts : page 1 has been finished!")
    
    if "paging" in post["posts"].keys():
        print("moving on to page 2.")
        post2 = requests.get(post["posts"]['paging']['next']).json() #page2
        for p in post2["data"]:
            update(p)
            posts_list.append(p)
        print("posts : page 2 has been finished!")
        print("posts : if there is page 3, moving on to page 3.")

        bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength) #page2~end
        post2_end = post2
        page_count = 3
        while True:
            if "paging" in post2_end:
                new_page = requests.get(post2_end['paging']['next']).json()
                for data in new_page["data"]:
                    update(data)
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
    
 
