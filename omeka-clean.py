import requests
from pyld import jsonld
import json

# get document and context separately, as CORS not currently set on
# 52.210.35.27

doc = requests.get('http://52.210.135.27/api/item_sets/15').json()
context = requests.get('http://52.210.135.27/api-context').json()

# inline the JSON content from the Items within the ItemSet
for item in doc['dcterms:hasPart']:
    idx = doc['dcterms:hasPart'].index(item)
    doc['dcterms:hasPart'][idx] = requests.get(item['@id']).json()

# Compact the JSONLD
compacted = jsonld.compact(doc, context)

# Replace xx prefix with oa, as 52.210.35.27 runs the 1.0.0.beta2 which does
# not have the fix to allow namespaces to be added beginning with 'o'
compacted_dump = json.dumps(compacted,
                            indent=2,
                            sort_keys=True).replace('xx', 'oa')

print compacted_dump
