# -*- coding: utf-8 -*-
"""Common Jinja2 filters for manipulating ansible vars."""

import itertools
import math
import operator
import os.path


def hostname(fqdn):
    """Return hostname part of FQDN."""
    return fqdn.partition('.')[0]


def domain(fqdn):
    """Return domain part of FQDN."""
    return fqdn.partition('.')[2]


def split_filename(filename):
    """Return extension of filename."""
    return os.path.splitext(filename)[0]


def split_extension(filename):
    """Return filename without extension."""
    return os.path.splitext(filename)[1]


def rstrip_substring(name, substring):
    """Strip given substring from the end of name."""
    if name.endswith(substring):
        return name[:-len(substring)]
    return name


def attrs(dict_list, key):
    """Iterate values of specified key in list of dicts."""
    return itertools.imap(operator.itemgetter(key), dict_list)


def ceil2(number, min_value=0):
    """Round up number to the next highest power of 2."""
    ceiled = 2 ** int(math.ceil(math.log(number, 2))) if number > 0 else 0
    return max(ceiled, min_value)


class FilterModule(object):

    """Common Jinja2 filters for manipulating ansible vars."""

    def filters(self):
        """Return filter functions."""
        return {
            'hostname': hostname,
            'domain': domain,
            'split_filename': split_filename,
            'split_extension': split_extension,
            'rstrip_substring': rstrip_substring,
            'attrs': attrs,
            'ceil2': ceil2,
        }
