# AdventOfCode2016
Python code for the Advent Of Code puzzles for December 2016


http://adventofcode.com/

All code is in Python (tested on 3.5.2).


* Day 1 - Follow path w/ right/left directions.  Used complex numbers and segment intersection.
    This (part2) segment intersection could probably be made much simpler, to take advantage
    of the 90-degree turns (half of the segments to check are always going to be parallel).

* Day 2 - Follow up/right/down/left instructions.  Set up a state transition table to handle
    the boundaries.

* Day 3 - Parsing three numbers and checking if they make a triangle.  Part one had the values
    in a row, and this was quick and elegant to parse.  Part two had the values in columns,
    and that was uglier.

* Day 4 - Collections.Counter for character counting and custom dictionary sorting, with 
    regex parsing

* Day 5 - Looking for starting digits in an MD5 hash.  

* Day 6 - More string character counting, and custom dict sorting.

* Day 7 - Big ugly regex's for part two

* Day 8 - Use numpy matrix manipulation (np.roll) and matplotlib imshow to display the results

* Day 9 - Completed part one... need to work on part two

* Day 10 - Used a little class to store bot values and exit-condition instructions

* Day 11 - Skipping :(

* Day 12 - "Machine language" like instruction set

* Day 13 - Used a graph representation and Dijkstra's method for finding the shortest path.
