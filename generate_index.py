import os,re,frontmatter,datetime
from config import *
from util import *
import markdown
from mdx_partial_gfm import PartialGithubFlavoredMarkdownExtension
from bs4 import BeautifulSoup as soup

gfm = markdown.Markdown(extensions=[PartialGithubFlavoredMarkdownExtension()])

ENTRIES = []

for post in POSTS:
	postc = POSTS[post]
	if not postc.get("published",False): continue
	title = postc.get("title")
	pslug = slug(title)
	first_paragraph = re.split("\n{2,}",postc.content)[0].replace("\n"," ").replace("  "," ")
	# convert to real text
	first_paragraph = soup(gfm.convert(first_paragraph),"html.parser").text
	excerpt = truncate(first_paragraph,postc.get("excerpt_length"))
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
