import json

data=open('sample-data.json').read()
print(
    """
    Interface Status
    ================================================================================
    DN                                                 Description           Speed    MTU
    -------------------------------------------------- --------------------  ------  ------
    """
)
j = json.load(data)

for k in j["imdata"]:
  dn = k["l1PhysIf"]["attributes"]["dn"]
  descr = k["l1PhysIf"]["attributes"]["descr"]
  speed = k["l1PhysIf"]["attributes"]["speed"]
  mtu = k["l1PhysIf"]["attributes"]["mtu"]

  print("{:50} {:20} {:7} {:6}".format(dn,descr,speed,mtu))