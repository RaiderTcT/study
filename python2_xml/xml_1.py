# -*- coding: utf8 -*-
import xml.etree.ElementTree as ET

xml_1 = """<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor>
        <name>John Cleese</name>
        <fictional:character>Lancelot</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <fictional:character>Sir Robin</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Commander Clement</fictional:character>
    </actor>
</actors>
"""
root = ET.XML(xml_1)
# xml 命名空间
# for actor in root.findall("{http://people.example.com}actor"):
#     name = actor.find('{http://people.example.com}name')
#     print name.text
#     for char in actor.findall('{http://characters.example.com}character'):
#         print '|-->', char.text

ns = {"real_person": "http://people.example.com",
      "role": "http://characters.example.com"}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print name.text
    for char in actor.findall('role:character', ns):
        print " |-->", char.text




