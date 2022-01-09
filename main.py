from argparse import ArgumentParser
import logging
from itertools import combinations


def plate_weight_totals(plate_pair_weights):
    logger = logging.getLogger('main')
    logger.debug(f'weight_totals called with plate_pair_weights={plate_pair_weights}')

    weight_totals = []
    for number_pairs in range(1, len(plate_pair_weights)+1):
        for pair_combos in combinations(plate_pair_weights, number_pairs):
            weight_totals.append(sum([2 * pair_weight for pair_weight in pair_combos]))
    return weight_totals


def main(plate_pair_weights, bar_weight):
    logger = logging.getLogger('main')
    logger.debug(f'main called with plate_pair_weights={plate_pair_weights}, bar_weight={bar_weight}')

    plate_totals = plate_weight_totals(plate_pair_weights)
    plate_totals_str = ', '.join([str(total) for total in plate_totals])

    print(f'Possible total plate weight amounts with available plates: {plate_totals_str}')

    totals_with_bar = [plate_total + bar_weight for plate_total in plate_totals]
    totals_with_bar_str = ', '.join([str(total) for total in totals_with_bar])

    print(f'Possible total weight amounts (including bar) with available plates: {totals_with_bar_str}')


if __name__ == '__main__':
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('main.log', 'w', 'utf-8')
    handler.setFormatter(logging.Formatter('%(name)s: %(message)s'))
    logger.addHandler(handler)

    parser = ArgumentParser()
    parser.add_argument('plate_pair_weights', type=int, nargs='*', help='weights representing different pairs of plates')
    parser.add_argument('--bar', type=int, default=45)
    args = parser.parse_args()

    main(args.plate_pair_weights, args.bar)