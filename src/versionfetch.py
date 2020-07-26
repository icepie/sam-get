import xml.etree.ElementTree as ET
import requests

def getlatestver(region, model):
    r = requests.get("http://fota-cloud-dn.ospserver.net/firmware/" + region + "/" + model + "/version.xml")
    root = ET.fromstring(r.text)
    vercode = root.find("./firmware/version/latest").text
    vc = vercode.split("/")
    if len(vc) == 3:
        vc.append(vc[0])
    if vc[2] == "":
        vc[2] = vc[0]
    return "/".join(vc)
