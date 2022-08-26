import requests
import json
rwa_url = "https://rozgarapinew.teachx.in/post/login"

hdr = {"Auth-Key": "appxapi",
       "User-Id": "-2",
       "Authorization": "",
       "User_app_category": "",
       "Language": "en",
       "Content-Type": "application/x-www-form-urlencoded",
       "Content-Length": "227",
       "Accept-Encoding": "gzip, deflate",
       "User-Agent": "okhttp/4.9.1"
       }

data = {"email": "7351881682", "password": ""}
res = requests.post(rwa_url, data=data, headers=hdr).json()
print(res)
userid = res["data"]["userid"]
token = res["data"]["token"]
hdr1 = {
    "Host": "rozgarapinew.teachx.in",
    "Client-Service": "Appx",
    "Auth-Key": "appxapi",
    "User-Id": userid,
    "Authorization": token
    }
print(userid)
print(token)

cour_url = "https://rozgarapinew.teachx.in/get/mycourse?userid="

res1 = requests.get("https://rozgarapinew.teachx.in/get/mycourse?userid="+userid, headers=hdr1)
b_data = res1.json()['data']
cool=""
for data in b_data:
    FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**"
    aa = f" ```{data['id']}```      - **{data['course_name']}**\n\n"
    # aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
    if len(f'{cool}{aa}') > 4096:
        print(aa)
        cool = ""
    cool += aa
print(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
editable1=input("**Now send the Batch ID to Download** : ")

sub_id_url="https://rozgarapinew.teachx.in/get/allsubjectfrmlivecourseclass?courseid="

res2 = requests.get("https://rozgarapinew.teachx.in/get/allsubjectfrmlivecourseclass?courseid="+editable1, headers=hdr1).json()
b_data1 = res2["data"]
print(b_data1)
#b_data1 = res2.json()['data']
#print(b_data1)
SubiD=input("Enter the Subject Id Show in above Response")
#Class_url = "https://rozgarapinew.teachx.in/get/alltopicfrmlivecourseclass?courseid=16&subjectid="

res3 = requests.get("https://rozgarapinew.teachx.in/get/alltopicfrmlivecourseclass?courseid="+editable1,"&subjectid="+SubiD, headers=hdr1)

b_data2 = res3.json()['data']
#print(b_data2)
vj = ""
for data in b_data2:
    tids = (data["topicid"])
    idid = f"{tids}&"
    if len(f"{vj}{idid}") > 4096:
        ##await m.reply_text(idid)
        vj = ""
    vj += idid
print(vj)
vp = ""
for data in b_data2:
    tn = (data["topic_name"])
    tns = f"{tn}&"
    if len(f"{vp}{tn}") > 4096:
        ##await m.reply_text(tns)
        vp = ""
    vp += tns
print(vp)
cool1 = ""
BBB =''
for data in b_data2:
    t_name = (data["topic_name"])
    tid = (data["topicid"])
    zz = len(tid)
    BBB = f"{'**TOPIC-ID    - TOPIC     - VIDEOS**'}\n"
    hh = f"```{tid}```     - **{t_name} - ({zz})**\n"

    #         hh = f"**Topic -** {t_name}\n**Topic ID - ** ```{tid}```\nno. of videos are : {zz}\n\n"

    if len(f'{cool1}{hh}') > 4096:
        ##await m.reply_text(hh)
        cool1 = ""
    cool1 += hh
print(BBB,cool1)

#TopicId = input(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")
TopicId=input("Enter the Topic id shown above : \n")
hdr1 = {
    "Host": "rozgarapinew.teachx.in",
    "Client-Service": "Appx",
    "Auth-Key": "appxapi",
    "User-Id": userid,
    "Authorization": token
    }
import json
res4 = requests.get("https://rozgarapinew.teachx.in/get/livecourseclassbycoursesubtopconceptapiv3?topicid="+TopicId+"&start=-1&conceptid=1&courseid="+editable1+"&subjectid="+SubiD, headers=hdr1).json()

#data=res4["data"]
topicid = res4["data"]
vj = ""
for data in topicid:
    tids = (data["Title"])
    idid = f"{tids}"
    if len(f"{vj}{idid}") > 4096:
        ##await m.reply_text(idid)
        vj = ""
    vj += idid
#print(vj)
vp = ""

for data in topicid:
    tn = (data["download_link"])
    tns = f"{tn}"
    if len(f"{vp}{tn}") > 4096:
        vp = ""
    #print("Download Links: \n", tns)
    #vp += tns

cool2 = ""
BBB1 =''
for data in topicid:
    t_name = (data["download_link"])
    tid = (data["Title"])
    zz = len(tid)
    #BBB1 = f"{'**Title   -Download Links   - VIDEOS**'}\n"
    hh = f"{tid}&{t_name}\n"

    #         hh = f"**Topic -** {t_name}\n**Topic ID - ** ```{tid}```\nno. of videos are : {zz}\n\n"

    if len(f'{cool2}{hh}') > 4096:
        ##await m.reply_text(hh)
        cool2 = ""
    cool2 += hh
print(BBB1,hh)
pwd = "638udh3829162018"
IV = "fedcba9876543210"
cte = "oYRgd1NAzpn2n8Z+D6nD+kmz+BAsfTSAixCRG9JbvLpMOG2q8GSAQhOPJexPMXA/mLYzQC6pfsTFvFIZE+jczneuXYH/n5vr7PBUg7f/xag=:ZmVkY2JhOTg3NjU0MzIxMA=="
