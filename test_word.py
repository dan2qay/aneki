from docx import Document
import httplib2
import os


url = "https://sun9-73.userapi.com/impg/8sVRvYR9nYh3BD54ROTjMRdmpPP8-7pWN6W0xw/iz4CAp2A1x4.jpg?size=56x75&quality=96&sign=e5f67fa97a4abeb7bbc27a52182de412&c_uniq_tag=7J2zlMSRlqoBppvamiFGQh2ePovXJEl9sARBGzgELh4&type=album"

h = httplib2.Http('.cache')
response, content = h.request(url)
out = open('data/img.jpg', 'wb')
out.write(content)
out.close()

document = Document(os.path.abspath('data/t.docx'))

document.add_picture('data/img.jpg')
document.save(os.path.abspath('data/t.docx'))
