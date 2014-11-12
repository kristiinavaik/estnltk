# -*- coding: utf-8 -*-
'''Core module of the estnltk library.
Defines common functionality for all modules.
'''
from __future__ import unicode_literals, print_function

import os
from jsonpath_rw import parse

# setup some paths

PACKAGE_PATH = os.path.dirname(__file__)
JAVARES_PATH = os.path.join(PACKAGE_PATH, 'java-res')

# corpora
CORPORA_PATH = os.path.join(PACKAGE_PATH, 'corpora')
PMNEWS_PATH = os.path.join(CORPORA_PATH, 'pm_news')


def get_filenames(root, prefix=u'', suffix=u''):
    '''Function for listing filenames with given prefix and suffix in the root directory.
    
    Parameters
    ----------
    
    prefix: str
        The prefix of the required files.
    suffix: str
        The suffix of the required files
        
    Returns
    -------
    list of str
        List of filenames matching the prefix and suffix criteria.
    '''
    return [fnm for fnm in os.listdir(root) if fnm.startswith(prefix) and fnm.endswith(suffix)]


class JsonPaths(object):
    '''Class for defining common jsonpath_rw expresssions.
    
    Attributes
    ----------
    words: jsonpath_rw.jsonpath.Descendants
        Expression for extracting words from corpus structures.
    analysis: jsonpath_rw.jsonpath.Descendants
        Expression for exracting analysis results from corpus structures.
    '''
    words = parse('[*]..words')
    analysis = parse('[*]..analysis')
