
suite = ['H', 'C', 'S', 'D']
cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
hands = ['HIGH','PAIR','2PAIR','THREE','STRAIGHT','FLUSH','FULLH','FOUR','STRAIGHTF']
while True:
    try:
        deal = input().strip().split()
        white = deal[5:]
        black = deal[:5]
        white_highs = sorted([cards.index(card[0]) for card in white])
        black_highs = sorted([cards.index(card[0]) for card in black])
        white_suits = sorted([suite.index(card[1]) for card in white])
        black_suits = sorted([suite.index(card[1]) for card in black])
        best_white = 0
        best_black = 0
        white_flush = False
        white_straight = False
        black_flush = False
        black_straight = False
        if white_highs[0] == white_highs[1] or white_highs[1] == white_highs[2] or white_highs[2] == white_highs[3] or white_highs[3] == white_highs[4]:
            best_white = 1
        if black_highs[0] == black_highs[1] or black_highs[1] == black_highs[2] or black_highs[2] == black_highs[3] or black_highs[3] == black_highs[4]:
            best_black = 1
        if (white_highs[0] == white_highs[1] and (white_highs[2] == white_highs[3] or white_highs[3] == white_highs[4])) or (white_highs[3] == white_highs[4] and white_highs[2] == white_highs[1]):
            best_white = 2
        if (black_highs[0] == black_highs[1] and (black_highs[2] == black_highs[3] or black_highs[3] == black_highs[4])) or (black_highs[3] == black_highs[4] and black_highs[2] == black_highs[1]):
            best_black = 2
        if (white_highs[0] == white_highs[1] == white_highs[2] or white_highs[1] == white_highs[2] == white_highs[3] or white_highs[2] == white_highs[3] == white_highs[4]):
            best_white = 3
        if (black_highs[0] == black_highs[1] == black_highs[2] or black_highs[1] == black_highs[2] == black_highs[3] or black_highs[2] == black_highs[3] == black_highs[4]):
            best_black = 3
        # straight
        if white_highs[0] + 4 == white_highs[1] + 3 == white_highs[2] + 2 == white_highs[3] + 1 == white_highs[4]:
            best_white = 4
            white_straight = True
        if black_highs[0] + 4 == black_highs[1] + 3 == black_highs[2] + 2 == black_highs[3] + 1 == black_highs[4]:
            best_black = 4
            black_straight = True
        if white_suits.count(0) == 5 or white_suits.count(1) == 5 or white_suits.count(2) == 5 or white_suits.count(3) == 5 or white_suits.count(4) == 5:
            best_white = 5
            white_flush = True
        if black_suits.count(0) == 5 or black_suits.count(1) == 5 or black_suits.count(2) == 5 or black_suits.count(3) == 5 or black_suits.count(4) == 5:
            best_black = 5
            black_flush = True
        if (white_highs[0] == white_highs[1] and white_highs[2] == white_highs[3] == white_highs[4]) or (white_highs[3] == white_highs[4] and white_highs[0] == white_highs[1] == white_highs[2]):
            best_white = 6
        if (black_highs[0] == black_highs[1] and black_highs[2] == black_highs[3] == black_highs[4]) or (black_highs[3] == black_highs[4] and black_highs[0] == black_highs[1] == black_highs[2]):
            best_black = 6
        if (black_highs[0] == black_highs[1] == black_highs[2] == black_highs[3]) or (black_highs[4] == black_highs[1] == black_highs[2] == black_highs[3]):
            best_black = 7
        if (white_highs[0] == white_highs[1] == white_highs[2] == white_highs[3]) or (white_highs[4] == white_highs[1] == white_highs[2] == white_highs[3]):
            best_white = 7
        if (white_flush and white_straight):
            best_white = 8
        if (black_flush and black_straight):
            best_black = 8
        if (best_black == best_white == 3) or (best_black == best_white == 6):
            if (max(max(black_highs.count(black_highs[0]), black_highs[1]), black_highs[2]))
        elif best_black > best_white:
            print("Black wins.")
        elif best_white > best_white:
            print("White wins.")
        elif white_highs[4] > black_highs[4]:
            print("White wins.")
        elif white_highs[4] < black_highs[4]:
            print("Black wins.")
        elif white_highs[3] > black_highs[3]:
            print("White wins.")
        elif white_highs[3] < black_highs[3]:
            print("Black wins.")
        elif white_highs[2] > black_highs[2]:
            print("White wins.")
        elif white_highs[2] < black_highs[2]:
            print("Black wins.")
        elif white_highs[1] > black_highs[1]:
            print("White wins.")
        elif white_highs[1] < black_highs[1]:
            print("Black wins.")
        elif white_highs[0] > black_highs[0]:
            print("White wins.")
        elif white_highs[0] < black_highs[0]:
            print("Black wins.")
        else:
            print("Tie.")
    except EOFError:
        break