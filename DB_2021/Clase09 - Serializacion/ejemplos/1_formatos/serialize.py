#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# Serializers/printers
import json
from pprint import pprint

# My model
import model

if __name__ == '__main__':
    # Uso: serialize "Artista" formato
    # Formato puede ser: xml, json, yaml
    # Sino, solamente hace un pprint de los datos
    format = sys.argv[2] if len(sys.argv) == 3 else None

    data = model.finder(sys.argv[1])

    if format == 'json':
        print(json.dumps(data))
    else:
        pprint(data)
