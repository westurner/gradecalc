#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
grade_calc
"""


def grade_calc(current_grade, desired_grade, final_exam_weight=0.20):
    """
    to start with:
    calculate the minimum necessary(*) to receive the desired grade
    given the current_grade and the final exam weight

    (current_grade*(1-final_exam_weight))+(x*final_exam_weight) = desired_grade

    x = (desired_grade-(current_grade*(1-final_exam_weight))) / final_exam_weight)
    """
    return (desired_grade-(current_grade*(1-final_exam_weight))) / final_exam_weight

def grade_range(current_grade, final_exam_weight=0.20, intervals=range(60,105,5)):
    for desired_grade in intervals:
        yield (desired_grade, grade_calc(current_grade, desired_grade, final_exam_weight))

import unittest
class Test_grade_calc(unittest.TestCase):
    def test_grade_calc(self):
        IO = (
            ( (80, 80, .20), 80 ),
            ( (95, 93, .20), 85 ),
        )
        for args, expected_output in IO:
            print(args, "should be", expected_output, end='...')
            actual_output = grade_calc(*args)
            print(actual_output)
            self.assertAlmostEqual(actual_output, expected_output)

    def test_grade_range(self):
        current_grade=80
        final_weight=0.20
        print("Given a current grade of %.2f, where the final is worth %.2f%%" % (current_grade, final_weight))
        for desired_grade, minimum_necessary_final_grade in grade_range(current_grade, final_weight):
            print("%7.2f%% ... %.2f%%" % (desired_grade, minimum_necessary_final_grade))

def main():
    import optparse
    import logging

    prs = optparse.OptionParser(usage="./%prog : args")

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',)
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',)
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',)

    (opts, args) = prs.parse_args()

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        import sys
        sys.argv = [sys.argv[0]] + args
        import unittest
        exit(unittest.main())

    grade_calc()

if __name__ == "__main__":
    main()
