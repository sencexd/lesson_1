# N** 2
def strcounter(s):
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)

#strcounter('aabbbbdsdsew')

# N * M

def strcounter_1(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)

#strcounter('aabbbbdsdsew')

# N
def strcounter_2(s):
    sym_counter = {}
    for sym in s:
        sym_counter[sym] = sym_counter.get(sym, 0) + 1

    for sym, count in sym_counter.items():
        print(sym, count)

strcounter_2('adsaweqwewqdsa')
