#!/usr/bin/env python3

import os
import json
from templates import login_page

print("Content-Type: text/html\n")
print(json.dumps(dict(os.environ), indent=2))
print(login_page())

