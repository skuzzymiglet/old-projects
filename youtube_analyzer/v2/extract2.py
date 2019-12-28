from lxml import html
from lxml.etree import tostring
import unicodedata, datetime, pickle
from dateutil.parser import parse

page = open("watch-history.html", "r")
doc = html.document_fromstring(page.read())
dumpfile = open("dump.dat", "wb")

divs = doc.xpath("//div[contains(@class, 'outer-cell')]")

extract_dict = {
    "video": "//a[contains(@href, 'watch')]",
    "channel": "//a[contains(@href, 'channel')]",
    "timestamp": "//*[contains(., 'GMT')]/text()",
    "video_href": "string(//a[contains(@href, 'watch')]/@href)",
    "channel_href": "string(//a[contains(@href, 'channel')]/@href)",
    "video_id": "string(//a[contains(@href, 'watch')]/@href)",
    "channel_id": "string(//a[contains(@href, 'channel')]/@href)"
    }

videos = []
EPOCH = datetime.datetime.utcfromtimestamp(0)

def _datetime_to_timestamp(dt):
    return (dt.replace(tzinfo=None) - EPOCH).total_seconds()


for div in divs:
    incomplete = False
    div_doc = html.document_fromstring(tostring(div))
    div_dict= {}
    for info in extract_dict:
        try:
            div_dict[info] = div_doc.xpath(extract_dict[info])[0].text
        except AttributeError:
            if info == "timestamp":
                datetime = ""
                for i in div_doc.xpath(extract_dict[info]):
                    #datetime += unicodedata.normalize("NFKD", str(i))
                    datetime += str(i)
                try:
                    datetime = datetime.split("\xa0")[1]
                except IndexError:
                    datetime = datetime.split("removed")[1]
                div_dict["datetime"] = datetime
                datetime = parse(datetime)
                div_dict[info] = _datetime_to_timestamp(datetime)
                div_dict["week"] = datetime.strftime("W%W %Y")
                div_dict["month"] = datetime.strftime("%b %Y")
            elif "href" in info:
                div_dict[info] = div_doc.xpath(extract_dict[info])
            elif info == "video_id":
                div_dict[info] = div_doc.xpath(extract_dict[info]).split("=")[1]
            elif info == "channel_id":
                div_dict[info] = div_doc.xpath(extract_dict[info]).split("/")[4]
        except IndexError:
            incomplete = True
            div_dict[info] = "###"

    if not incomplete:
        videos.append(div_dict)

videos = list(reversed(videos))
print(videos[678])
pickle.dump(videos, dumpfile)
dumpfile.close()
