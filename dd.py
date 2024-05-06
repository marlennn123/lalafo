import random
count = 1
word1 = int(input('мин. диапазон: '))
word2 = int(input('макс. диапазон: '))
word3 = random.randint(word1, word2)
while True:
    print(f'{word1} жана {word2} ортосундагы сан:')
    total = int(input("сиздин жооп: "))
    if total < word3:
        print("сиздин сан кичине")
    if total > word3:
        print("сиздин сан чонн")
    if total == word3:
        print(f'ТУУУРААА, {count} аракеттен таптыныз!')
        break
    count += 1