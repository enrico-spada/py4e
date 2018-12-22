import xml.etree.ElementTree as ET

#triple quoted string '''
#in Python it represents a multi-line string
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)   #this returns a tree object
print("Name:", tree.find("name").text)    #this expression gets more complex with deeper trees
print("email:", tree.find("email").get("hide"))
