# What's that?

Openstreetmap is awesome but whenever you look for an address on
[https://openstreetmap.org](https://openstreetmap.org) it goes through
[nominatim](https://wiki.openstreetmap.org/wiki/Nominatim) which knows
a lot of addresses but sadly not all.

In France we have the
[BAN/BANO](https://wiki.openstreetmap.org/wiki/WikiProject_France/WikiProject_Base_Adresses_Nationale_Ouverte_%28BANO%29)
(and its search engine [addok](https://github.com/etalab/addok)) which
is great (there are much more addresses) but it's 'plugged in' (yet)
on the search field on the map.

This is a script which looks for the address you give him and returns
the results with a probability and a link you just have to copy/paste
in your browser.

## Usage

`./addok2map.py avenue jeanne d\'arc 76000`

Rue Jeanne d'Arc 76000 Rouen (Pertinence : 70%)

https://www.openstreetmap.org/?mlat=49.443756&mlon=1.091569#map=16/49.443756/1.091569/

Place Saint-Marc 76000 Rouen (Pertinence : 30%)

https://www.openstreetmap.org/?mlat=49.438277&mlon=1.100996#map=16/49.438277/1.100996/

# What about i18n?

Comments/variables are in English because it may be read by
everybody but as it's useful only for French addresses (at least for
now) the returned message are in French.
