#!/usr/bin/env python
for n in range(3, 21):
    text = '{:02d}'.format(n)
    print(text[0] + '.' + text[1], end=' ')
