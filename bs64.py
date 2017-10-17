# -*- coding: utf-8 -*-
import base64
info='马浩'
bm=base64.b64encode(info)
print bm
mh=base64.b64decode(bm)
print mh