import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

# sorting for deck
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spade_high_sort(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value + suit_values[card.suit]

class FrenchDeck:
    suits = 'spades diamonds clubs hearts'.split()
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    # sample representation of Card
    # beer_card = Card('7', 'diamonds')
    # print(beer_card)

    # return the length of the card deck
    deck = FrenchDeck()
    # print(len(deck))

    # read specific items from the deck
    first_card = deck[0]
    # print(first_card)

    # get a random card in the deck
    import random
    random_card = random.choice(deck)
    # print(random_card)

    # automatic support of slicing
    mini_deck = deck[:3]
    # print(mini_deck)

    # deck is also iterable and reversible
    # for card in deck:
    #     print(card)
    
    # for card in reversed(deck):
    #     print('Reversed: ', card)

    # return sorted deck using spades_high_sort
    for card in sorted(deck, key=spade_high_sort):
        print(card)