#!/usr/bin/evn python3
#coding=utf-8

# 干支纪年-天干
TG_YEAR = ['庚','辛','壬','癸','甲',
      '乙','丙','丁','戊','己',]

# 干支纪年-地支
DZ_YEAR = ['申','酉','戌','亥','子','丑',
      '寅','卯','辰','巳','午','未',]

# 干支纪月 - 天干
TG_MONTH = dict({'戊癸':['甲','乙','丙','丁','戊','己',
                       '庚','辛','壬','癸','甲','乙'],
                 '甲己':['丙','丁','戊','己','庚','辛',
                       '壬','癸','甲','乙','丙','丁'],
                 '乙庚':['戊','己','庚','辛','壬','癸',
                       '甲','乙','丙','丁','戊','己'],
                 '丙辛':['庚','辛','壬','癸','甲','乙',
                       '丙','丁','戊','己','庚','辛'],
                 '丁壬':['壬','癸','甲','乙','丙','丁',
                       '戊','己','庚','辛','壬','癸']})

#
# 返回公历年的天干地支
# 输入：
#       year  - 公历年，如公元元年，year=1
#                      公元2011年，year=2011
#                      公元前1年，year=-1
#                      公元前221年，year=-220
# 输出：
#       [年天干,年地支]
# 调用示例：
#       (TG_YEAR,DZ_YEAR) = get_chinese_ear_year(2011)
def get_chinese_ear_year(year):
        if (year < 0):    # 公元前
                year = 60 - (-1) * year %60 + 1
        tg_y = year % 10
        dz_y = year % 12
        return [TG_YEAR[tg_y],DZ_YEAR[dz_y]]

       
msg=("干支纪年从东汉章帝元和二年（公元85年，{0[0]}{0[1]}年）“四分历”开始。")
print(msg.format(get_chinese_ear_year(85)))

print("公元2011年，{0[0]}{0[1]}年".format(get_chinese_ear_year(2011)))
print("公元2年，{0[0]}{0[1]}年".format(get_chinese_ear_year(2)))
print("公元元年，{0[0]}{0[1]}年".format(get_chinese_ear_year(1)))
print("公元前1年，{0[0]}{0[1]}年".format(get_chinese_ear_year(-1)))
print("公元前2年，{0[0]}{0[1]}年".format(get_chinese_ear_year(-2)))
print("公元59年，{0[0]}{0[1]}年".format(get_chinese_ear_year(59)))
print("公元60年，{0[0]}{0[1]}年".format(get_chinese_ear_year(60)))
print("公元61年，{0[0]}{0[1]}年".format(get_chinese_ear_year(61)))
print("公元前221年，{0[0]}{0[1]}年".format(get_chinese_ear_year(-221)))
print("公元19年，{0[0]}{0[1]}年".format(get_chinese_ear_year(19)))
print("公元20年，{0[0]}{0[1]}年".format(get_chinese_ear_year(20)))
print("公元1900年，{0[0]}{0[1]}年".format(get_chinese_ear_year(1900)))


for i in list(range(-100,100,1)):
        if (i == 0):
                continue
        elif (i < 0):
                print("公元前{0}年，{1[0]}{1[1]}年".format(abs(i), get_chinese_ear_year(i)))
        else:
                print("公元{0}年，{1[0]}{1[1]}年".format(i, get_chinese_ear_year(i)))
        
                
        



print(TG_MONTH['戊癸'])




#
# 取得八字
# 输入：
#       year  - 公历年，如公元元年，year=1
#                      公元2011年，year=2011
#                      公元前1年，year=0
#                      公元前221年，year=220
#       month - 公历月，1 - 12
#       day   - 公历日
#       time  - 时辰，1 - 子时(23:00 -  1:00)
#                    2 - 丑时( 1:00 -  3:00)
#                补！
# 输出：
#       [年天干,年地支,月天干,月地支,
#        日天干,日地支,时辰天干,时辰地支]
# 调用示例：
#       (TG_YEAR,DZ_YEAR) = get_chinese_ear_year(2011)
#def get_eight_character(year,month,day,time):


 
