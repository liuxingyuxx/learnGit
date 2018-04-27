# encoding: utf-8

from lxml import etree
import pdb

root = etree.Element("root")
print(root.tag)

root.append(etree.Element("child1"))

child2 = etree.SubElement(root,"child2")
child3 = etree.SubElement(root, "child3")

pdb.set_trace()
print(etree.tostring(root, pretty_print=True))

for child in root:
    print(child.tag)

root.insert(0, etree.Element("child0"))
start = root[:1]
end = root[-1:]
print(start[0].tag)
print(end[0].tag)

for child in root:
    print(child.tag)

"""XML支持属性的创建"""
root = etree.Element("root", interesting='totally')
print(etree.tostring(root))

#属性是无序的键值对
print(root.get("interesting"))

root.set("Hello", "LXY")
print(root.get("Hello"))

sorted(root.keys())

#如果要获得一个类似字典的对象，使用attrib属性
attributes = root.attrib
print(attributes['Hello'])

d = dict(root.attrib)
print(sorted(d.items()))
