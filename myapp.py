#!/usr/bin/env python

from bottle import run, route, static_file

@route('/myapp/<filename>')
def myapp(filename):
    return static_file(filename, root='./static/')

run(host='localhost', port=8080, debug=True)

