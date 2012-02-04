#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

""" Convert Wordpress data.xml into user-friendly html page.
    Depends on: Mako Template Engine
    Usage: python parser.py data.xml data.html
"""

import sys
from xml.dom import minidom, Node
from mako.template import Template

def get_node_value(node, index=0):
    """ get value of DOM node """

    if node is None:
        return ''
    if not node.childNodes:
        return u'无'
    child = node.childNodes[index]

    if child.nodeType == Node.TEXT_NODE: 
        return child.data.replace('\n', '<br/>')
    return child.nodeValue.replace('\n', '<br/>')


def get_node(node, name):
    """ get DOM node """

    return node.getElementsByTagName(name) if node else []


class WordpressParser(object):
    """
    Core wordpress data parser.
    in_file should be xml data exported from wordpress admin page.
    template is self-defined output html template based on Mako template engine.
    """

    def __init__(self, in_file, out_file, template='template.html'):
        """ init """

        self.doc = minidom.parse(in_file)
        self.out = out_file
        self.template = template

    def query_items(self):
        """ query all blog items """

        root = self.doc.documentElement
        return root.getElementsByTagName('item')

    def render(self):
        """ return html string rendered by Mako engine """

        tpl = Template(filename=self.template, output_encoding='utf-8')
        blogs = self.query_items()
        items = []
        for blog in blogs:
            item = {}
            pid = get_node(blog, 'wp:post_id')[0]
            title = get_node(blog, 'title')[0]
            pub_time = get_node(blog, 'pubDate')[0]
            post_time = get_node(blog, 'wp:post_date')[0]
            content = get_node(blog, 'content:encoded')[0]

            item['id'] = get_node_value(pid)
            item['title'] = get_node_value(title)
            item['time'] = get_node_value(pub_time)
            item['post_time'] = get_node_value(post_time)
            item['content'] = get_node_value(content)
            items.append(item)
        return tpl.render(items=items)

    def run(self):
        """ Write into file """

        outf = file(self.out, 'w')
        outf.write(self.render())
        outf.close()


if __name__ == '__main__':

    if len(sys.argv) < 3: 
        print 'Usage: %s xmlfile targetfile' % sys.argv[0]
        sys.exit(0)
    P = WordpressParser(sys.argv[1], sys.argv[2])
    P.run()
        
