
import re

"""Regex Practice"""

a-z are literal (dont need / or \)


MATCHING MULTIPLES

match 0 or 1
- use a ? *after* what you want to match

matches 0+
- use a * *after* what you want to match

match 1+
- use a + *after* what you want to match


GROUPING ()
(wiolhnw)


WOuld it be:
[wiolhn]*d+


###

match_obj = re.findall(r"[wiolhn]*d+[wiolhn]*", )
#returns a list of all matches

