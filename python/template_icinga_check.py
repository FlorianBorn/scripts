#!/usr/bin/env python

# References:
# https://www.digitalocean.com/community/tutorials/how-to-create-nagios-plugins-with-python-on-ubuntu-12-10
# https://nagios-plugins.org/doc/guidelines.html

import argparse

def get_random_percentage():
    from random import randint
    return "{}%".format(randint(1, 100))


def main():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-c','--critical_threshold', help='On which threshold you want to return a critical?', required=False)
    parser.add_argument('-w','--warning_threshold', help='On which threshold you want to return a warning?', required=False)
    args = vars(parser.parse_args())

    random_perc = get_random_percentage()

    # Make warning and critical command line arguments mandatory.
    if random_perc >= args["critical_threshold"]:
        return 2

    if random_perc >= args["warning_threshold"]:
        return 1

    if random_perc < args["warning_threshold"]:
        return 0


if __name__ == '__main__':
    main()