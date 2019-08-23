def holdem_eval(board, hands):
    scores = [(poker_score((board + ' ' + hand).split()), i) for i, hand in enumerate(hands)]
    best = max(scores)[0]
    return [x[1] for x in filter(lambda x: x[0] == best, scores)]

def poker_score(hand):
    ranks = '  23456789TJQKA'
    if len(hand) > 5: return max([poker_score(hand[:i] + hand[i+1:]) for i in range(len(hand))])
    rcounts = {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
    score, ranks = zip(*sorted(((cnt, rank) for rank, cnt in rcounts), reverse=True))
    if len(score) == 5:
        if ranks[0:2] == (14, 5):
            ranks = (5, 4, 3, 2, 1)
        straight = ranks[0] - ranks[4] == 4
        flush = len({suit for _, suit in hand}) == 1
        score = ([(1,), (3, 1, 2)], [(3, 1, 3), (5,)])[flush][straight]
    return score, ranks

def test():
    print(holdem_eval('9h Tc Jc Qs Kc', [
        'Js Jd', # 0
        'Ad 9c', # 1 A-straight
        'Jd 2c', # 2
        'Ac 8d', # 3 A-straight
        'Qh Kh', # 4
        'Ts 9c', # 5
        'Ah 3h', # 6 A-straight
        '3d 2c', # 7
    ]))
    # holdem_eval() should show [1,3,6]. Winners
    # can be more than 1 in tie situations

if __name__ == '__main__':
    test()