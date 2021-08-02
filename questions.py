questions = {
    'question_1': {
        'question': 'De onde é a invenção do chuveiro elétrico?',
        'options': {
            'a': 'França',
            'b': 'Inglaterra',
            'c': 'Brasil',
            'd': 'Austrália',
            'e': 'Itália'
        },
        'correct': 'c'
    },
    'question_2': {
        'question': 'Quais o menor e o maior país do mundo?',
        'options': {
            'a': 'Vaticano e Rússia',
            'b': 'Nauru e China',
            'c': 'Mônaco e Canadá',
            'd': 'Malta e Estados Unidos',
            'e': 'São Marino e Índia'
        },
        'correct': 'a'
    },
    'question_3': {
        'question': 'Qual o grupo em que todas as palavras foram escritas corretamente?',
        'options': {
            'a': 'Asterístico, beneficiente, meteorologia, entertido',
            'b': 'Asterisco, beneficente, meteorologia, entretido',
            'c': 'Asterisco, beneficente, metereologia, entretido',
            'd': 'Asterístico, beneficiente, metereologia, entretido',
            'e': 'Asterisco, beneficiente, metereologia, entretido'
        },
        'correct': 'b'
    },
    'question_4': {
        'question': 'Quantas casas decimais tem o número pi?',
        'options': {
            'a': 'Duas',
            'b': 'Centenas',
            'c': 'Infinitas',
            'd': 'Vinte',
            'e': 'Milhares'
        },
        'correct': 'c'
    },
    'question_5': {
        'question': 'O que a palavra legend significa em português?',
        'options': {
            'a': 'Legenda',
            'b': 'Conto',
            'c': 'História',
            'd': 'Lenda',
            'e': 'Legendário'
        },
        'correct': 'd'
    },
}

correct_answers = 0
number = 1

for qk, qv in questions.items():

   print(f'\n{number}) {qv["question"]}')

   for rk, rv in qv['options'].items():
       print(f'\t{rk}) {rv}')

   answer = input('\nResposta: ')

   if answer == qv['correct']:
       print('Resposta certa!!!')
       correct_answers += 1
   else:
       print(f'Resposta Errada! Alternativa correta: {qv["correct"].upper()}')

   number += 1


print(f'\nVocê acertou {correct_answers / len(questions) * 100}% das pergunta(s)!')
