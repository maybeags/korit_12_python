# 기초 설정 하시오.
# ascii art generator를 통해 hangman logo를 만들고 logo 변수에 대입하시오.
# 첫 시작 시에만 print(logo)가 실행될 수 있게끔 작성하시오.
# 생성형 ai에 word_list를 400 개 짜리 만들어 달라고 해서 붙여넣으시오.
# 그러면 전체 hangman이 완성되겠네요.
import random

logo = '''
.-. .-.  .--.  .-. .-. .---. .-.   .-.  .--.  .-. .-.
| {_} | / {} \ |  `| |/   __}|  `.'  | / {} \ |  `| |
| { } |/  /\  \| |\  |\  {_ }| |\ /| |/  /\  \| |\  |
`-' `-'`-'  `-'`-' `-' `---' `-' ` `-'`-'  `-'`-' `-'
'''
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
word_list = [
    'apple', 'banana', 'camel', 'abandon', 'abnormal', 'absolute', 'abstract', 'academic',
    'accelerate', 'accessible', 'accommodate', 'accompany', 'accumulate', 'accurate',
    'acknowledge', 'acquire', 'adapt', 'adequate', 'adjust', 'administer', 'adopt',
    'advocate', 'aesthetic', 'affect', 'afford', 'aggregate', 'allocate', 'alter',
    'alternative', 'ambiguous', 'analyze', 'anticipate', 'apparent', 'appreciate',
    'approach', 'appropriate', 'approximate', 'arbitrary', 'aspect', 'assemble',
    'assert', 'assess', 'assign', 'assist', 'assume', 'assure', 'attach', 'attain',
    'attitude', 'attribute', 'authority', 'available', 'aware', 'barrier', 'behalf',
    'benefit', 'bias', 'bond', 'brief', 'bulk', 'capable', 'capacity', 'category',
    'cease', 'challenge', 'channel', 'chapter', 'chart', 'circumstance', 'cite',
    'civil', 'clarify', 'classic', 'clause', 'code', 'coherent', 'coincide', 'collapse',
    'colleague', 'combine', 'comment', 'commission', 'commit', 'commodity', 'communicate',
    'community', 'compatible', 'compensate', 'compile', 'complement', 'complex',
    'component', 'compound', 'comprehensive', 'comprise', 'compute', 'conceive',
    'concentrate', 'concept', 'conclude', 'concurrent', 'conduct', 'confer', 'confine',
    'confirm', 'conflict', 'conform', 'consent', 'consequent', 'considerable', 'consist',
    'constant', 'constitute', 'constrain', 'construct', 'consult', 'consume', 'contact',
    'contemporary', 'context', 'contract', 'contradict', 'contrary', 'contrast',
    'contribute', 'controversy', 'convene', 'converse', 'convert', 'convince', 'cooperate',
    'coordinate', 'core', 'corporate', 'correspond', 'couple', 'create', 'credit',
    'criteria', 'crucial', 'culture', 'currency', 'cycle', 'data', 'debate', 'decade',
    'decline', 'deduce', 'define', 'definite', 'demonstrate', 'denote', 'deny', 'depict',
    'derive', 'design', 'despite', 'detect', 'deviate', 'device', 'devote', 'differentiate',
    'dimension', 'diminish', 'discrete', 'discriminate', 'displace', 'display', 'dispose',
    'distinct', 'distort', 'distribute', 'diverse', 'document', 'domain', 'domestic',
    'dominate', 'draft', 'drama', 'duration', 'dynamic', 'economy', 'edit', 'element',
    'eliminate', 'emerge', 'emphasize', 'empirical', 'enable', 'encounter', 'energy',
    'enforce', 'enhance', 'enormous', 'ensure', 'entity', 'environment', 'equate',
    'equip', 'equivalent', 'erode', 'error', 'establish', 'estate', 'estimate', 'ethical',
    'evaluate', 'eventual', 'evident', 'evolve', 'exceed', 'exclude', 'exhibit', 'expand',
    'expert', 'explicit', 'exploit', 'export', 'expose', 'external', 'extract', 'facilitate',
    'factor', 'feature', 'federal', 'fee', 'file', 'final', 'finance', 'finite', 'flexible',
    'fluctuate', 'focus', 'format', 'formula', 'forthcoming', 'found', 'foundation',
    'framework', 'function', 'fundamental', 'fund', 'gender', 'generate', 'generation',
    'globe', 'goal', 'grade', 'grant', 'guarantee', 'guideline', 'hence', 'hierarchy',
    'highlight', 'hypothesis', 'identical', 'identify', 'ideology', 'ignorance', 'illustrate',
    'image', 'immigrate', 'impact', 'implement', 'implicate', 'implicit', 'imply',
    'impose', 'incentive', 'incidence', 'incline', 'income', 'incorporate', 'index',
    'indicate', 'individual', 'induce', 'inevitable', 'infer', 'infrastructure', 'inherent',
    'inhibit', 'initial', 'initiate', 'injure', 'innovate', 'input', 'insert', 'insight',
    'inspect', 'instance', 'institute', 'instruct', 'integral', 'integrate', 'integrity',
    'intelligence', 'intense', 'interact', 'intermediate', 'internal', 'interpret',
    'interval', 'intervene', 'intrinsic', 'invest', 'investigate', 'invoke', 'involve',
    'isolate', 'issue', 'item', 'job', 'journal', 'justify', 'label', 'labor', 'layer',
    'lecture', 'legal', 'legislate', 'levy', 'liberal', 'licence', 'likewise', 'link',
    'locate', 'logic', 'maintain', 'major', 'manipulate', 'manual', 'margin', 'mature',
    'maximize', 'mechanism', 'media', 'mediate', 'medical', 'medium', 'mental', 'method',
    'migrate', 'military', 'minimal', 'minimize', 'minimum', 'ministry', 'minor', 'mode',
    'modify', 'monitor', 'motive', 'mutual', 'negate', 'network', 'neutral', 'nevertheless',
    'norm', 'notion', 'notwithstanding', 'nuclear', 'objective', 'obvious', 'occupy',
    'occur', 'odd', 'offset', 'ongoing', 'option', 'orient', 'outcome', 'output', 'overall',
    'overlap', 'overseas', 'panel', 'paradigm', 'paragraph', 'parallel', 'parameter',
    'participate', 'partner', 'passive', 'perceive', 'percent', 'period', 'persist',
    'perspective', 'phase', 'phenomenon', 'philosophy', 'physical', 'plus', 'policy',
    'portion', 'pose', 'positive', 'potential', 'practitioner'
]
chosen_word = random.choice(word_list)
print(f'테스트 단어 {chosen_word}')
print(logo)

display = []
for _ in range(len(chosen_word)):
    display.append('_')

lives = 6
end_of_game = False
while not end_of_game:
    print(stages[lives])
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
            print(stages[lives])
            print(f'정답은 {chosen_word}입니다.')
    if '_' not in display:
        print(f'정답입니다 !! 🍎')
        end_of_game = True

    print(' '.join(display))