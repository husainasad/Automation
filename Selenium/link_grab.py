import re
import linkGrabber

links = linkGrabber.Links("https://www.google.com/")
gb = links.find(limit=5, duplicates=False,pretty=True)
print(gb)