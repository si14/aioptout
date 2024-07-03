#!/usr/bin/env python

from tomlkit import dump as toml_dump, load as toml_load, document as toml_document, aot as toml_aot
import json

with open("known_robots_reference.toml", 'rb') as input_:
    doc = toml_load(input_)

sorted_bots = toml_aot()

for bot in sorted(doc['known_robots'], key=lambda x: x['company']):
    sorted_bots.append(bot)

sorted_doc = toml_document()
sorted_doc.append('known_robots', sorted_bots)

with open("static/known_robots.toml", 'w') as toml_output:
    toml_dump(sorted_doc, toml_output)

with open("static/known_robots.json", 'w') as json_output:
    json.dump(sorted_doc, json_output, indent=2)
