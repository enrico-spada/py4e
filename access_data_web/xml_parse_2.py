import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''


stuff = ET.fromstring(input)
#let's search for all the user tags below users
user_list = stuff.findall("users/user")   #note that it returns a list of tags! not a list of strings
print("User count:", len(user_list))
for item in user_list:
    print("Name: ", item.find("name").text)
    print("Id: ", item.find("id").text)
    print("Attribute: ", item.get("x"))
