import xml.etree.ElementTree as ET

file = open("tidy.html", "r", encoding="ISO-8859-1")
root = ET.fromstring(file.read())

# Top-level elements
print(root.findall("."))
