from argparse import ArgumentParser
import logging
from itertools import combinations


def weight_totals(plate_pair_weights):
    logger = logging.getLogger('main')
    logger.debug(f'weight_totals called with plate_pair_weights={plate_pair_weights}')

    weight_totals = []
    for number_pairs in range(1, len(plate_pair_weights)+1):
        for pair_combos in combinations(plate_pair_weights, number_pairs):
            weight_totals.append(sum([2 * pair_weight for pair_weight in pair_combos]))
    return weight_totals


def main(plate_pair_weights):
    logger = logging.getLogger('main')
    logger.debug(f'main called with plate_pair_weights={plate_pair_weights}')

    totals = [str(total) for total in weight_totals(plate_pair_weights)]
    print(f'Possible total weight amounts with available plates: {", ".join(totals)}')


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