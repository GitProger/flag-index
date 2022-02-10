#!/usr/bin/env python3
import sys, os, re, glob, pycountry

GREEN = '\033[1;32m' 
RED = '\033[1;31m'
END = '\033[0m'

COLOR = len(sys.argv) > 1 and sys.argv[1] == "c"

def koef(n):
    def sz(n):
        return os.path.getsize(n)
    return sz(n + ".zip") / sz(n)

def get_name_from_file(f):
    country_code = re.findall("/([^./]*)\\.", f)[0]
    res = pycountry.countries.get(alpha_2=country_code)

    if res is None:
        if COLOR:
            return RED + country_code + END
        else:
            return country_code
    if COLOR:
        return GREEN + res.name + END
    else:
        return res.name

print(
    "\n".join(
        map(
            get_name_from_file, 
            sorted(glob.glob('bmp/*.bmp'), key=koef)
        )
    )
)
print()
