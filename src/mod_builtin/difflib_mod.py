#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import difflib

txt1 = """line1,hello.
line2 are you ok?
"""
txt2 = """line1,hello.
line2 are you 好吗?
over
"""

txt1_lines = txt1.splitlines()
txt2_lines = txt2.splitlines()

d = difflib.Differ()
diff = d.compare(txt1_lines, txt2_lines)
print('\n'.join(diff))

hd = difflib.HtmlDiff()
with open('diff.html', 'w', encoding='utf-8') as f:
    f.write(hd.make_file(txt1_lines, txt2_lines))

print('\n'.join((difflib.unified_diff(txt1_lines, txt2_lines))))

print('\n'.join(difflib.context_diff(txt1_lines, txt2_lines)))
