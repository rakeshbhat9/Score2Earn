from wrapper import UserData
from rstousd import rate
from collections import Counter

list_of_players = []
round_winner = []


def create_players():
    number_of_players = int(raw_input("Please input total number of players: "))

    for i in range(number_of_players):
        a = raw_input("Provide Name & PPId using , separator: ")
        obj = UserData(a.split(",")[0], a.split(",")[1])

        if obj:
            list_of_players.append(obj)

    print "Data for below players added"
    print [x.name for x in list_of_players]


def get_scores():
    print ("Lets Input scores for users..")
    for player in list_of_players:
        scores = raw_input("Input score for " + player.name)
        player.score = player.add_score(scores)


def find_leader():
    print "Leading scorer this round is: "
    leader = max((player.score, player.name) for player in list_of_players)
    round_winner.append(leader[1])
    msg = '{} {} {}'.format(leader[1], " with total score of ", leader[0])
    print msg


def game_status():
    q = raw_input("Are we playing another game? Y/N: ")

    if q.upper().strip() not in ['Y', 'N']:
        print "Sorry don't understand that,lets try again.."
        game_status()

    elif q.upper().strip() == 'Y':
        msg = "{0} {1}".format("Let's begin round ", len(round_winner) + 1)
        print msg
        get_scores()
        find_leader()
        game_status()

    elif q.upper().strip() == 'N':
        print "Cool let me see who has earned some money today.."
        print "Final Winner is..."
        print final_winner()
        calc_payment()

    else:
        print "Sorry don't understand that,lets try again.."
        game_status()


def final_winner():
    d = Counter(round_winner)
    winner = list(filter(lambda t: t[1] == max(d.values()), d.items()))[0][0]
    return winner


'''
    Who is the winner?

    (a) Highest Points: we will have to get winner and charge
    others per round
    (b) Number of rounds won: we can use final_winner
    and charge others per round

    Payment:
    (a) Settle each round? Winner of each round gets money.
    (b) Or winner of most rounds takes all the money

    Current implementation is b & b

'''


def calc_payment():
    total_rounds = len(round_winner)
    game_rate = 100  # INR Per Round
    paying_players = len(list_of_players) - 1
    total_winnings = game_rate * total_rounds * paying_players
    per_head = total_winnings / paying_players
    # conversion_rate = rate
    conversion_rate = 50
    dollar_amt = per_head / conversion_rate

    msg = '{} {} {} {} {} {}{}'.format('Everyone pays', final_winner(), '$',
                                     dollar_amt, 'using link',
                                     [x.ppid for x in list_of_players if x.name == final_winner()][0] + "/",
                                     dollar_amt)

    print msg


if __name__ == '__main__':
    create_players()
    get_scores()
    find_leader()
    game_status()
