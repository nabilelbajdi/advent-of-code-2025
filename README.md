# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Notes

**Day 1**: Nice warmup! Part 1 was straightforward, just track the dial and count zeros. Part 2 tripped me up at first cause I was only checking if we ended on zero, not counting all the times we pass through it during the rotation. Took me a minute to realize that. Once I got it, just had to check each position we pass through.

**Day 2**: Fun one. Started part 1 by just iterating through all the numbers in each range and checking them... yeah that didn't work, way too slow. Had to actually think about how to generate the invalid IDs directly. Part 2 was similar but now checking for any repeating pattern, not just two repeats. Ended up being cleaner than I thought it would be.
