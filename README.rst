Wordseg
=======

Wicked fast word segmenter with a focus on splitting #hashtags.


Example
-------

.. code:: python

    from wordseg import segment

    segment('mannequinchallenge')
        # => (['mannequin', 'challenge'], 5.996932418552515e-11)


More Info
---------

Because the "training" data was harvested from social media websites, this
word segmenter is especially good as a hashtag splitter. It's also about *10x
faster* than `wordsegment`_.

The speed derives from an implementation of the `Viterbi algorithm`_ I found
posted on SO_. The built-in dictionary was pulled from about 6GB of social media
posts (English only). Tools for building your own dictionary are included in the
:code:`bin` folder.

Roadmap
-------

- Improve data set by including posts from a broader range of time and with more
  unique unigrams.

- Include common bigrams or even trigrams to help segmentation be context-aware.

- Beef-up the very minimal Viterbi implementation


.. _wordsegment: https://pypi.python.org/pypi/wordsegment/0.6.2
.. _SO: http://stackoverflow.com/a/481773/554406
.. _Viterbi algorithm: https://en.wikipedia.org/wiki/Viterbi_algorithm
.. _Recurrent Neural Networks: http://karpathy.github.io/2015/05/21/rnn-effectiveness/
