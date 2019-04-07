from config import *
import re
def slug(title):
	return "-".join([x.strip() for x in re.sub(r"[^\w]","-",title.lower()).split("-") if x.strip()][:SLUG_LEN]).lower()

def truncate(content,length=EXCERPT_LENGTH):
	if length is None: length = EXCERPT_LENGTH # hacky workaround because defaults don't work how I think they do
	if len(content)<=length: return content
	return content[:length-3].rstrip()+"..."
