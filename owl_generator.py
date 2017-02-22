from lxml.etree import Element, SubElement, QName, tostring, ElementTree

class OwlGenerator:
	def __init__(self, iri):
		self.iri = iri
		self.entities = []
		self.data_attrs = []
		self.obj_attrs = []

	def write_owl(self, filename):
		base = self.iri
		none = base + "#"
		rdf = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
		owl = 'http://www.w3.org/2002/07/owl#'
		xml = 'http://www.w3.org/XML/1998/namespace'
		xsd = 'http://www.w3.org/2001/XMLSchema#'
		rdfs = 'http://www.w3.org/2000/01/rdf-schema#'
		about = self.iri

		root = Element(QName(rdf, 'RDF'), nsmap={ None:none, 'rdf':rdf, 'owl':owl })
		root.attrib[QName(xml, 'base')] = base

		ontology = SubElement(root, QName(owl, 'Ontology'))
		ontology.attrib[QName(rdf, 'about')] = base

		for obj_attr in self.obj_attrs:
			el = SubElement(root, QName(owl, 'ObjectProperty'))
			el.attrib[QName(rdf, 'about')] = none + obj_attr.name

			domain_el = SubElement(el, QName(rdfs, 'domain'))
			domain_el.attrib[QName(rdf, 'resource')] = none + obj_attr.domain.name

			range_el = SubElement(el, QName(rdfs, 'range'))
			range_el.attrib[QName(rdf, 'resource')] = none + obj_attr.range.name

		for data_attr in self.data_attrs:
			el = SubElement(root, QName(owl, 'DatatypeProperty'))
			el.attrib[QName(rdf, 'about')] = none + data_attr.name

			domain_el = SubElement(el, QName(rdfs, 'domain'))
			domain_el.attrib[QName(rdf, 'resource')] = none + data_attr.domain.name

			range_el = SubElement(el, QName(rdfs, 'range'))
			range_el.attrib[QName(rdf, 'resource')] = rdf + data_attr.range

		for entity in self.entities:
			class_el = SubElement(root, QName(owl, 'Class'))
			class_el.attrib[QName(rdf, 'about')] = none + entity.name

		doc = ElementTree(root)
		doc.write(filename, pretty_print=True, encoding='utf-8', xml_declaration=True)
		print("OWL file successfully generated")


class OwlEntity:
	def __init__(self, name):
		self.name = name

class OwlDataAttr:
	def __init__(self, name, domain, range_val):
		self.name = name
		self.domain = domain
		self.range = range_val

class OwlObjAttr:
	def __init__(self, name, domain, range_val):
		self.name = name
		self.domain = domain
		self.range = range_val

