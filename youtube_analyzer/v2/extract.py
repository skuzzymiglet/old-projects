from lxml import html
from lxml.etree import tostring

page = open("watch-history.html", "r")
doc = html.document_fromstring(page.read())

divs = doc.xpath("//div[contains(@class, 'outer-cell')]")
videos_xpath = "//a[contains(@href, 'watch')]"
channels_xpath = "//a[contains(@href, 'channel')]"
datetimes_xpath = "//*[contains(., 'GMT')]/text()"
videos = []

for div in divs:
    incomplete = False
    div_doc = html.document_fromstring(tostring(div))
    try:
        video = div_doc.xpath(videos_xpath)[0].text
    except IndexError:
        video = "#################"
        incomplete = True
    try:
        channel = div_doc.xpath(channels_xpath)[0].text
    except IndexError:
        channel = "#################"
        incomplete = True
    try:
        datetime = div_doc.xpath(datetimes_xpath)
    except IndexError:
        datetime = "#################"
        incomplete = True

    if not incomplete:
        videos.append({"video_title"})
    
#print(len(divs), len(videos), len(channels), len(datetimes))
