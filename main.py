from argparse import ArgumentParser
import logging
from itertools import combinations


def main(plate_pair_weights):
    logger = logging.getLogger('main')
    logger.debug(f'main called with plate_pair_weights={plate_pair_weights}')

    print(f'Possible total weight amounts with available plates:')
    for number_pairs in range(1, len(plate_pair_weights)+1):
        for pair_combos in combinations(plate_pair_weights, number_pairs):
            print(sum([2 * pair_weight for pair_weight in pair_combos]))


if __name__ == '__main__':
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('main.log', 'w', 'utf-8')
    handler.setFormatter(logging.Formatter('%(name)s: %(message)s'))
    logger.addHandler(handler)


    parser = ArgumentParser()
    parser.add_argument('plate_pair_weights', type=int, nargs='*', help='weights representing different pairs of plates')
    args = parser.parse_args()


    main(args.plate_pair_weights)