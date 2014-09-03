Estnltk
=======

Estnltk provides common natural language processing functionality such as paragraph, sentence and word tokenization,
morphological analysis, named entity recognition etc for Estonian language.

# License

Pyvabamorf is licensed under LGPL. See LICENSE for details.

# Installation

To build and install the library on Linux, invoke the following commands:
```
python setup.py build
sudo python setup.py install
```

# Example

```python
>>> from estnltk.corpus import PlainTextDocumentImporter
>>> from pprint import pprint

>>> importer = PlainTextDocumentImporter()
>>> document = importer(u'See on esimene lõik. See on esimese lõigu sisu\nTeine lõik.')

>>> # importer performs basic tokenization of the document
>>> pprint(document)
{'end': 58,
 'paragraphs': [{'end': 46,
                 'rel_end': 46,
                 'rel_start': 0,
                 'sentences': [{'end': 20,
                                'rel_end': 20,
                                'rel_start': 0,
                                'start': 0,
                                'text': u'See on esimene l\xf5ik.',
                                'words': [{'end': 3,
                                           'rel_end': 3,
                                           'rel_start': 0,
                                           'start': 0,
                                           'text': u'See'},
                                          {'end': 6,
                                           'rel_end': 6,
                                           'rel_start': 4,
                                           'start': 4,
                                           'text': u'on'},
                                          {'end': 14,
                                           'rel_end': 14,
                                           'rel_start': 7,
                                           'start': 7,
                                           'text': u'esimene'},
                                          {'end': 20,
                                           'rel_end': 20,
                                           'rel_start': 15,
                                           'start': 15,
                                           'text': u'l\xf5ik.'}]},
                               {'end': 46,
                                'rel_end': 46,
                                'rel_start': 21,
                                'start': 21,
                                'text': u'See on esimese l\xf5igu sisu',
                                'words': [{'end': 24,
                                           'rel_end': 3,
                                           'rel_start': 0,
                                           'start': 21,
                                           'text': u'See'},
                                          {'end': 27,
                                           'rel_end': 6,
                                           'rel_start': 4,
                                           'start': 25,
                                           'text': u'on'},
                                          {'end': 35,
                                           'rel_end': 14,
                                           'rel_start': 7,
                                           'start': 28,
                                           'text': u'esimese'},
                                          {'end': 41,
                                           'rel_end': 20,
                                           'rel_start': 15,
                                           'start': 36,
                                           'text': u'l\xf5igu'},
                                          {'end': 46,
                                           'rel_end': 25,
                                           'rel_start': 21,
                                           'start': 42,
                                           'text': u'sisu'}]}],
                 'start': 0,
                 'text': u'See on esimene l\xf5ik. See on esimese l\xf5igu sisu'},
                {'end': 58,
                 'rel_end': 58,
                 'rel_start': 47,
                 'sentences': [{'end': 58,
                                'rel_end': 11,
                                'rel_start': 0,
                                'start': 47,
                                'text': u'Teine l\xf5ik.',
                                'words': [{'end': 52,
                                           'rel_end': 5,
                                           'rel_start': 0,
                                           'start': 47,
                                           'text': u'Teine'},
                                          {'end': 58,
                                           'rel_end': 11,
                                           'rel_start': 6,
                                           'start': 53,
                                           'text': u'l\xf5ik.'}]}],
                 'start': 47,
                 'text': u'Teine l\xf5ik.'}],
 'rel_end': 58,
 'rel_start': 0,
 'start': 0,
 'text': u'See on esimene l\xf5ik. See on esimese l\xf5igu sisu\nTeine l\xf5ik.'}

>>> # we can use pyvabamorf analyzer to add morphological annotations
>>> from estnltk.morf import PyVabamorfAnalyzer
>>> analyzer=PyVabamorfAnalyzer()

>>> pprint(analyzer(document))
{'end': 58,
 'paragraphs': [{'end': 46,
                 'rel_end': 46,
                 'rel_start': 0,
                 'sentences': [{'end': 20,
                                'rel_end': 20,
                                'rel_start': 0,
                                'start': 0,
                                'text': u'See on esimene l\xf5ik.',
                                'words': [{'analysis': [{'clitic': u'',
                                                         'ending': u'0',
                                                         'form': u'sg n',
                                                         'lemma': u'see',
                                                         'lemma_tokens': [u'see'],
                                                         'partofspeech': u'P',
                                                         'root': u's<ee'}],
                                           'end': 3,
                                           'rel_end': 3,
                                           'rel_start': 0,
                                           'start': 0,
                                           'text': u'See'},
                                          {'analysis': [{'clitic': u'',
                                                         'ending': u'0',
                                                         'form': u'b',
                                                         'lemma': u'ole',
                                                         'lemma_tokens': [u'ole'],
                                                         'partofspeech': u'V',
                                                         'root': u'ole'},
                                                        {'clitic': u'',
                                                         'ending': u'0',
                                                         'form': u'vad',
                                                         'lemma': u'ole',
                                                         'lemma_tokens': [u'ole'],
                                                         'partofspeech': u'V',
                                                         'root': u'ole'}],
                                           'end': 6,
                                           'rel_end': 6,
                                           'rel_start': 4,
                                           'start': 4,
                                           'text': u'on'},
...

>>> # morphological analyzer accepts single documents and lists of documents
>>> document2 = importer(u'Teine dokument.')
>>> pprint(analyzer([document, document2]))
[{'end': 58,
  'paragraphs': [{'end': 46,
                  'rel_end': 46,
                  'rel_start': 0,
                  'sentences': [{'end': 20,
                                 'rel_end': 20,
                                 'rel_start': 0,
                                 'start': 0,
                                 'text': u'See on esimene l\xf5ik.',
                                 'words': [{'analysis': [{'clitic': u'',
                                                          'ending': u'0',
                                                          'form': u'sg n',
                                                          'lemma': u'see',
                                                          'lemma_tokens': [u'see'],
                                                          'partofspeech': u'P',
                                                          'root': u's<ee'}],
                                            'end': 3,
                                            'rel_end': 3,
                                            'rel_start': 0,
                                            'start': 0,
                                            'text': u'See'},
...
 {'end': 15,
  'paragraphs': [{'end': 15,
                  'rel_end': 15,
                  'rel_start': 0,
                  'sentences': [{'end': 15,
                                 'rel_end': 15,
                                 'rel_start': 0,
                                 'start': 0,
                                 'text': u'Teine dokument.',
                                 'words': [{'analysis': [{'clitic': u'',
                                                          'ending': u'0',
                                                          'form': u'sg n',
                                                          'lemma': u'teine',
                                                          'lemma_tokens': [u'teine'],
                                                          'partofspeech': u'O',
                                                          'root': u'teine'},
                                                         {'clitic': u'',
                                                          'ending': u'0',
                                                          'form': u'sg n',
                                                          'lemma': u'teine',
                                                          'lemma_tokens': [u'teine'],
                                                          'partofspeech': u'P',
                                                          'root': u'teine'}],
                                            'end': 5,
                                            'rel_end': 5,
                                            'rel_start': 0,
                                            'start': 0,
                                            'text': u'Teine'},
                                           {'analysis': [{'clitic': u'',
                                                          'ending': u'0',
                                                          'form': u'sg n',
                                                          'lemma': u'dokument',
                                                          'lemma_tokens': [u'dokument'],
                                                          'partofspeech': u'S',
                                                          'root': u'd?okum<en]t'}],
                                            'end': 15,
                                            'rel_end': 15,
                                            'rel_start': 6,
                                            'start': 6,
                                            'text': u'dokument.'}]}],
                  'start': 0,
                  'text': u'Teine dokument.'}],
  'rel_end': 15,
  'rel_start': 0,
  'start': 0,
  'text': u'Teine dokument.'}]
```