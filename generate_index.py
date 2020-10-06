import os,re,frontmatter,datetime,uuid
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
	pslug = slug(postc)
	first_paragraph = soup(gfm.convert(postc.content),"html.parser").find("p").text.replace("\n"," ").replace("  "," ")
	excerpt = truncate(first_paragraph,postc.get("excerpt_length"))
	pubdate = postc.get("pubdate")
	ENTRIES.append(dict(title=title,pslug=pslug,pubdate=pubdate,excerpt=excerpt,mtime=postc.get("mtime")))

ENTRIES.sort(key=lambda x: (x["pubdate"],x["title"]))
ENTRIES.reverse()

os.system("mkdir -p in")
os.system("mkdir -p includes")
with open("in/index.md","w") as f:
	f.write("<!-- attrib title: {} -->\n<!-- attrib description: {} -->\n<!-- attrib template: default -->\n\n".format(BLOG_NAME,BLOG_DESCRIPTION))
	f.write("# {}\n\n".format(BLOG_NAME))
	for post in ENTRIES[:POSTS_SHOWN]:
		f.write("## [{post[title]}](./{post[pslug]}.html) - published {post[pubdate]}\n\n{post[excerpt]}\n\n".format(post=post))
	f.write("[Show older posts](archive.html)")

with open("in/archive.md","w") as f:
	f.write("""<!-- attrib title: Archive | {0} -->\n<!-- attrib description: Index of all of the posts from {0}. -->\n<!-- attrib template: default -->\n\n""".format(BLOG_NAME))
	f.write("# Archive\n\n")
	for post in ENTRIES:
		f.write("## [{post[title]}](./{post[pslug]}.html) - published {post[pubdate]}\n\n{post[excerpt]}\n\n".format(post=post))

UUID = None
if not os.path.exists(".uuid"):
	UUID = uuid.uuid4().urn
	with open(".uuid","w") as f:
		f.write(UUID)
else:
	with open(".uuid") as f:
		UUID = f.read().strip()
with open("includes/feed.atom","w") as f:
	f.write("<?xml version=1.0 encoding=\"utf-8\"?>\n\n")
	f.write("<feed xmlns=\"http://www.w3.org/2005/Atom\">\n")
	f.write("<title>"+BLOG_NAME+"</title>\n<subtitle>"+BLOG_DESCRIPTION+"</subtitle>\n")
	f.write("<link rel=\"self\" href=\""+BLOG_URL+"/feed.atom\" />\n<link href=\""+BLOG_URL+"\" />\n")
	f.write("<id>"+UUID+"</id>\n")
	f.write("<author><name>"+BLOG_NAME+"</name></author>\n")
	for post in ENTRIES[:POSTS_SHOWN]:
		f.write("<entry>\n")
		# title
		f.write("\t<title>"+post["title"]+"</title>\n")
		# link
		f.write("\t<link rel=\"alternate\" type=\"text/html\" href=\""+BLOG_URL+"/"+post["pslug"]+".html\" />\n")
		# updated
		f.write("\t<updated>"+post["mtime"]+"</updated>\n")
		# summary
		f.write("\t<summary>"+post["excerpt"]+"</summary>\n")
		# id
		f.write("\t<id>"+BLOG_URL+"/"+post["pslug"]+".html</id>\n")
		f.write("</entry>\n")
	f.write("</feed>\n")
