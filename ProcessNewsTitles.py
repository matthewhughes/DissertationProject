# -*- coding: utf-8 -*-


import nltk

class ProcessTitles(object):

    def __init__(self):
        self.title = ''
        self.tokenized_text = ''
        self.tokens = ''
        self.noun = ''
        self.verb = ''

    def tokenize_title(self):
        self.tokenized_text = nltk.word_tokenize(self.title)

    def position_tags(self):
        self.tokens = nltk.pos_tag(self.tokenized_text)

    def find_noun(self):
        nouns_list = []

        for i in self.tokens:
            if (i[1] == 'NN' or i[1] == 'NNS' or i[1] == 'NNP' or i[1] == 'NNPS'):
                print i
                nouns_list.append([i])
        noun = nouns_list[0][0]
        if noun != '':
            self.noun = noun
            print noun
        else:
            print "No noun found. "

    def find_verb(self):
        verbs_list = []
        print self.tokens

        for i in self.tokens:
            if(i[1] == 'VB' or i[1] == 'VBD' or i[1] == 'VBG' or i[1] == 'VBN' or i[1] == 'VBP' or i[1] == 'VBZ'):
                print i
                verbs_list.append([i])
        try:
            verb = verbs_list[0][0]
            if verb != '':
                self.verb = verb
                print verb
        except:
            print "No verb found. "


def main():
    news_titles = ["Parties clash over jobless figures", "Funeral celebrates Becky Watts' life",
    'County footballer jailed for attacks', u'Rolls-Royce receives record £6bn engine order',
    'IMF praises UK economic strategy']
    Titles = ProcessTitles()
    try:
        for i in range(0, len(news_titles)):
            Titles.title = i
            Titles.tokenize_title()
            Titles.position_tags()
            Titles.find_noun()
            Titles.find_verb()
            print Titles.noun
            print Titles.verb
    except IndexError:
        pass



if __name__ == '__main__':
    main()
