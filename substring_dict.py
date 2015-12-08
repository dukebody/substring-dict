class SubstringDict(dict):
    """
    Dict that returns a list with all values for whose key is a superstring
    of the given key.
    """
    def __getitem__(self, key):
        return [value for dkey, value in self.items() if key in dkey]


def test_substringdict():
    d = SubstringDict()
    d[u'foobar'] = 1
    d[u'barfoo'] = 2
    d[u'forget'] = 3
    d[u'arfbag'] = 4
    assert 4 in d[u'a']
    assert 2 in d[u'a']
    assert 1 in d[u'a']

    assert 2 in d[u'arf']
    assert 4 in d[u'arf']

    assert 2 in d[u'oo']
    assert 1 in d[u'oo']

    assert d[u'food'] == []
