import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [ 'apple', 'banana', 'camel' ]
chosen_word = random.choice(word_list)
print(f'test word : {chosen_word}')

display = []
for _ in range(len(chosen_word)):
    display.append('_')

lives = 6
end_of_game = False
while not end_of_game:
    guess = input('알파벳을 입력하세요 >>> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] == guess
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f'기회가 {lives} 번 남았습니다.')