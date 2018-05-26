#!/usr/bin/evn python3
#coding=utf-8


import urllib.request
import re

def search_desired(line, f):
    m1 = re.match(r"(.*)(https://pan.baidu.com/(.*))(</a>)(.*)+", line)
    m2 = re.match(r'(.*)20140803" >[：| ]?([0-9a-z]+)(<br>|</div>)', line)  
    m3 = re.match(r'(.*)<br>(([0-9]+.)?(王菲)?《(.*?)》)(.*)', line)  
    if m1 and m2 and m3:
#    if m1 and m2:
#        print(m3.group(0))
#        print(m3.group(1))
#        print(m3.group(2))
#        print(m3.group(3))
#        print(m3.group(4))
#        print(m3.group(5))
#        print(m3.group(6))
#        name = m1.group(2).strip('\n\r')
#        code = m2.group(2).strip('\n\r')
        name = m1.group(2).strip()
        code = m2.group(2).strip()
        title = m3.group(2).strip()
        print(title+", "+name+", "+code+"\n")
        f.write(title+", "+name+", "+code+"\n")
#        print(name+", "+code+"\n")
#        f.write(name+", "+code+"\n")
              
    

def process_file(reader, f):
    for line in reader:
        line = line.decode("utf-8")
        line = line.strip()
        search_desired(line, f)
        
if __name__=="__main__":
    '''
            从百度贴吧上搜索到王菲的专辑，用这个工具摘取链接
            【华语】呕心沥血整理出94张王菲专辑
    http://tieba.baidu.com/p/5493737812?pn=1
    '''
    
    f = open("./result.txt", "w")

#    url="http://tieba.baidu.com/p/5493737812?pn=2"
#    print(url)
#    webpage = urllib.request.urlopen(url)
#    process_file(webpage, f)
#    webpage.close()
    
    for i in range(7):
        url="http://tieba.baidu.com/p/5493737812?pn=" + str(i+1)
        print(url)
        webpage = urllib.request.urlopen(url)
        process_file(webpage, f)
        webpage.close()



#    search_desired(r'''</ul></div><div  class="d_post_content_main">        <div class="p_content  p_content p_content_nameplate"><div class="save_face_bg_hidden save_face_bg_0"><a class="save_face_card"></a>            </div>        <cc><div id="post_content_116750962321" class="d_post_content j_d_post_content  clearfix">            <img class="BDE_Image" pic_type="0" width="560" height="567" src="http://imgsrc.baidu.com/forum/w%3D580/sign=c5741db73fa85edffa8cfe2b795509d8/97993ba85edf8db1b25608830223dd54544e74d2.jpg" ><br><br>27.王菲《1994 金碟至尊精选》[WAV 整轨]<br>专辑名称：金碟至尊精选<br>专辑歌手：王靖雯 （王菲）<br>唱片公司：新艺宝<br>版    本: 日本天龙版<br>发行时间：1994年<br>专辑介绍: <br>　新艺宝唱片94年限量发行的24K 金碟版精选集，音质通透，非常稀有且少见。选曲收录了入《迟到的爱》等罕见曲目，更显珍贵。 <br>专辑曲目:<br>01 知己知彼[Europe Mix]<br>02 我愿意 <br>03 有缘的话<br>04 重燃<br>05 如风<br>06 只因喜欢Faye<br>07 梦游<br>08 冷战<br>09 请勿客气<br>10 把钥匙投进信箱<br>11 忘掉你像忘掉我<br>12 迟到的爱<br>13 中间人<br>14 KEEP IT TOGETHER<br>15 流非飞<br>16 未平复的心<br>17 天与地<br><a href="http://jump.bdimg.com/safecheck/index?url=rN3wPs8te/pjz8pBqGzzzz3wi8AXlR5g1NgdDpM6gxLzs9EQ/qifZ5Zybca//YpfAG+4Cm4FSU0="  target="_blank">https://pan.baidu.com/s/1i57vZm9</a> <img class="BDE_Smiley" pic_type="1" width="30" height="30" src="http://tb2.bdstatic.com/tb/editor/images/face/i_f36.png?t=20140803" >：lu0f<br>这个cue有问题，原因不详。</div><br></cc><br><div class="user-hide-post-down" style="display: none;"></div>        <div class="achievement_medal_section"></div></div>    <div class="core_reply j_lzl_wrapper hideLzl" style="min-height:200px"></div></div><div class="clear"></div></div><div class="l_post j_l_post l_post_bright  "  data-field='{&quot;author&quot;:{&quot;user_id&quot;:794231756,&quot;user_name&quot;:&quot;ddzh1222&quot;,&quot;name_u&quot;:&quot;ddzh1222&amp;ie=utf-8&quot;,&quot;user_sex&quot;:1,&quot;portrait&quot;:&quot;cc0364647a6831323232572f&quot;,&quot;is_like&quot;:1,&quot;level_id&quot;:9,&quot;level_name&quot;:&quot;\u9ad8\u6b4c\u731b\u8fdb&quot;,&quot;cur_score&quot;:1405,&quot;bawu&quot;:0,&quot;props&quot;:null},&quot;content&quot;:{&quot;post_id&quot;:116751643140,&quot;is_anonym&quot;:false,&quot;open_id&quot;:&quot;tieba&quot;,&quot;open_type&quot;:&quot;&quot;,&quot;date&quot;:&quot;2018-01-04 15:27&quot;,&quot;vote_crypt&quot;:&quot;&quot;,&quot;post_no&quot;:72,&quot;type&quot;:&quot;0&quot;,&quot;comment_num&quot;:1,&quot;ptype&quot;:&quot;0&quot;,&quot;is_saveface&quot;:false,&quot;props&quot;:null,&quot;post_index&quot;:1,&quot;pb_tpoint&quot;:null}}' >            <div class="user-hide-post-position"></div><div class="d_author">                    <div class="louzhubiaoshi_wrap">''', f)
    
#    search_desired(r'''</ul></div><div  class="d_post_content_main">        <div class="p_content  p_content p_content_nameplate"><div class="save_face_bg_hidden save_face_bg_0"><a class="save_face_card"></a>            </div>        <cc><div id="post_content_116954154357" class="d_post_content j_d_post_content  clearfix">            <img class="BDE_Image" pic_type="0" width="560" height="551" src="http://imgsrc.baidu.com/forum/w%3D580/sign=5749ca62b9b7d0a27bc90495fbee760d/927bbdb7d0a20cf4cbd0580f7d094b36aeaf999c.jpg" ><br><br><img class="BDE_Image" pic_type="0" width="560" height="439" src="http://imgsrc.baidu.com/forum/w%3D580/sign=420607f3bb7eca80120539efa1229712/58eabf7eca806538fcc005c39cdda144ac348236.jpg" ><br>36.王菲《1997 王菲(FAYE WONG日本版)》[WAV 整轨]<br>专辑名称：王菲97 日本版<br>专辑歌手：王菲<br>专辑日期：1997年<br>专辑语言：国语<br>地区: 日本<br>专辑介绍：<br>   《王菲》是香港歌手王菲的第十四张大碟、第五张国语大碟，也是她以“一间制作有限公司”（A Production House Ltd.）的身份加盟百代唱片的第一张大碟，于1997年9月发行。一共十首歌曲，一首是翻唱。这张大碟因为亚洲金融危机在香港销量一般，但在台湾成绩很好，而且助她的人气在中国大陆迅速上升。《王菲》发片10天全亚洲销量便超过50万。台湾总销量就超过45万张；香港为白金唱片；大马大破10万，新加坡破6万，是1997年度新马两地最畅销的女歌手专辑，累计总销量破百万。<br>此专辑为日本版：侧标为王菲侧身像，封面上的“王菲”变为“Faye Wong”。台湾再版：普通封面，侧标为“加盟百代第一张专辑”，附一张纸卡作另外封面。<br>专辑曲目：<br>01. 麻醉 <br>02. 你快乐(所以我快乐) <br>03. 闷 <br>04. 娱乐场 <br>05. 人间 <br>06. 我也不想这样 <br>07. 小题大做 <br>08. 怀念 <br>09. 扑火 <br>10. 云端<br><a href="http://jump.bdimg.com/safecheck/index?url=rN3wPs8te/pjz8pBqGzzzz3wi8AXlR5g1NgdDpM6gxJDTZv4tRHfNwKVx42Rt+ScvuBP3Gsw9C297VeXtGSXY4LM3DuEnA1dl4jr5lxXTDSK3eHANzN1gyg53x+R4b53I0JUbeLI9St2Pah4egTNMg=="  target="_blank">https://pan.baidu.com/s/1o9M11Nk</a> <img class="BDE_Smiley" pic_type="1" width="30" height="30" src="http://tb2.bdstatic.com/tb/editor/images/face/i_f36.png?t=20140803" >kvk8<br>王菲最经典的国语专辑之一</div><br></cc><br><div class="user-hide-post-down" style="display: none;"></div>        <div class="achievement_medal_section"></div></div>    <div class="core_reply j_lzl_wrapper hideLzl" style="min-height:140px"></div></div><div class="clear"></div></div><div class="l_post j_l_post l_post_bright  "  data-field='{&quot;author&quot;:{&quot;user_id&quot;:2452722572,&quot;user_name&quot;:&quot;\u540d\u5b57\u771f\u5fc3\u95f9\u5fc3\u554a&quot;,&quot;name_u&quot;:&quot;%E5%90%8D%E5%AD%97%E7%9C%9F%E5%BF%83%E9%97%B9%E5%BF%83%E5%95%8A&amp;ie=utf-8&quot;,&quot;user_sex&quot;:0,&quot;portrait&quot;:&quot;8c93e5908de5ad97e79c9fe5bf83e997b9e5bf83e5958a3192&quot;,&quot;is_like&quot;:0,&quot;level_id&quot;:1,&quot;level_name&quot;:&quot;\u4e91\u8d77\u96ea\u98de&quot;,&quot;cur_score&quot;:0,&quot;bawu&quot;:0,&quot;props&quot;:null},&quot;content&quot;:{&quot;post_id&quot;:116957028304,&quot;is_anonym&quot;:false,&quot;open_id&quot;:&quot;tieba&quot;,&quot;open_type&quot;:&quot;&quot;,&quot;date&quot;:&quot;2018-01-11 19:28&quot;,&quot;vote_crypt&quot;:&quot;&quot;,&quot;post_no&quot;:94,&quot;type&quot;:&quot;0&quot;,&quot;comment_num&quot;:0,&quot;ptype&quot;:&quot;0&quot;,&quot;is_saveface&quot;:false,&quot;props&quot;:null,&quot;post_index&quot;:20,&quot;pb_tpoint&quot;:null}}' >            <div class="user-hide-post-position"></div><div class="d_author">                <ul class="p_author">''', f)


    f.close()



