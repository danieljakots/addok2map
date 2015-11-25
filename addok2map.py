#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004

# Copyright (C) 2015 Daniel Jakots <vigdis@chown.me>

# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.

#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

# 0. You just DO WHAT THE FUCK YOU WANT TO.
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
import json
import sys

def print_url(latitude, longitude):
    osm = 'https://www.openstreetmap.org/'
    level = 16
    map_url = '#map=' + str(level) + '/' + str(latitude) + '/' + str(longitude) + '/'
    pointer_url = '?mlat=' + str(latitude) +'&mlon=' + str(longitude)
    url = osm + pointer_url + map_url
    print(url)

# we need an address to look for
if len(sys.argv) == 1:
    print("Je n'ai pas d'adresse à chercher :(")
    print("Par exemple ./addok2map.py avenue de la republique")
    sys.exit(1)
else:
    address = str(sys.argv[1:])
    addok_url = 'https://api-adresse.data.gouv.fr/search/?q='
    r = requests.get(addok_url + address)


# if the HTTP answer is not OK, abort
if r.status_code == 200:
    for f in r.json()['features']:
        pertinence = str(int(f['properties']['score'] * 100))
        print(f['properties']['label'] + ' (Pertinence : ' + pertinence + '%)')
        latitude = f['geometry']['coordinates'][1]
        longitude = f['geometry']['coordinates'][0]
        print_url(latitude, longitude)

else:
    raise Exception("Addok indisponible. Ressayez un peu plus tard ;)")
