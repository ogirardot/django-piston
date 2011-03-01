import XMLtoDict
from pprint import pprint

xml = \
'''<?xml version="1.0" encoding="utf-8"?>
<projects>
    <resource>
        <name>llalala 2</name>
        <client>100</client>
    </resource>
   <resource>
        <name>blah blah 2</name>
        <client id="82" notes="test" />
        <users>
            <id>1</id>
            <id>2</id>
        </users>
    </resource>
</projects>
'''

xml2 = \
'''<?xml version="1.0" encoding="utf-8"?>
    <response>
        <resource>
            <admins></admins>
            <managers></managers>
            <id>82</id>
            <name>toms client 1</name>
            <individuals>
                <resource>
                    <username>tom@email.co.uk</username>
                    <first_name>Tom</first_name>
                    <last_name>C</last_name>
                    <id>1</id>
                </resource>
                <resource>
                    <username>charles@mail.co.uk</username>
                    <first_name>Charles</first_name>
                    <last_name>H</last_name>
                    <id>17</id>
                </resource>
            </individuals>
        </resource>
        <resource>
            <admins></admins>
            <managers></managers>
            <id>83</id>
            <name>toms client 2</name>
            <individuals>
                <resource>
                    <username>tom@email.co.uk</username>
                    <first_name>Tom</first_name>
                    <last_name>C</last_name>
                    <id>1</id>
                </resource>
                <resource>
                    <username>charles@mail.co.uk</username>
                    <first_name>Charles</first_name>
                    <last_name>H</last_name>
                    <id>17</id>
                </resource>
            </individuals>
        </resource>
        <resource>
            <admins></admins>
            <managers></managers>
            <id>81</id>
            <name>toms client 3</name>
            <individuals>
                <resource>
                    <username>tom@email.co.uk</username>
                    <first_name>Tom</first_name>
                    <last_name>C</last_name>
                    <id>1</id>
                </resource>
            </individuals>
        </resource>
    </response>'''

xml3 = \
'''<?xml version="1.0" encoding="utf-8"?>
<response>
    <resource>
        <admins />
        <managers />
        <id>82</id>
        <name>toms client 1</name>
        <individuals />
    </resource>
</response>
'''

#pprint(XMLtoDict.fromstring(xml))
pprint(XMLtoDict.fromstring(xml2))
#pprint(XMLtoDict.fromstring(xml3))
