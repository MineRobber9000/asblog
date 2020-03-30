from config import *
from util import *
from os import system
import re
import markdown
from mdx_partial_gfm import PartialGithubFlavoredMarkdownExtension
from bs4 import BeautifulSoup as soup

gfm = markdown.Markdown(extensions=[PartialGithubFlavoredMarkdownExtension()])

system("rm -rf in")
system("mkdir in")

for post in POSTS:
	postc = POSTS[post]
	if not postc.get("published",False): continue
	title = postc.get("title")
	pslug = slug(postc)
	first_paragraph = soup(gfm.convert(postc.content),"html.parser").find("p").text.replace("\n"," ").replace("  "," ")
	excerpt = truncate(first_paragraph,postc.get("excerpt_length"))
	with open("in/{}.html".format(pslug),"w") as f:
		f.write("<!-- attrib title: {} -->\n<!-- attrib description: {}-->\n<!-- attrib template: post -->\n<!-- attrib sitename: {} -->\n\n".format(title,excerpt,BLOG_NAME))
		f.write("<h1>{} (published {})</h1>\n\n".format(title,postc.get("pubdate","1970-01-01")))
		f.write(gfm.convert(postc.content).replace("<table>","<table class='table table-striped table-hover'>"))
