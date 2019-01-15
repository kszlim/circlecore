import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("-m", "--map", dest="map_id",
                    help="checks the leaderboard on the given beatmap id against each other")

argparser.add_argument("-u", "--user", dest="user_id",
                    help="checks only the given user against the other leaderboard replays. Must be set with -m")

argparser.add_argument("-l", "--local", help=("compare scores under the user/ directory to a beatmap leaderboard (if set with -m), "
                                             "a score set by a user on a beatmap (if set with -m and -u) or other locally "
                                            "saved replays (default behavior)"), action="store_true")

argparser.add_argument("-t", "--threshold", help="sets the similarity threshold to print results that score under it. Defaults to 20", type=int, default=20)

argparser.add_argument("-n", "--number", help="how many replays to get from a beatmap. No effect if not set with -m. Defaults to 50." 
                                              "PLEASE NOTE HIGHER NUMBERS TAKE EXPONENTIALLY LONGER.", default=50)