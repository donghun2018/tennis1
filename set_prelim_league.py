# Set league groupings

from input_parser import *
from collections import deque
from math import ceil
from itertools import combinations
from random import shuffle

fns = {"princeton.csv",
       "columbia.csv",
       "cornell.csv",
       "pennstate.csv",
       "upenn.csv",
       "yale.csv"}
school_keys = ['Princeton',
               'Columbia',
               'Cornell',
               'Penn State',
               'UPenn',
               'Yale']
level_keys = ['A', 'B', 'C', 'D']

opt = {'avoid_same_school_in_prelim': True}

# input entries are put into num_courts leagues
def populate_league(entries, num_courts, rand_seed):
    entries.sort(key=lambda e: e.seed)
    num_league = num_courts
    leagues = [[] for _ in range(num_league)]   # leagues[l_ix][e_ix] = entry index e_ix in league l_ix

    ix_l = 0
    for ix_e, e in enumerate(entries):
        if ix_e % num_league != 0:
            if ix_e // num_league % 2 == 0:  # filling in league index order
                ix_l += 1
            else:                         # filling in reverse order
                ix_l -= 1
        leagues[ix_l].append(e)
    if opt['avoid_same_school_in_prelim'] is True:
        pass   # TODO: implement switcher algorithm
    return leagues

# if any entry plays back-to-back, match is invalid
# TODO suggestion: can accept up to 2 consecutive matches in prelim.
def check_match_validity(matches):
    match_valid = True
    match_seq = list(zip(matches[:-1], matches[1:]))
    for m2 in match_seq:
        for e in m2[0]:
            if any([e == e2 for e2 in m2[1]]) is True:
                match_valid = False
                return match_valid
    return match_valid

if __name__=="__main__":

    # init
    # entries_per_league = 3
    num_courts = 3   # number of available courts for level
    level_key = 'A'
    match_shuffle_max_tries = 100000

    entries = []
    for fn in fns:
        t = input_parser.simple_parser(fn)
        for e in t:
            if e.level == level_key:
                entries.append(e)
    entries.sort(key=lambda e: e.seed)

    # populate league
    leagues = populate_league(entries, num_courts, 1111)

    # build match order for each league
    leagues_match_order = []

    l = leagues[0]

    prelim_matches = []
    for l_ix, l in enumerate(leagues):
        matches = list(combinations(l, 2))
        # match validity checker
        shuffle_cnt = 0
        while(check_match_validity(matches) is False):
            # print("match invalid, reshuffling match order.")
            shuffle(matches)
            shuffle_cnt += 1
            if shuffle_cnt > match_shuffle_max_tries:
                print("max shuffle count reached. returning imperfect matching for league {}".format(l_ix))
                # TODO: minimize imperfection, instead of giving up
                break
        prelim_matches.append(matches)

    # print matches in order
    for m_ix, matches in enumerate(prelim_matches):
        print("-------------league {}------------".format(m_ix))
        for m in matches:
            print("{} VS. {}".format(m[0], m[1]))


    print(0)
