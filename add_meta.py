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
	excerpt = truncate(re.sub(r"\[([^\]]+)\](?:\([^)]+\)|\[([^\]]+)\])",r"\g<1>",re.split("\n{2,}",postc.content)[0].replace("\n"," ").replace("  "," ")),postc.get("excerpt_length"))
	with open("in/{}.md".format(pslug),"w") as f:
		f.write("<!-- attrib title: {} -->\n<!-- attrib description: {}-->\n<!-- attrib template: post -->\n<!-- attrib sitename: {} -->\n\n".format(title,excerpt,BLOG_NAME))
		f.write("# {} (published {})\n\n".format(title,postc.get("pubdate","1970-01-01")))
		f.write(postc.content)
