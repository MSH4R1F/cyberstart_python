import xml.etree.cElementTree as elementtree

root = elementtree.Element("root")
elementtree.SubElement(root, "country",name = "United States of America")
elementtree.SubElement(root, "country",name = "United Kingdom")
elementtree.SubElement(root, "country",name = "Panama")

xml_code = elementtree.ElementTree(root)
xml_code.write("/tmp/vulnerable-countries.xml")
