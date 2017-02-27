IIIF Presentation API:

Basic Omeka-S template:

Fields with a * are potentially useful but probably not used in MVP. These may not all be
populated on ingest of a new IIIF object. But having them stored in Omeka-S, rather than
always retrieving from the JSON-LD may be useful for performance and page-rendering.


@id 					? dcterms:identifier (what are you using at the moment?)
@type					rdf:type
format					dc:format
viewingDirection		sc:viewingDirection
viewingHint				sc:viewingHint
navDate					sc:presentationDate
label 					rdfs:label
description				dcterms:description
thumbnail				foaf:thumbnail
attribution				sc:attributionLabel
license					dcterms:rights
logo					foaf:logo

within*					dcterms:isPartOf
rendering*				dcterms:hasFormat
related*				dcterms:relation
seeAlso*				rdfs:seeAlso

One omission is metadata. Those are multiple label/value pairs, with an optional language set.

As per the JSON-LD context:

"metadata": {
      "@type": "@id",
      "@id": "sc:metadataLabels",
      "@container": "@list"
    }

It may always be easier to just get these from the JSON-LD.

----- Longer list -----

Technical properties:

@id 					? dcterms:identifier (what are you using at the moment?)
@type					rdf:type
format					dc:format
viewingDirection		sc:viewingDirection
viewingHint				sc:viewingHint
navDate					sc:presentationDate

Descriptive properties:

label 					rdfs:label
description				dcterms:description
thumbnail				foaf:thumbnail

Rights/licensing:

attribution				sc:attributionLabel
license					dcterms:rights
logo					foaf:logo

Linking properties:

related					dcterms:relation
rendering				dcterms:hasFormat
service					svcs:has_service
seeAlso					rdfs:seeAlso
within					dcterms:isPartOf


