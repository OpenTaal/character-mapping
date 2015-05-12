#!/usr/bin/env python3


import unicodedata

if __name__ == '__main__':
    src_nodes = []
    dst_nodes = []
    edges = []
    gv_file = open('character-mapping.gv', 'w')
    gv_file.write('''digraph G {
layout="twopi"
ranksep=1.5
fontsize=32
label="Character mapping"
labelloc="c"
node [shape="box" fontsize=24 ]
''')
    with open('character-mapping.tsv', 'r') as input_file:
        for line in input_file:
            if line != '\n' and line[0] != '#':
                chars = line[:-1].split('	')
                char_src = chars[0]
                char_dst = chars[1]
                if char_src not in src_nodes:
                    src_nodes.append(char_src)
                if char_dst not in dst_nodes:
                    dst_nodes.append(char_dst)
                edge = '"{}" -> "{}"'.format(char_src, char_dst)
                if edge in edges:
                    print('ERROR {}'.format(edge))
                    print(edges)
                    exit(1)
                else:
                    if char_src not in '/' and char_dst not in ('/'):#FIXME
                        edges.append(edge)

    for node in dst_nodes:
        if len(node) == 1:
            gv_file.write('"{}" [label=<<b>{}</b><br/><font point-size="8">{}</font>> ]\n'.format(node, node, unicodedata.name(node).replace('LETTER ', 'LETTER_').replace(' ', '<br/>').replace('LETTER_', 'LETTER ').lower()))
        else:
            gv_file.write('"{}" [label=<<b>{}</b>> ]\n'.format(node, node))
    gv_file.write('''node [style="rounded" ]
''')
    for node in src_nodes:
        if node in ('>', '<'):#FIXME
            gv_file.write('"{}" [label="{}" ]\n'.format(node, node))
        elif node in ('﻿', '`', '´', '$', '&', '/', '.', '\\'):#FIXME
            pass
        elif len(node) == 1:
            try:
                gv_file.write('"{}" [label=<<b>{}</b><br/><font point-size="8">{}</font>> ]\n'.format(node, node, unicodedata.name(node).replace('LETTER ', 'LETTER_').replace(' ', '<br/>').replace('LETTER_', 'LETTER ').lower()))
            except ValueError:
                print('ValueError for {}'.format(node))
                gv_file.write('"{}" [label=<<b>{}</b>> ]\n'.format(node, node))
        else:
            gv_file.write('"{}" [label=<<b>{}</b>> ]\n'.format(node, node))
    for edge in edges:
        gv_file.write('{}\n'.format(edge))

    gv_file.write('''}
''')
