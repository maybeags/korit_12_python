# ch05_hangman 내부에 -> python package로 hangman_oop 생성 -> hangman6.py / hangman_arts.py / hangman_word_list.py
import random
import hangman_arts
import hangman_word_list
# import 다음에 파일명을 썼다는 것에 주목해야합니다. 이 파일 하나를 파이썬에서는 module(모듈)이라고 합니다.

# 외부의 hangman_word_list에 있는 word_list 변수를 참조해서 chosen_word를 만들 필요가 있습니다.
print(hangman_arts.logo)
# 위에가 힌트. 그러면 chosen_word를 불러올 수 있도록 코드를 작성하시오.
chosen_word = random.choice(hangman_word_list.word_list)
print(f'테스트 단어 : {chosen_word}')
# 나머지 부분을 잘 복사한 다음에 오류 생기는 부분을 수정하시오.

display = []
for _ in range(len(chosen_word)):
    display.append('_')

lives = 6
end_of_game = False
while not end_of_game:
    print(hangman_arts.stages[lives])
    guess = input('알파벳을 입력하세요 >>> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f'기회가 {lives} 번 남았습니다.')
        if lives == 0:
            print(f'모든 기회를 잃었습니다.')
            end_of_game = True
            print(hangman_arts.stages[lives])
            print(f'정답은 {chosen_word}입니다.')
    if '_' not in display:
        print(f'정답입니다 !! 🍎')
        end_of_game = True

    print(' '.join(display))