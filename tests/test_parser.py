#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from lpp_parser import get_lpp_info

lpp_file = '44S_target8mm.lpp'


def test_get_lpp_info():
    d = get_lpp_info(lpp_file)
    settings = d['settings']
    assert settings['primary_beam'] == {
        'A': '48',
        'name': 'Ca',
        'Q': '20',
        'Z': 20,
        'Ek': '220',
        'power': '0.082',
        'rf_freq': '40.25',
        'tau': '0.261'
    }
    assert settings['frag_beam'] == {'A': '44', 'name': 'S', 'Z': 16}
