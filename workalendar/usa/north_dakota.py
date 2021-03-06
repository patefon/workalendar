# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class NorthDakota(UnitedStates):
    """North Dakota"""
    include_columbus_day = False
    include_good_friday = True

# NOTE: At the time of writing, the Public Holidays for USA wikipedia page
# doesn't mention Good Friday, although the official Secretary of State page
# does: http://sos.nd.gov/about-office/holiday-office-closings
