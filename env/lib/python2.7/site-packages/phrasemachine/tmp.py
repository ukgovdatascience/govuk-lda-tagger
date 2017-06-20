'''
PICKLE = "averaged_perceptron_tagger.pickle"

tagger = PerceptronTagger(load=False)
tagger.load('averaged_perceptron_tagger.pickle')
print tagger.tag('The quick brown fox jumps over the lazy dog'.split())
'''

import phrasemachine
text = u"Barack Obama supports expanding social security."
print phrasemachine.get_phrases(text)