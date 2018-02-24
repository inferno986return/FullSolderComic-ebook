#Broken code that I can't get working to write out the anchor tags into the toc.ncx.

    currentanchor = 0
    #totalanchors = len(data["pages"][currentpage]["headingAnchorName"]) #Number of anchor tags

#Write out the anchor tags.
#if (data["pages"][currentpage]["headingAnchorName"][currentanchor] in data["pages"] == True):

    #while currentanchor != totalanchors:
ncx.write('\t\t\t<navLabel>\n')
ncx.write('\t\t\t<text>' + data["pages"][currentpage]["headingAnchorName"][currentanchor] + '</text>\n')
ncx.write('\t\t\t</navLabel>\n')
ncx.write('\t\t\t<content src="' + data["pages"][currentpage]["fileName"] + data["pages"][currentpage]["headingAnchorLink"][currentanchor] + '" />\n')

    #currentanchor += 1
