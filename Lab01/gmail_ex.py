from gmail import GMail, Message
from random import choice

gmail = GMail('ngovankhanh108@gmail.com','Khanhart108')

html_content = """ <p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<h2 style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></h2>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Em ch&agrave;o thầy, t&ecirc;n em l&agrave; Ng&ocirc; Văn Kh&aacute;nh</p>
<p style="text-align: left;">H&ocirc;m nay em viết mail n&agrave;y để xin thầy nghỉ học vì {{sickness}} <img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Em xin cảm ơn</p>
<p style="text-align: left;">Kh&aacute;nh Ng&ocirc;</p>
"""

a = ["em bị ốm","em đưa gấu đi xem phim","em đưa gấu đi uống trà đá","trời mưa to em không đi học được"]
sickness = choice(a)
html_content_to_send = html_content.replace("{{sickness}}", sickness)

msg = Message('Test Message',to='20130075@student.hust.edu.vn',html=html_content_to_send)
gmail.send(msg)