#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# Serializers/printers
import xmlrpc.client as xmlrpclib
import json
import yaml
from pprint import pprint

#My model
import model

if __name__ == '__main__':
    format = sys.argv[2] if len(sys.argv) == 3 else None
    print(sys.argv[1])
    model.printModel(sys.argv[1])

    data = model.finder(sys.argv[1])

    if format == 'xml':
        print(xmlrpclib.dumps((data,)))
    elif format == 'json':
        print(json.dumps(data))
    elif format == 'yaml':
        print(yaml.dump(data, default_flow_style=False, explicit_start=True, explicit_end=True))
    else:
        pprint(data)
