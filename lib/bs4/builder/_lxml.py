__all__ = [
    'LXMLTreeBuilderForXML',
    'LXMLTreeBuilder',
    ]

import collections
from lxml import etree
from lib.bs4.element import Comment, Doctype, NamespacedAttribute
from lib.bs4.builder import (
    FAST,
    HTML,
    HTMLTreeBuilder,
    PERMISSIVE,
    TreeBuilder,
    XML)
from lib.bs4.dammit import UnicodeDammit

LXML = 'lxml'

class LXMLTreeBuilderForXML(TreeBuilder):
    DEFAULT_PARSER_CLASS = etree.XMLParser

    is_xml = True

    # Well, it's permissive by XML parser standards.
    features = [LXML, XML, FAST, PERMISSIVE]

    @property
    def default_parser(self):
        # This can either return a parser object or a class, which
        # will be instantiated with default arguments.
        return etree.XMLParser(target=self, strip_cdata=False, recover=True)

    def __init__(self, parser=None, empty_element_tags=None):
        if empty_element_tags is not None:
            self.empty_element_tags = set(empty_element_tags)
        if parser is None:
            # Use the default parser.
            parser = self.default_parser
        if isinstance(parser, collections.Callable):
            # Instantiate the parser with default arguments
            parser = parser(target=self, strip_cdata=False)
        self.parser = parser
        self.soup = None
        self.nsmaps = None

    def _getNsTag(self, tag):
        # Split the namespace URL out of a fully-qualified lxml tag
        # name. Copied from lxml's src/lxml/sax.py.
        if tag[0] == '{':
            return tuple(tag[1:].split('}', 1))
        else:
            return (None, tag)

    def prepare_markup(self, markup, user_specified_encoding=None,
                       document_declared_encoding=None):
        """
        :return: A 3-tuple (markup, original encoding, encoding
        declared within markup).
        """
        if isinstance(markup, unicode):
            return markup, None, None, False

        try_encodings = [user_specified_encoding, document_declared_encoding]
        dammit = UnicodeDammit(markup, try_encodings, is_html=True)
        return (dammit.markup, dammit.original_encoding,
                dammit.declared_html_encoding,
                dammit.contains_replacement_characters)

    def feed(self, markup):
        self.parser.feed(markup)
        self.parser.close()

    def close(self):
        self.nsmaps = None

    def start(self, name, attrs, nsmap={}):
        nsprefix = None
        # Invert each namespace map as it comes in.
        if len(nsmap) == 0 and self.nsmaps != None:
            # There are no new namespaces for this tag, but namespaces
            # are in play, so we need a separate tag stack to know
            # when they end.
            self.nsmaps.append(None)
        elif len(nsmap) > 0:
            # A new namespace mapping has come into play.
            if self.nsmaps is None:
                self.nsmaps = []
            inverted_nsmap = dict((value, key) for key, value in nsmap.items())
            self.nsmaps.append(inverted_nsmap)
            # Also treat the namespace mapping as a set of attributes on the
            # tag, so we can recreate it later.
            attrs = attrs.copy()
            for prefix, namespace in nsmap.items():
                attribute = NamespacedAttribute(
                    "xmlns", prefix, "http://www.w3.org/2000/xmlns/")
                attrs[attribute] = namespace
        namespace, name = self._getNsTag(name)
        if namespace is not None:
            for inverted_nsmap in reversed(self.nsmaps):
                if inverted_nsmap is not None and namespace in inverted_nsmap:
                    nsprefix = inverted_nsmap[namespace]
                    break
        self.soup.handle_starttag(name, namespace, nsprefix, attrs)

    def end(self, name):
        self.soup.endData()
        completed_tag = self.soup.tagStack[-1]
        namespace, name = self._getNsTag(name)
        nsprefix = None
        if namespace is not None:
            for inverted_nsmap in reversed(self.nsmaps):
                if inverted_nsmap is not None and namespace in inverted_nsmap:
                    nsprefix = inverted_nsmap[namespace]
                    break
        self.soup.handle_endtag(name, nsprefix)
        if self.nsmaps != None:
            # This tag, or one of its parents, introduced a namespace
            # mapping, so pop it off the stack.
            self.nsmaps.pop()
            if len(self.nsmaps) == 0:
                # Namespaces are no longer in play, so don't bother keeping
                # track of the namespace stack.
                self.nsmaps = None

    def pi(self, target, data):
        pass

    def data(self, content):
        self.soup.handle_data(content)

    def doctype(self, name, pubid, system):
        self.soup.endData()
        doctype = Doctype.for_name_and_ids(name, pubid, system)
        self.soup.object_was_parsed(doctype)

    def comment(self, content):
        "Handle comments as Comment objects."
        self.soup.endData()
        self.soup.handle_data(content)
        self.soup.endData(Comment)

    def test_fragment_to_document(self, fragment):
        """See `TreeBuilder`."""
        return u'<?xml version="1.0" encoding="utf-8"?>\n%s' % fragment


class LXMLTreeBuilder(HTMLTreeBuilder, LXMLTreeBuilderForXML):

    features = [LXML, HTML, FAST, PERMISSIVE]
    is_xml = False

    @property
    def default_parser(self):
        return etree.HTMLParser

    def test_fragment_to_document(self, fragment):
        """See `TreeBuilder`."""
        return u'<html><body>%s</body></html>' % fragment
