import sys

def _shownames(_CLUTTER=dir()):
    """Modified dir()"""
    titles = ['name value id'.split(),
              '---- ----- --'.split()]
    rows = [(key, repr(value), id(value))
            for key, value in globals().items()
            if key not in _CLUTTER and not key.startswith('_')]
    for name, value, id_ in titles + rows:
        print(f'{name:4.4}   {value:5.5}   {id_}')

a = 300
_shownames()