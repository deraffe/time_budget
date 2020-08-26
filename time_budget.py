#!/usr/bin/env python3
import argparse
import datetime
import logging

from durations import Duration

log = logging.getLogger(__name__)


def time_budget(
    interval: datetime.timedelta, time_avoided: datetime.timedelta,
    time_frame: datetime.timedelta
) -> datetime.timedelta:
    count = time_frame / interval
    budget = time_avoided * count
    return budget


def get_time(time_str: str) -> datetime.timedelta:
    dur = Duration(time_str)
    td = datetime.timedelta(seconds=dur.to_seconds())
    return td


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--loglevel', default='WARNING', help="Loglevel", action='store'
    )
    parser.add_argument('interval', help='How often does something happen?')
    parser.add_argument(
        'time_avoided',
        help=
        'What amount of time can be avoided each interval (by fixing, automating, etc)'
    )
    parser.add_argument(
        'time_frame',
        nargs='?',
        default='5y',
        help=
        'How long do you think this solution will be in use? (double your first estimate)'
    )
    args = parser.parse_args()
    loglevel = getattr(logging, args.loglevel.upper(), None)
    if not isinstance(loglevel, int):
        raise ValueError('Invalid log level: {}'.format(args.loglevel))
    logging.basicConfig(level=loglevel)
    interval = get_time(args.interval)
    time_avoided = get_time(args.time_avoided)
    time_frame = get_time(args.time_frame)
    budget = time_budget(interval, time_avoided, time_frame)
    print(budget)


if __name__ == '__main__':
    main()
