# -*- coding: utf-8 -*-
"""Pygments styles."""
from pygments.style import Style
from pygments.token import (Comment, Error, Generic, Keyword, Name, Number,
                            Operator, String, Whitespace)


class CgitStyle(Style):

    """Style for Cgit. Based on Github styles."""

    default_style = ''

    background_color = '#ffffff'

    styles = {
        Whitespace: '#bbbbbb',

        Comment: 'italic #999988',
        Comment.Preproc: 'bold noitalic #999999',
        Comment.Special: 'bold italic #999999',

        Keyword: 'bold',
        Keyword.Type: 'bold #445588',

        Operator: 'bold',

        Name: '#333333',
        Name.Attribute: '#008080',
        Name.Builtin: '#0086b3',
        Name.Builtin.Pseudo: '#999999',
        Name.Class: 'bold #445588',
        Name.Constant: '#008080',
        Name.Entity: '#800080',
        Name.Exception: 'bold #990000',
        Name.Function: 'bold #990000',
        Name.Namespace: '#555555',
        Name.Tag: '#000080',
        Name.Variable: '#008080',

        String: '#dd1144',
        String.Regex: '#009926',
        String.Symbol: '#990073',

        Number: '#009999',

        Generic.Deleted: 'bg:#ffdddd #000000',
        Generic.Emph: 'italic',
        Generic.Error: '#aa0000',
        Generic.Heading: '#999999',
        Generic.Inserted: 'bg:#ddffdd #000000',
        Generic.Output: '#888888',
        Generic.Prompt: '#555555',
        Generic.Strong: 'bold',
        Generic.Subheading: 'bold #800080',
        Generic.Traceback: '#aa0000',

        Error: 'bg:#e3d2d2 #a61717',
    }
