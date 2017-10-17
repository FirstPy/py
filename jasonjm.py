# -*- coding: utf-8 -*-
import json
l={"items":[{"dateEnd":"2017-10-12","dateStart":"2017-10-12","duration":720,"from":"SHA","to":"BJS"}],"sysCode":"ADP"}
encoded_json=json.dumps(l)
print encoded_json
decode_json=json.loads(encoded_json)
print type(decode_json)
print decode_json