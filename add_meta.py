from config import *
from util import *
from os import system
import re

system("rm -rf in")
system("mkdir in")

for post in POSTS:
	postc = POSTS[post]
	if not postc.get("published",False): continue
	title = postc.get("title")
	pslug = slug(title)
	excerpt = truncate(re.split("\n{2,}",postc.content)[0],postc.get("excerpt_length"))
	with open("in/{}.md".format(pslug),"w") as f:
		f.write("<!-- attrib title: {} | {} -->\n<!-- attrib description: {}-->\n<!-- attrib template: post -->\n\n".format(title,BLOG_NAME,excerpt))
		f.write("# {}\n## published {}\n\n".format(title,postc.get("pubdate","1970-01-01")))
		f.write(postc.content)
