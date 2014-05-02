# -*- coding: utf-8 -*-
import itertools
import math
import operator
import os.path


def hostname(fqdn):
    """Returns hostname part of FQDN."""
    return fqdn.partition('.')[0]


def domain(fqdn):
    """Returns domain part of FQDN."""
    return fqdn.partition('.')[2]


def split_filename(filename):
    """Returns extension of filename."""
    return os.path.splitext(filename)[0]


def split_extension(filename):
    """Returns filename without extension."""
    return os.path.splitext(filename)[1]


def rstrip_substring(name, substring):
    """Strips given substring from the end of name."""
    if name.endswith(substring):
        return name[:-len(substring)]
    return name
    

def attrs(dict_list, key):
    """Iterates values of specified key in list of dicts."""
    return itertools.imap(operator.itemgetter(key), dict_list)


def ceil2(number, min_value=0):
    """Rounds up number to the next highest power of 2."""
    ceiled = 2 ** int(math.ceil(math.log(number, 2))) if number > 0 else 0
    return max(ceiled, min_value)


class FilterModule(object):
    """Jinja2 filters for manipulating ansible vars."""
    def filters(self):
        return {
            'hostname': hostname,
            'domain': domain,
            'split_filename': split_filename,
            'split_extension': split_extension,
            'rstrip_substring': rstrip_substring,
            'attrs': attrs,
            'ceil2': ceil2,
        }
