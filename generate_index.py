import os,re,frontmatter,datetime
from config import *
from util import *

ENTRIES = []

for post in POSTS:
	postc = POSTS[post]
	if not postc.get("published",False): continue
	title = postc.get("title")
	pslug = slug(title)
	excerpt = truncate(re.sub(r"\[([^\]]+)\](?:\([^)]+\)|\[\])",r"\g<1>",re.split("\n{2,}",postc.content)[0].replace("\n"," ").replace("  "," ")),postc.get("excerpt_length"))
	pubdate = postc.get("pubdate")
	ENTRIES.append(dict(title=title,pslug=pslug,pubdate=pubdate,excerpt=excerpt))

ENTRIES.sort(key=lambda x: x["pubdate"])
ENTRIES.reverse()
ENTRIES = ENTRIES[:POSTS_SHOWN]

os.system("mkdir -p in")
with open("in/index.md","w") as f:
	f.write("<!-- attrib title: {} -->\n<!-- attrib description: {} -->\n<!-- attrib template: default -->\n\n".format(BLOG_NAME,BLOG_DESCRIPTION))
	f.write("# {}\n\n".format(BLOG_NAME))
	for post in ENTRIES:
		f.write("## [{post[title]}](./{post[pslug]}.html) - published {post[pubdate]}\n\n{post[excerpt]}\n\n".format(post=post))
