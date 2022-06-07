# -*- coding: utf-8 -*-
"""Tubes TBA'2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nMAW1REPrKVvBGELG90k27P_szNHYENE
"""

import string

# input 
# kalimat = input('input token : ')

def analyze(sentence):
    input_kata = sentence.lower()+'#'

    #initialization
    listhuruf = list(string.ascii_lowercase)
    statelist = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
                'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
                'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
                'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40',
                'q41', 'q42', 'q43', 'q44', 'q45', 'q46']
    tabelTransisi = {}

    for state in statelist:
        for huruf in listhuruf:
            tabelTransisi[(state, huruf)] = 'error'
        tabelTransisi[(state, ' ')] = 'error'
        tabelTransisi[(state, '#')] = 'error'

    # before input string
    tabelTransisi['q0', ' '] = 'q0'

    # update transition table "bini"
    tabelTransisi[('q0', 'b')] = 'q1'
    tabelTransisi[('q1', 'i')] = 'q2'
    tabelTransisi[('q2', 'n')] = 'q3'
    tabelTransisi[('q3', 'i')] = 'q45'
    tabelTransisi[('q45', '#')] = 'accept'
    tabelTransisi[('q45', ' ')] = 'q46'
    tabelTransisi[('q46', '#')] = 'accept'

    # update transition table "benahin"
    tabelTransisi[('q0', 'b')] = 'q1'
    tabelTransisi[('q1', 'e')] = 'q4'
    tabelTransisi[('q4', 'n')] = 'q5'
    tabelTransisi[('q5', 'a')] = 'q6'
    tabelTransisi[('q6', 'h')] = 'q7'
    tabelTransisi[('q7', 'i')] = 'q8'
    tabelTransisi[('q8', 'n')] = 'q9'
    tabelTransisi[('q45', '#')] = 'accept'
    tabelTransisi[('q45', ' ')] = 'q46'
    tabelTransisi[('q46', '#')] = 'accept'

    # update transition table "bures"
    tabelTransisi[('q0', 'b')] = 'q1'
    tabelTransisi[('q1', 'u')] = 'q10'
    tabelTransisi[('q10', 'r')] = 'q11'
    tabelTransisi[('q11', 'e')] = 'q12'
    tabelTransisi[('q12', 's')] = 'q45'
    tabelTransisi[('q45', '#')] = 'accept'
    tabelTransisi[('q45', ' ')] = 'q46'
    tabelTransisi[('q46', '#')] = 'accept'

    # update transition table "demen"
    tabelTransisi[('q0', 'd')] = 'q13'
    tabelTransisi[('q13', 'e')] = 'q14'
    tabelTransisi[('q14', 'm')] = 'q15'
    tabelTransisi[('q15', 'e')] = 'q16'
    tabelTransisi[('q16', 'n')] = 'q45'
    tabelTransisi[('q45', '#')] = 'accept'
    tabelTransisi[('q45', ' ')] = 'q46'
    tabelTransisi[('q46', '#')] = 'accept'

    # update transition table "tisi"
    tabelTransisi[('q0', 't')] = 'q17'
    tabelTransisi[('q17', 'i')] = 'q18'
    tabelTransisi[('q18', 's')] = 'q19'
    tabelTransisi[('q19', 'i')] = 'q45'
    tabelTransisi[('q45', '#')] = 'accept'
    tabelTransisi[('q45', ' ')] = 'q46'
    tabelTransisi[('q46', '#')] = 'accept'

    # update transition table "nganjang"
    tabelTransisi[('q0', 'n')] = 'q20'
    tabelTransisi[('q20', 'g')] = 'q21'
    tabelTransisi[('q21', 'a')] = 'q22'
    tabelTransisi[('q22', 'n')] = 'q23'
    tabelTransisi[('q23', 'j')] = 'q24'
    tabelTransisi[('q24', 'a')] = 'q25'
    tabelTransisi[('q25', 'n')] = 'q26'
    tabelTransisi[('q26', 'g')] = 'q45'
    tabelTransisi[('q45', '#')] = 'accept'
    tabelTransisi[('q45', ' ')] = 'q46'
    tabelTransisi[('q46', '#')] = 'accept'

    # update transition table "nyai"
    tabelTransisi[('q0', 'n')] = 'q20'
    tabelTransisi[('q20', 'y')] = 'q27'
    tabelTransisi[('q27', 'a')] = 'q28'
    tabelTransisi[('q28', 'i')] = 'q45'
    tabelTransisi[('q45', '#')] = 'accept'
    tabelTransisi[('q45', ' ')] = 'q46'
    tabelTransisi[('q46', '#')] = 'accept'

    # update transition table "embok"
    tabelTransisi[('q0', 'e')] = 'q29'
    tabelTransisi[('q29', 'm')] = 'q30'
    tabelTransisi[('q30', 'b')] = 'q31'
    tabelTransisi[('q31', 'o')] = 'q32'
    tabelTransisi[('q32', 'k')] = 'q45'
    tabelTransisi[('q45', '#')] = 'accept'
    tabelTransisi[('q45', ' ')] = 'q46'
    tabelTransisi[('q46', '#')] = 'accept'

    # update transition table "pangkeng"
    tabelTransisi[('q0', 'p')] = 'q33'
    tabelTransisi[('q33', 'a')] = 'q34'
    tabelTransisi[('q34', 'n')] = 'q35'
    tabelTransisi[('q35', 'g')] = 'q36'
    tabelTransisi[('q36', 'k')] = 'q37'
    tabelTransisi[('q37', 'e')] = 'q38'
    tabelTransisi[('q38', 'n')] = 'q39'
    tabelTransisi[('q39', 'g')] = 'q45'
    tabelTransisi[('q45', '#')] = 'accept'
    tabelTransisi[('q45', ' ')] = 'q46'
    tabelTransisi[('q46', '#')] = 'accept'

    # update transition table "gaplok"
    tabelTransisi[('q0', 'g')] = 'q40'
    tabelTransisi[('q40', 'a')] = 'q41'
    tabelTransisi[('q41', 'p')] = 'q42'
    tabelTransisi[('q42', 'l')] = 'q43'
    tabelTransisi[('q43', 'o')] = 'q44'
    tabelTransisi[('q44', 'k')] = 'q45'
    tabelTransisi[('q45', '#')] = 'accept'
    tabelTransisi[('q45', ' ')] = 'q46'
    tabelTransisi[('q46', '#')] = 'accept'

    # transition token baru
    tabelTransisi[('q46', 'b')] = 'q1'
    tabelTransisi[('q46', 'd')] = 'q13'
    tabelTransisi[('q46', 't')] = 'q17'
    tabelTransisi[('q46', 'n')] = 'q20'
    tabelTransisi[('q46', 'e')] = 'q29'
    tabelTransisi[('q46', 'p')] = 'q33'
    tabelTransisi[('q46', 'g')] = 'q40'

    # lexical analysis
    x = 0
    state = 'q0'
    token_saat_ini = ''
    while state != 'accept':
        huruf_saat_ini = input_kata[x]
        token_saat_ini += huruf_saat_ini
        state = tabelTransisi[(state, huruf_saat_ini)]
        if state == 'q45':
            token_saat_ini = ''
        if state == 'error':
            return False
            break;
        x = x + 1

    # conclusion
    if state == 'accept':
        return True