import json

with open("sample-data.json", 'r') as str_json:
    data = json.loads(str_json.read())

print("""

Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------

""")
for it in data["imdata"]:
    if len(it["l1PhysIf"]["attributes"]["dn"]) == 41:
        ik = it["l1PhysIf"]["attributes"]["dn"] + ' '
        print(ik, end='                                ')
    else:
        print(it["l1PhysIf"]["attributes"]["dn"], end='                                ')
    print(it["l1PhysIf"]["attributes"]["speed"], end='   ')

    print(it["l1PhysIf"]["attributes"]["mtu"])

str_json.close()

