# Modify the variables to change main things.

# Directory of posts. You should probably just leave it alone.
POSTS_DIR = "posts"

# Amount of words used to generate slug.
SLUG_LEN = 5

# Length of excerpt in characters. Only grabbed from first paragraph.
EXCERPT_LENGTH = 100

# Amount of posts shown on title page.
POSTS_SHOWN = 3

# Name and description of blog. Description used in main page, name used throughout for branding.
BLOG_NAME = "AutoSite-Blog"
BLOG_DESCRIPTION = "This is a set of scripts that makes AutoSite by dotcomboom work as a Jekyll alternative."

# URL where blog will be made public, without the trailing slash.
BLOG_URL = "https://example.com/blog"

# used to prevent duplication of effort

import frontmatter,os,os.path,datetime,tzlocal
def load(fn):
	with open(fn) as f:
		return frontmatter.load(f)
POSTS = os.listdir(POSTS_DIR)
POSTS = [os.path.join(POSTS_DIR,x) for x in POSTS]
POSTS = {post: load(post) for post in POSTS}
for fn, post in POSTS.values():
	post["mtime"]=datetime.datetime.fromtimestamp(os.path.getmtime(fn),tzlocal.get_localzone()).isoformat()
