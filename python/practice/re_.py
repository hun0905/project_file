import re


para = '''Date: Mon, 28 Sep 2020 12:38:45 +0800
To: erwin11115@gmail.com
From: =?Big5?B?sk2kaq7VsMiwVK6nqHSyzg==?= <nthumsg@my.nthu.edu.tw>
Subject: <NTHU Bulletin Board>
Message-ID: <32d4189fc5f13fa00b8c065a7281314b@localhost.localdomain>
X-Priority: 3
X-Mailer: PHPMailer [version 1.73]
MIME-Version: 1.0
Content-Type: multipart/alternative;
	boundary="b1_32d4189fc5f13fa00b8c065a7281314b"
--b1_32d4189fc5f13fa00b8c065a7281314b
Content-Type: text/plain; charset = "Big5"
Content-Transfer-Encoding: 8bit
Information of NTHU(Student)
清華大學訊息發佈(全校暨學生版)
This is a HTML-formatted message
此為HTML格式的郵件
Subject
公告主旨
10/1-10/2, the Main Library and the Branches are closed
“My Journey to Taiwanese Folk Music” with Mr. Jian Shangren
First prize NTD10,000【Exhibition of High Quality SDGs Practical Achievements】 solicitation starts from now until 9/28!
10/1(四)至10/3(六) 中秋節連假期間垃圾清運時間表
【重要公告】10/01-10/02中秋假期，總圖書館、各分館及夜讀區閉館
109年公共區域修繕工程~南門入口AC、水木旁人行道施工公告
【歡迎報名】2020 清大生醫中心 流式細胞儀教育訓練 Flow Cytometry and Cell Sorter Workshop
【科法所】109/10/5國民法官法新法說明會，歡迎報名參加！
【演講】2020年度孫運璿科技講座，邀請各領域重量級講者蒞臨分享，睽違已久精采可期，歡迎踴躍報名參加！
簡上仁的台灣音樂之旅－說唱咱台灣~9/29演講活動@總圖書館清沙龍
【清大好聲音】唱出給你有力量追夢的歌，還有機會獲得西提、聚火鍋、星巴克餐卷。報名只到9/30喔！！趕緊手刀報起來！
【教你好夢正酣的秘笈-研究生舒眠振興方案】10/24早上9點
最後1天！優選１萬元【大學生優質SDGs實踐成果展】徵件開跑！快來看看你曾經做過的事是否符合資格吧， 不論是小組、服學、課程實作， 都可報名參展。
2020年賽普勒斯國基發明展-參展辦法
【eLearn數位學習平台操作教學】熱烈加場10/13(二) 下午2點~5點(校本部計中二樓電腦教室)：課程將說明如何將平台多元功能化繁為簡、事半功倍，節省您建置課程的時間！歡迎老師和助教、助理線上報名。
獻上「最難的一堂課」影片，感謝為教育貢獻的教師及教育工作者，祝教師節快樂
【歡迎報名】科技法律研究所 招生說明會(新竹場)109年9月29日 (二) 12：10-14：10
This message was sent automatically by the mail system. Please do not reply. Inquiries regarding the messages should be directed to the issuing unit.
Please do not forward this message to other university students to avoid duplicated messages.
此為系統自動發信，請勿直接回信，如有問題，請洽各發佈單位。
請勿再度將此信轉發給校內學生，以避免信件重複發送。
--b1_32d4189fc5f13fa00b8c065a7281314b
Content-Type: text/html; charset = "Big5"
Content-Transfer-Encoding: 8bit
<html>
				<head>
			<title>訊息系統</title>
			<meta http-equiv="Content-Type" content="multipart/alternative; charset=big5" />
			<META HTTP-EQUIV="Content-Style-Type" CONTENT="text/css">
				</head>
				<body>
			<div align="center">
					<table width="90%" border=0>
				<!--
				<tr>
						<td style="font-size:18pt; font-family:標楷體; letter-spacing:2pt;"><center>清華大學訊息發佈 Information of NTHU<br>(全校學生 Student)</center></td>
				</tr>
				-->
				<tr>
						<td style="letter-spacing:2pt;">
					<!--
					<center style="font-size:18pt;">如需閱讀英文訊息，請拉至信件下方點閱。</center>
					-->
					<center style="font-size:8pt; color:red; font-family:Time New Roman;">For English version, please scroll down through the Chinese version.</center>
						</td>
				</tr>
				<tr>
						<td align="right">2020-09-28 12PM</td>
				</tr>
					</table>
					<table width="95%" border=0>
				<tr>
						<td colspan="2" style="font-size:10pt; font-family:Time New Roman;">Chinese Version</td>
				</tr>
					</table>
					<table width="90%" border=1 style="margin-bottom:30px; word-wrap:break-word; word-break:break-word;" cellpadding=8>
				<tr>
						<!--
						<td style="width:30%;background-color: #cc99ff;font-size:14pt; font-family:標楷體;">發佈單位Department</td><td style="background-color:#cc99ff;font-size:14pt; font-family:標楷體;">公告主旨Subject (欲知詳情，請點選以下超連結 For more information, please click on the link below)</td>
						-->
						<td style="background-color:#cc99ff;font-size:14pt; font-family:標楷體;">公告主旨 (欲知詳情，請點選以下超連結)</td>
				</tr><tr><td style='font-size:14pt; font-family:標楷體; background-color: #ccccff'><b>&nbsp;&nbsp;行政事務通知</b></td></tr><tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL2FmZmFpcnMuc2l0ZS5udGh1LmVkdS50dy9wLzQwNi0xMTY1LTE4NzUwMyxyMTI3LnBocD9MYW5nPXpoLXR3&b=DGREBV/c%d1023825583016063/vsghy/26149438542298/DFGBB14135-03' target='_new'>10/1(四)至10/3(六) 中秋節連假期間垃圾清運時間表</a></td></tr>
<tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL3d3dy5saWIubnRodS5lZHUudHcvbmV3cy9uZXdzX2RlZmF1bHQuaHRtbCNyc3NfbmV3cy54bWw/MTA1OQ==&b=DGREBV/c%d1023825583016063/vsghy/26149441465292/DFGBB14488-13' target='_new'>【重要公告】10/01-10/02中秋假期，總圖書館、各分館及夜讀區閉館</a></td></tr>
<tr><td style='font-size:14pt; font-family:標楷體; background-color: #ccccff'><b>&nbsp;&nbsp;修繕工程</b></td></tr><tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL2NvbnN0cnVjLnNpdGUubnRodS5lZHUudHcvcC80MDYtMTE2Ny0xODc4MTcscjk5Mi5waHA/TGFuZz16aC10dw==&b=DGRECV/c%d1023825583016063/vsghy/26149440531827/DFGBB14135-02' target='_new'>109年公共區域修繕工程~南門入口AC、水木旁人行道施工公告</a></td></tr>
<tr><td style='font-size:14pt; font-family:標楷體; background-color: #ccccff'><b>&nbsp;&nbsp;演講訊息</b></td></tr><tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL2Jtc2Uuc2l0ZS5udGh1LmVkdS50dy9wLzQwNi0xMTk0LTE4NzYzMixyMTA1Mi5waHA=&b=DGREDV/c%d1023825583016063/vsghy/26149439477007/DFGBB14293-10' target='_new'>【歡迎報名】2020 清大生醫中心 流式細胞儀教育訓練 Flow Cytometry and Cell Sorter Workshop</a></td></tr>
<tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQUlwUUxTZFBLMndPWUstWmtXTXY0UXdVZnlyQ29GMWhELVN5SkFYekEtX0dmZkJ4bmYzcjR3L3ZpZXdmb3Jt&b=DGREDV/c%d1023825583016063/vsghy/26149443472630/DFGBB14354-01' target='_new'>【科法所】109/10/5國民法官法新法說明會，歡迎報名參加！</a></td></tr>
<tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL3N1bnNwZWVjaC5zaXRlLm50aHUuZWR1LnR3L3AvNDIzLTE0NDgtMjk5My5waHA=&b=DGREDV/c%d1023825583016063/vsghy/26149443472826/DFGBB14354-01' target='_new'>【演講】2020年度孫運璿科技講座，邀請各領域重量級講者蒞臨分享，睽違已久精采可期，歡迎踴躍報名參加！</a></td></tr>
<tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL3d3dy5saWIubnRodS5lZHUudHcvbmV3cy9uZXdzX2RlZmF1bHQuaHRtbCNyc3NfbmV3cy54bWw/MTA2MA==&b=DGREDV/c%d1023825583016063/vsghy/26149441465520/DFGBB14488-13' target='_new'>簡上仁的台灣音樂之旅－說唱咱台灣~9/29演講活動@總圖書館清沙龍</a></td></tr>
<tr><td style='font-size:14pt; font-family:標楷體; background-color: #ccccff'><b>&nbsp;&nbsp;各類活動</b></td></tr><tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL0NBUkVFUi5OVEhVL3Bob3Rvcy9hLjQ3MTI0MzA2Mjg5NzIxMy8zNTEzMjM5NDM4Njk3NTQ1&b=DGREFV/c%d1023825583016063/vsghy/26149441493998/DFGBB14411-17' target='_new'>【清大好聲音】唱出給你有力量追夢的歌，還有機會獲得西提、聚火鍋、星巴克餐卷。報名只到9/30喔！！趕緊手刀報起來！</a></td></tr>
<tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL2NvdW5zZWwuc2l0ZS5udGh1LmVkdS50dy9wLzQwNi0xMjUwLTE4NTg3NCxyNjYyNC5waHA=&b=DGREFV/c%d1023825583016063/vsghy/26149441494317/DFGBB14411-17' target='_new'>【教你好夢正酣的秘笈-研究生舒眠振興方案】10/24早上9點</a></td></tr>
<tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL3Jjb2xsZWdlLm50aHUuZWR1LnR3L3AvNDA0LTExMDMtMTg2MzA4LnBocD9MYW5nPXpoLXR3&b=DGREFV/c%d1023825583016063/vsghy/26149440474103/DFGBB14458-12' target='_new'>最後1天！優選１萬元【大學生優質SDGs實踐成果展】徵件開跑！快來看看你曾經做過的事是否符合資格吧， 不論是小組、服學、課程實作， 都可報名參展。</a></td></tr>
<tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cHM6Ly9vY2ljLmlpaC5udGh1LmVkdS50dy9uZXdzX2RldGFpbC5waHA/bmV3c19ya2V5PUxPMUs5SzJQR0Y=&b=DGREFV/c%d1023825583016063/vsghy/26149443486705/DFGBB14293-10' target='_new'>2020年賽普勒斯國基發明展-參展辦法</a></td></tr>
<tr><td style='font-size:14pt; font-family:標楷體; background-color: #ccccff'><b>&nbsp;&nbsp;學習資源</b></td></tr><tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cHM6Ly9iaXQubHkvZWxlYXJuMTA5MDFi&b=DGREGV/c%d1023825583016063/vsghy/26149439516924/DFGBW05833-16' target='_new'>【eLearn數位學習平台操作教學】熱烈加場10/13(二) 下午2點~5點(校本部計中二樓電腦教室)：課程將說明如何將平台多元功能化繁為簡、事半功倍，節省您建置課程的時間！歡迎老師和助教、助理線上報名。</a></td></tr>
<tr><td style='font-size:14pt; font-family:標楷體; background-color: #ccccff'><b>&nbsp;&nbsp;其他</b></td></tr><tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL0NBUkVFUi5OVEhVL3Bvc3RzLzM1NjI4NjgxMDM3MzQ2Nzg=&b=DGREOV/c%d1023825583016063/vsghy/26149443494193/DFGBB14411-17' target='_new'>獻上「最難的一堂課」影片，感謝為教育貢獻的教師及教育工作者，祝教師節快樂</a></td></tr>
<tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL250aHVpbHN0&b=DGREOV/c%d1023825583016063/vsghy/26149443482927/DFGBB14354-01' target='_new'>【歡迎報名】科技法律研究所 招生說明會(新竹場)109年9月29日 (二) 12：10-14：10</a></td></tr>
</table>
					<table width="95%" border=0 style="margin-top:30px;">
				<tr>
						<td colspan="2" style="color:red; font-size:10pt; font-family:Time New Roman;">English Version</td>
				</tr>
					</table>
					<table width="90%" border=1 style="margin-bottom:15px; word-wrap:break-word; word-break:break-word;" cellpadding=8>
				<tr>
						<td style="background-color:#cc99ff;font-size:14pt; font-family:Time New Roman;">Subject (Please click on the link below for more information)</td>
				</tr><tr><td style='font-size:14pt; font-family:Time New Roman; background-color: #ccccff'><b>&nbsp;&nbsp;Administrative Announcements</b></td></tr><tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL3d3dy5saWIubnRodS5lZHUudHcvbmV3cy9uZXdzX2RlZmF1bHRfZW4uaHRtbCNyc3NfbmV3c19lbi54bWw/MTA1OQ==&b=DGREBV/c%d1023825583016063/vsghy/26149441465307/DFGBB14488-13' target='_new'>10/1-10/2, the Main Library and the Branches are closed</a></td></tr>
<tr><td style='font-size:14pt; font-family:Time New Roman; background-color: #ccccff'><b>&nbsp;&nbsp;Lectures</b></td></tr><tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL3d3dy5saWIubnRodS5lZHUudHcvbmV3cy9uZXdzX2RlZmF1bHRfZW4uaHRtbCNyc3NfbmV3c19lbi54bWw/MTA2MA==&b=DGREDV/c%d1023825583016063/vsghy/26149441465535/DFGBB14488-13' target='_new'>“My Journey to Taiwanese Folk Music” with Mr. Jian Shangren</a></td></tr>
<tr><td style='font-size:14pt; font-family:Time New Roman; background-color: #ccccff'><b>&nbsp;&nbsp;Activities</b></td></tr><tr><td><a style='cont-color:#00008b; text-decoration:underline;' href='http://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/OT/MSG/1/1.8/MSG18001.php?a=aHR0cDovL3Jjb2xsZWdlLm50aHUuZWR1LnR3L3AvNDA0LTExMDMtMTg2MzA4LnBocD9MYW5nPXpoLXR3&b=DGREFV/c%d1023825583016063/vsghy/26149440474118/DFGBB14458-12' target='_new'>First prize NTD10,000【Exhibition of High Quality SDGs Practical Achievements】 solicitation starts from now until 9/28!</a></td></tr>
					</table>
					<table width="90%" border=0 style="margin-top:15px;">
				<tr>
						<td style="color:#680000;font-size:12pt; font-family:Time New Roman;">
						This message was sent automatically by the mail system. Please do not reply. Inquiries regarding the messages should be directed to the issuing unit.<br>
						Please do not forward this message to other university students to avoid duplicated messages. 
						</td>
				</tr>
				<tr>
						<td style="color:#680000;font-size:12pt;">
						此為系統自動發信服務，請勿直接回信；如有問題，請洽各發佈單位。<br>
						請勿再度將此信轉發給校內學生，以避免信件重複發送。
						</td>
				</tr>
					</table>
			</div>
				</body>
		</html>
--b1_32d4189fc5f13fa00b8c065a7281314b--
'''


link = '(http:[^\']*)..target=..new.>([^<]*)'
result = re.findall(link,para)
for i in result:
	for j in i:
		print(j)


