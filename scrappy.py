import base64
import json

image = base64.decodestring(json.dumps(data)["image"])
