import configparser
conf=configparser.ConfigParser()
conf.read("1.conf")
print(conf.get("controller","host"))
print(conf.get("controller","password"))
print(conf.get("controller","port1",))
print(conf.get("controller","port2"))