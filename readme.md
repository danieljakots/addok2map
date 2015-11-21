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
the results with a probability.

## Usage

`./addok2map.py avenue de la republique`

# What about i18n?

Comments/variables are in English because it may be read by
everybode but as it's useful only for French addresses (at least for
now) the returned message are in French.
