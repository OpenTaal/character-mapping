#!/usr/bin/env python3


import unicodedata

#TODO reduce als punt
#TODO dotted naar reduced
#TODO src reduced square
#TODO raksepS aanpassen
#TODO spaties toch terug en reduced loskoppelen?!
#TODO delete toevoegen

src_nodes = []
dst_nodes = []
edges = []
fligas = []
regexes = []
grouped_dsts = []
sed_file = open('character-mapping.sed', 'w')
gv_file = open('character-mapping.gv', 'w')
gv_file.write('''digraph G {
layout="twopi"
ranksep=2
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
            if char_dst in ('DELETE', ):
                continue
            if char_dst == 'REDUCE':
                char_src = 'REDUCE{}'.format(char_src)
            if char_src not in src_nodes:
                src_nodes.append(char_src)
            if char_dst not in dst_nodes:
                dst_nodes.append(char_dst)
            edge = '"{}" -> "{}"'.format(char_src.replace('\\', '\\\\'), char_dst.replace('\\', '\\\\'))
            if edge in edges:
                print('ERROR {}'.format(edge))
                print(edges)
                exit(1)
            else:
                edges.append(edge)
            if len(char_dst) > 1 and (char_dst[0] == 'f' or char_dst == 'st'):
                fligas.append('"{}" -> "typographic-ligature"'.format(char_dst))
                grouped_dsts.append(char_dst)

#            if char_dst == 'REDUCE':
#                regex = 's/{}+/{}/g'.format(char_src.replace('\\', '\\\\').replace('*', '\\*').replace('/', '\\/'), char_src.replace('\\', '\\\\').replace('*', '\\*').replace('/', '\\/'))
#            elif char_dst == 'DELETE':
#                regex = 's/{}+//g'.format(char_src.replace('\\', '\\\\').replace('*', '\\*').replace('/', '\\/'))
#            else:
            regex = 's/{}/{}/g'.format(char_src.replace('\\', '\\\\').replace('*', '\\*').replace('/', '\\/'), char_dst.replace('\\', '\\\\').replace('*', '\\*').replace('/', '\\/'))
            if regex in regexes:
                print('ERROR')
                exit(1)
            else:
                regexes.append(regex)


for node in dst_nodes:
    if len(node) == 1:
        gv_file.write('"{}" [label=<<b>{}</b><br/><font point-size="8">{}</font>> ]\n'.format(node.replace('\\', '\\\\'), node.replace(']', '&#93;'), unicodedata.name(node).replace('LETTER ', 'LETTER_').replace(' ', '<br/>').replace('LETTER_', 'LETTER ').lower()))
    else:
        gv_file.write('"{}" [label=<<b>{}</b>> ]\n'.format(node, node))
gv_file.write('''node [style="rounded" ]
''')
for node in src_nodes:
    if node in ('>', '<'):#FIXME
        gv_file.write('"{}" [label="{}" ]\n'.format(node, node))
    elif node in ('﻿', '`', '´', '$', '&', '/', '.', '\\'):#FIXME
        pass
    elif 'REDUCE' in node:
        gv_file.write('"{}" [label=<<b>{}</b><br/><font point-size="8">{}</font>> ]\n'.format(node.replace('\\', '\\\\'), node.replace('REDUCE', '').replace(']', '&#93;').replace('&', '&amp;'), unicodedata.name(node.replace('REDUCE', '')).replace('LETTER ', 'LETTER_').replace(' ', '<br/>').replace('LETTER_', 'LETTER ').lower()))
    elif len(node) == 1:
        try:
            gv_file.write('"{}" [label=<<b>{}</b><br/><font point-size="8">{}</font>> ]\n'.format(node.replace('\\', '\\\\'), node.replace(']', '&#93;'), unicodedata.name(node).replace('LETTER ', 'LETTER_').replace(' ', '<br/>').replace('LETTER_', 'LETTER ').lower()))
        except ValueError:
            print('ValueError for {}'.format(node))
            gv_file.write('"{}" [label=<<b>{}</b>> ]\n'.format(node, node))
    else:
        gv_file.write('"{}" [label=<<b>{}</b>> ]\n'.format(node, node))
for edge in edges:
    gv_file.write('{}\n'.format(edge))

gv_file.write('''
edge [style="dotted" arrowhead="none" ]
node [shape="point" penwidth=0 label="" height=0 width=0 ]
''')

for edge in fligas:
    gv_file.write('{}\n'.format(edge))
for char_dst in dst_nodes:
    if char_dst.islower() and char_dst.upper() in dst_nodes:
        grouped_dsts.append(char_dst)
        grouped_dsts.append(char_dst.upper())
        gv_file.write('"{}" -> "{}"\n'.format(char_dst.upper(), char_dst))
#        gv_file.write('"{}" -> "{}{}"\n'.format(char_dst, char_dst, char_dst.upper()))
#        gv_file.write('"{}" -> "{}{}"\n'.format(char_dst.upper(), char_dst, char_dst.upper()))

#for char_dst in dst_nodes:
#    if len(char_dst) == 2 and char_dst not in grouped_dsts:
#        gv_file.write('"{}" -> "other-ligature"\n'.format(char_dst))

gv_file.write('''}
''')

for regex in regexes:
    sed_file.write('{}\n'.format(regex))
