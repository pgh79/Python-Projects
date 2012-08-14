# Blake Dutton
l = input("Please enter the list: ")
def nl(s):
    if isinstance(s, list):
        s.sort(key=nl); return sum(nl(x) for x in s)
    else: return s
l.sort(key=nl); print l
