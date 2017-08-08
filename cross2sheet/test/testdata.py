from cross2sheet.test.test import ImageTest
import unittest

class NowhereMan(ImageTest):
    url='2014/puzzle/puzzle_with_answer_nowhere_man/grid.png'
    rows=13
    cols=13
    fill='''
O............
.O...........
..O..........
...O.........
....O........
.............
.............
.............
........O....
.........O...
..........O..
...........O.
............O
'''
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           |             |
+-+ +-+   +-+ + +-+   +-+ +
| | | |       |           |
+ + + +   +-+ + +-+   +-+ +
|         | |         | | |
+     +-+ + +         + + +
|     | |                 |
+ + + + +-+ +-+ + +-+     +
| | |         | |         |
+ + +   + +   +-+ +-+-+ + +
|       | |         | | | |
+-+   + + +   +-+-+ + +-+ +
|     | |         | |     |
+ +-+ + +-+-+   + + +   +-+
| | | |         | |       |
+ + +-+-+ +-+   + +   + + +
|         | |         | | |
+     +-+ + +-+ +-+ + + + +
|                 | |     |
+ + +         + + +-+     +
| | |         | |         |
+ +-+   +-+ + +-+   + + + +
|           |       | | | |
+ +-+   +-+ + +-+   +-+ +-+
|             |           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class CrossPollinationA(ImageTest):
    url='2014/puzzle/cross_pollination/A.png'
    rows=15
    cols=15
    fill='''
......#....#...
......#....#...
......#........
##......#......
....##....#....
...#.....#.....
...#........###
......###......
###........#...
.....#.....#...
....#....##....
......#......##
........#......
...#....#......
...#....#......
'''
    cells_with_text='auto'

class CrossPollinationB(ImageTest):
    url='2014/puzzle/cross_pollination/B.png'
    rows=15
    cols=15
    fill='''
.....#.....#...
.....#.....#...
.....#.........
...#...#.......
....#.....#....
....#.....#....
.....#.....#...
###...###...###
...#.....#.....
....#.....#....
....#.....#....
.......#...#...
.........#.....
...#.....#.....
...#.....#.....
'''
    #broken
    #cells_with_text='auto'

class SamsYourUncle(ImageTest):
    url='2013/coinheist.com/feynman/sams_your_uncle/image00.png'
    rows=23
    cols=24
    cells_with_text='''
..*.**.***********.****.
*..**.**.....*..*....*..
**....*........*....*...
...*.*..*....*...***.*..
*.*.*..*..*..*..**..*...
*......*.*..*.....*...*.
**..*......**..**..*.*..
*..**.***.....*..*..*...
*.....*.......*.........
*.*.*.........*.*.**....
*....***......*......*..
*...*..*......*..*.**...
*.....*.*.....*...*.*...
*.*.*..*......***...*.*.
**...*.*..*****...*..*..
*..**..*.*..*.*..**.....
*....**.*.....*.*..**...
*.*...*.....*.....*...*.
*...*...*..*..*..*..**..
**.*..**..*..*.*.*...*..
.**.*.......*.....*.....
*...*...*.....*..*..*...
........................
'''
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                               |
+ +-+ +-+   +-+     + + + +     +   +-+ + +     +
|       |     |     | | | |     |       | |     |
+ +-+   +   + +     + + + + + + +   +-+ + +   + +
|           |           | | | |         |     | |
+ + + +   +-+ + +     + + + + +   + +-+-+ +-+ + +
| | | |       | |     | | |       |             |
+ + +-+ +     + +-+ +-+ + +-+ + +-+-+   +-+ +-+ +
|     | |     |           | | | |       |       |
+     +-+   + + +-+-+   +-+ + +-+   +   +   +-+ +
|           | |         |           |           |
+ +-+ +-+   + + +-+ + +-+-+   +-+   + +-+ +-+   +
|       |           | |       | |     |         |
+     +-+-+ + +-+-+ + + + + + + + +-+ + +       +
|           |           | | |     |     |       |
+   +-+   +-+-+   +     + + +-+   +     +-+     +
|           |     |                             |
+   +-+ + +-+-+   + +-+-+-+-+   +-+ +-+ +-+ +-+ +
|       |           |       |     | | |         |
+ +-+   + +-+-+-+-+ +       +     + + +-+-+-+-+ +
|           |       |       |                   |
+ +-+ +-+   + + +-+ +       + +-+ +   +-+-+ +-+ +
|       |     |     |       |     |     |       |
+ +-+ +-+-+ + + +-+ +       + +-+ + +   +-+ +-+ +
|           |       |       |     | |           |
+ +-+-+-+-+ + +     +       + +-+-+-+-+ +   +-+ +
|         | | |     |       |           |       |
+ +-+ +-+ +-+ +-+   +-+-+-+-+     +-+-+ + +-+   +
|                                   |           |
+     +-+     +   +-+ + +   +-+   +-+-+         +
|       |     |     | | |           |           |
+       + + +-+ +-+ + + + + + +-+-+ + +-+-+     +
|         |     |         | |           |       |
+   +-+ +-+ +   +-+   +-+-+ + +-+ + +   +-+ +-+ +
|           |           |         | |           |
+ +-+   +-+ +   +-+ + +-+   +-+-+ + +   +-+     +
|       |       | | | |           |     | |     |
+ +-+ +-+   +-+-+ + +-+ + +-+ +-+ +     + +-+ + +
|             |       | | |     | |       | | | |
+ + +-+ + +-+ + + + + + + +     + + +-+   + + + +
| |     |       | | | | |           |           |
+ +   + + +-+   + + + + + + +     + +   +   +-+ +
|     | |       |     | | | |     |     |       |
+     + + +-+   +     + + + +     +-+   +-+ +-+ +
|                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''

class FixesTheWavyZigzagJumble(ImageTest):
    url='2013/coinheist.com/rubik/fixes_the_wavy_zigzag_jumble/image00.png'
    rows=21
    cols=21
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           |         | |           |     |
+ +-+   +-+ + +-+ + + + + +-+ +-+ +-+   +-+
| |             | | | |           | |     |
+ +-+   +-+   +-+ + + +   +-+ +-+ + +   +-+
|         |         |           |         |
+ +-+ + +-+ + +-+ +-+     +-+-+ + + +   +-+
| | | |     | |             | | | | |     |
+ + +-+-+-+ +-+-+ +-+ +-+-+-+ + +-+ +-+-+-+
|         | | |     | |           |       |
+     +-+ + + +-+   + +-+ +-+   +-+-+   +-+
|           |         |         | |       |
+ + + +-+   + +-+-+ + +-+ +-+ +-+ +-+   +-+
| | | |         | | | |       |           |
+-+ + +-+ +-+ +-+ + + +-+ +-+ +-+ +-+ +-+-+
|       | |           | |       | | |     |
+   +-+ +-+-+ +-+ + +-+ + +-+ + + + +   +-+
|     | |         | |       | | |         |
+ + +-+ + + +-+-+ +-+ + + +-+ + +-+ +   +-+
| | |     | |       | | | |         |     |
+ +-+-+ + + + +-+-+ + + + +-+   +-+ +-+ +-+
|       | |                     | |       |
+-+ +-+ +-+   +-+ + + + +-+-+ + + + +-+-+ +
|     |         | | | |       | |     | | |
+-+   + +-+ + +-+ + + +-+ +-+-+ + + +-+ + +
|         | | |       | |         | |     |
+-+   + + + + +-+ + +-+ + +-+ +-+-+ +-+   +
|     | | |       | |           | |       |
+-+-+ +-+ +-+ +-+ +-+ + + +-+ +-+ +-+ + +-+
|           |       | | | |         | | | |
+-+   +-+ +-+ +-+ +-+ + +-+-+ +   +-+ + + +
|       | |         |         |           |
+-+   +-+-+   +-+ +-+ +   +-+ + + +-+     +
|       |           | |     | | |         |
+-+-+-+ +-+ + +-+-+-+ +-+ +-+-+ +-+-+-+ + +
|     | | | | |             | |     | | | |
+-+   + + + +-+-+     +-+ +-+ + +-+ + +-+ +
|         |           |         |         |
+-+   + + +-+ +-+   + + + +-+   +-+   +-+ +
|     | |           | | | |             | |
+-+   +-+ +-+ +-+ + + + + +-+ + +-+   +-+ +
|     |           | |         |           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class EvilInfluence(ImageTest):
    url='2012/puzzles/mayan_fair_lady/evil_influence/1s.png'
    rows=13
    cols=13
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+
| |               |       |
+ +   +   +-+ + + + +-+ +-+
|     |       | |         |
+ +   +   +-+ + +   +     +
| |       |         |     |
+ + +-+   + +-+-+   +     +
|     |     | |           |
+ +   + +-+ + +-+-+-+     +
| |       |     | |       |
+ +   +-+-+ + +-+ + +-+ + +
|         | |       | | | |
+-+-+ +-+ +-+ +-+   + +-+ +
|           | |           |
+ +-+ +   +-+ +-+ +-+ +-+-+
| | | |       | |         |
+ + +-+ + +-+ + +-+-+   + +
|       | |     |       | |
+     +-+-+-+ + +-+ +   + +
|           | |     |     |
+     +   +-+-+ +   +-+ + +
|     |         |       | |
+     +   + + +-+   +   + +
|         | |       |     |
+-+ +-+ + + + +-+   +   + +
|       |               | |
+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class Laureate(ImageTest):
    url='2011/puzzles/civilization/laureate/assets/grid.png'
    rows=9
    cols=17
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           |           |         |
+           + +         +   +     +
|             |             |     |
+           + +     +       +     +
|           |       |             |
+           +       +       +-+   +
|           |                     |
+-+ +-+   +-+   +               +-+
|               |                 |
+ +-+ +-+     +-+-+ +-+-+ +   +-+ +
|               |         |       |
+           +-+ + +-+     +       +
|                   |             |
+                   + +           +
|                     |           |
+             +       +   +       +
|             |           |       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class NinetyNineCentsAClue(ImageTest):
    url='2009/puzzles/99_cents_a_clue/PUZZLE/grid.png'
    rows=15
    cols=15
    fill='''
.........#....O
.#.#.#.#.#O#.#.
.O...#.........
.#.#.#.#.#.#O#.
O........#.....
.#.###O#.#.###.
..O.....#......
##.#.#.#.#.#.##
......#..O.....
.###.#.#O###.#.
.....#.........
.#O#.#.#.#.#.#.
......O..#.....
.#.#.#.#.#.#O#.
.....#.......O.
'''
    cells_with_text='auto'

class WorldsTallestCryptic(ImageTest):
    url='2008/world_s_tallest_cryptic/images/worldstallest.jpg'
    rows=38
    cols=13
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     | |       |     | | |
+ +-+-+ +-+-+ + +   +-+ + +
| |         | | |         |
+ + +-+ +-+ + + +   +-+ + +
|           |         | | |
+ + +-+ +-+ + + + +-+-+ + +
| | |     | | | | | |     |
+ + + +-+ + + + +-+ +-+ + +
|                   | | | |
+ + + +-+ + + + +-+ + + + +
| | |     | | |           |
+ + + +-+ + + +-+-+     + +
|       |       |       | |
+-+   +-+ + +-+-+ +-+ +-+ +
|     | | |       | |     |
+ + +-+ + +-+ +-+ + +-+ +-+
| | |                     |
+ +-+   +-+-+ +-+   +-+ + +
|                     | | |
+ +-+ +-+-+ + +-+     + + +
| | |       | |           |
+ + + +-+ + + + +     + + +
|       | |     |     | | |
+ +   +-+ + + + +-+ + + + +
| |       | | |     |     |
+ + +-+ +-+ + +-+ +-+ + + +
|     | |       |     | | |
+ +-+-+ +-+-+ + +   +-+ + +
| |         | | |         |
+ + +-+ +-+ + + +   +-+ + +
|           |         | | |
+ + +-+ +-+ + + + +-+-+ + +
| | |     | | | | | |     |
+ + + +-+ + + + +-+ +-+ + +
|                   | | | |
+ + + +-+ + + + +-+ + + + +
| | |     | | |           |
+ + + +-+ + + +-+-+     + +
|       |       |       | |
+-+   +-+ + +-+-+ +-+ +-+ +
|     | | |       | |     |
+ + +-+ + +-+ +-+ + +-+ +-+
| | |                     |
+ +-+   +-+-+ +-+   +-+ + +
|                     | | |
+ +-+ +-+-+ + +-+     + + +
| | |       | |           |
+ + + +-+ + + + +     + + +
|       | |     |     | | |
+ +   +-+ + + + +-+ + + + +
| |       | | |     |     |
+ + +-+ +-+ + +-+ +-+ + + +
|     | |       |     | | |
+ +-+-+ +-+-+ + +   +-+ + +
| |         | | |         |
+ + +-+ +-+ + + +   +-+ + +
|           |         | | |
+ + +-+ +-+ + + + +-+-+ + +
| | |     | | | | | |     |
+ + + +-+ + + + +-+ +-+ + +
|                   | | | |
+ + + +-+ + + + +-+ + + + +
| | |     | | |           |
+ + + +-+ + + +-+-+     + +
|       |       |       | |
+-+   +-+ + +-+-+ +-+ +-+ +
|       | |       |       |
+   +-+ + +-+     + +-+ +-+
|       |                 |
+ +-+   +-+             + +
| |                     | |
+ +-+   +-+   + +-+     + +
|             |           |
+ +-+   +-+ +-+ +-+     + +
| |                     | |
+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='''
**..**..*.*..
.*......*....
*.....*..*...
..**....*.*..
*............
..*....*.....
*...*.*.**.*.
*.*..*....*.*
.**.*........
*..*.........
..*....*.....
*....*..*....
.**.*..*.**..
**..**..*.*..
.*......*....
*.....*..*...
..**....*.*..
*............
..*....*.....
*...*.*.**.*.
*.*..*....*.*
.**.*........
*..*.........
..*....*.....
*....*..*....
.**.*..*.**..
**..**..*.*..
.*......*....
*.....*..*...
..**....*.*..
*............
..*....*.....
*...*.*.**.*.
*.*..*...**.*
**..*........
.*......*....
*.....**.....
****.*.*.****
'''

class GridWithAHoleInTheMiddle(ImageTest):
    url='2006/puzzles/cambridge/grid_with_a_hole_in_the_middle/grid.png'
    rows=11
    cols=11
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+
| |         |         |
+ + +-+     +   +-+ + +
|           |       | |
+   +-+   + +   +-+ + +
|         |           |
+ + +   +-+   + + + + +
| | |         | | | | |
+ + + +-+ + +-+ + + + +
|         |           |
+-+   +-+ +-+-+-+ +-+-+
|         |           |
+-+-+ +-+-+-+ +-+   +-+
|           |         |
+ + + + +-+ + +-+ + + +
| | | | |         | | |
+ + + + +   +-+   + + +
|           |         |
+ + +-+   + +   +-+   +
| |       |           |
+ + +-+   +     +-+ + +
|         |         | |
+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class WhoaIKnowWindows(ImageTest):
    url='2003/www.acme-corp.com/teamGuest/Training/images/windows.jpg'
    rows=12
    cols=12
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+
|         |             |
+-+     +-+ +-+   +-+ +-+
|             |       | |
+-+ +   +-+ +-+   +-+ + +
| | |       |           |
+ + +   + + +-+   +-+ + +
|       | |         | | |
+ + + + + +-+ +-+ +-+ + +
| | | | |       | |     |
+ +-+ +-+ +-+   + +-+-+ +
|       | |             |
+-+-+   + +   + +   +-+-+
|             | |       |
+ +-+-+ +   +-+ +-+ +-+ +
|     | |       | | | | |
+ + +-+ +-+ +-+ + + + + +
| | |         | |       |
+ + +-+   +-+ + +   + + +
|           |       | | |
+ + +-+   +-+ +-+   + +-+
| |       |             |
+-+ +-+   +-+ +-+     +-+
|             |         |
+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class InnerTube(ImageTest):
    url='2000/set3/1/grid.jpg'
    rows=13
    cols=13
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+
|               |         |
+-+     +-+ +-+ + +-+-+ + +
|         |         | | | |
+-+     +-+ +-+ + + + + + +
| |           | | |       |
+ +     +-+ +-+ + +   +-+ +
|         | |             |
+ +-+   +-+ +-+ +-+     + +
| | |         | |       | |
+ + +       +-+ +   +-+ + +
|           |           | |
+     +-+   +-+-+ +-+   + +
|       |         |       |
+ +   +-+ +-+-+   +-+     +
| |           |           |
+ + +-+   + +-+       + + +
| |       | |         | | |
+ +     +-+ +-+ +-+   +-+ +
|             | |         |
+ +-+   + + +-+ +-+     + +
|       | | |           | |
+ + + + + + +-+ +-+     +-+
| | | |         |         |
+ + +-+-+ + +-+ +-+     +-+
|         |               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class TheWickedSwitch(ImageTest):
    url='2012/puzzles/a_circus_line/the_wicked_switch/1.png'
    rows=13
    cols=13
    fill='''
...#....#....
...#....#....
.............
....##...#...
###.......###
...#...#.....
......#......
.....#...#...
###.......###
...#...##....
.............
....#....#...
....#....#...
'''
    cells_with_text='auto'

class PacificOvertones(ImageTest):
    url='2012/puzzles/ben_bitdiddle/pacific_overtones/1.png'
    rows=15
    cols=15
    fill='''
....##....#....
....#.....#....
....#.....#....
###.....OO...##
...O...........
......##...O...
.....##...#....
###.........###
....#...##.....
...#...O#......
...........#...
##...##.....###
....O.....#....
....#.....#....
....#....OO....
'''
    cells_with_text='''
****..****.****
*....*.....*...
*....*.....*...
...**.....*....
***.*...**...**
*..*....*...*..
*......*...*...
...*.**...*....
***..*....*.***
*...*....*.....
*..*...**...*..
..*....*...*...
**...**....****
*....*.....*...
*....*.....*...
'''

class OneMoreTry(ImageTest):
    url='2011/puzzles/mega_man/one_more_try/assets/grid.png'
    rows=25
    cols=25
    fill='''
###......##....#...##....
##........#.........#....
#.........#.........#....
......#....#.....##.....#
.....#......#...#.....###
..#....#........#........
##.......#....#.....#....
....#...#..........##....
...#....#...##....###....
...#....#.......#...##...
.......#...#....##......#
..#...#...#....#.......##
......#...........#......
##.......#....#...#...#..
#......##....#...#.......
...##...#.......#....#...
....###....##...#....#...
....##..........#...#....
....#.....#....#.......##
........#........#....#..
###.....#...#......#.....
#.....##.....#....#......
....#.........#.........#
....#.........#........##
....##...#....##......###
'''
    cells_with_text='auto'

class  DualSingularities(ImageTest):
    url='2009/puzzles/dual_singularities/PUZZLE/grid3.png'
    rows=17
    cols=17
    fill='''
.....#.....#.....
.....#.....#.....
.....#...........
......#......#...
###.....#.....###
....#......#.....
...#......###....
...#...#...#.....
........#........
.....#...#...#...
....###......#...
.....#......#....
###.....#.....###
...#......#......
...........#.....
.....#.....#.....
.....#.....#.....
'''
    cells_with_text='auto'

class Unspeakable(ImageTest):
    url='2007/puzzles/unspeakable/grid-1.png'
    rows=11
    cols=11
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+
|       |       |     |
+     + +     + +     +
|     |       |       |
+     + +     + +     +
|       |       |     |
+ +-+-+ + +-+   + +-+ +
|       |             |
+-+     +-+ +-+ +-+   +
|       |       |     |
+       + +   +-+     +
|         |     |     |
+     +-+ + +   +     +
|     |     |         |
+   +-+ +-+-+   +-+ +-+
|       |       |     |
+-+-+ + +   +-+ + +-+ +
|     |       |       |
+     + +     +   +   +
|       |         |   |
+       +       + +   +
|       |       |     |
+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class DealingWithChange(ImageTest):
    url='2003/www.acme-corp.com/teamGuest/4/images/dealing-with-change.jpg'
    rows=19
    cols=19
    fill='''
.....###....#.....#
......#.....#.....#
......#.....#......
..........#........
...#...###...##....
...#.....#.....####
....###....#.......
###................
.......##...##.....
...#.....#.....#...
.....##...##.......
................###
.......#....###....
####.....#.....#...
....##...###...#...
........#..........
......#.....#......
#.....#.....#......
#.....#....###.....
'''
    #broken
    #detects many extraneous vertical bars
    #cells_with_text='auto' works if bar detection disabled

class QED(ImageTest):
    url='2012/puzzles/ben_bitdiddle/qed/1.png'
    rows=9
    cols=9
    # the diagonal should be a very light gray; we don't detect this at the moment
    fill='''
....#....
....#....
...#....#
##...#...
..#...#..
...#...##
#....#...
....#....
....#....
'''
    cells_with_text='auto'

class PipeDream2(ImageTest):
    url='2011/puzzles/world1/pipe_dream_2/assets/grid.png'
    rows=7
    cols=7
    fill='''
....O..
..O...O
O...O#.
...#...
.#O...O
O...O..
..O....
'''
    cells_with_text='''
.***..*
*.....*
*..**.*
.**...*
..*....
.......
***..**
'''

class RumpledManWithABowlCut(ImageTest):
    url='2009/puzzles/the_rumpled_man_with_a_bowl_cut/PUZZLE/600px-acrostic.png'
    rows=3
    cols=18
    fill='''
..#..#...#........
..#....#...#.....#
.........#.#.....# 
'''
    cells_with_text='''
**.**.***.********
**.****.***.*****.
*********.*.*****.
'''

class GoodTimesInTheCasino(ImageTest):

    url='2011/puzzles/mega_man/good_times_in_the_casino/assets/grid.png'
    rows=13
    cols=21
    fill='''
......##....#........
.#.#.#.#.#.#.#.#.#.#.
.......#.......#.....
##.#.#.#####.#.#.#.#.
.....#........#......
.#####.#.#.#.#.#.#.#.
.......#.....#.......
.#.#.#.#.#.#.#.#####.
......#........#.....
.#.#.#.#.#####.#.#.##
.....#.......#.......
.#.#.#.#.#.#.#.#.#.#.
........#....##......
'''
    cells_with_text='auto'

class CurseOfTheAtlanteansTomb(ImageTest):
    url='2015/puzzle/the_curse_of_the_atlanteans_tomb/images/curse-of-the-atlantean-tomb.png'
    rows=19
    cols=39
    #broken
    #fill
    #cells_with_text='auto'

class TwistsAndTurns(ImageTest):
    url='2003/www.acme-corp.com/teamGuest/6/images/twists-and-turns.jpg'
    rows=12
    cols=12
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+
|     |     |     |     |
+ +-+ + +-+ + +-+ + +-+ +
|   | |   | | |   | |   |
+-+ + +-+ + + + +-+ + +-+
|   | |   |   |   | |   |
+ +-+ + +-+-+-+-+ + +-+ +
|   |   |   |   |   |   |
+-+ +-+-+ + + + +-+-+ +-+
|   |     | | |     |   |
+ +-+ +-+-+ + +-+-+ +-+ +
|     |     |     |     |
+-+-+-+ +-+-+-+-+ +-+-+-+
|     |     |     |     |
+ +-+ +-+-+ + +-+-+ +-+ +
|   |     | | |     |   |
+-+ +-+-+ + + + +-+-+ +-+
|   |   |   |   |   |   |
+ +-+ + +-+-+-+-+ + +-+ +
|   | |   |   |   | |   |
+-+ + +-+ + + + +-+ + +-+
|   | |   | | |   | |   |
+ +-+ + +-+ + +-+ + +-+ +
|     |     |     |     |
+-+-+-+-+-+-+-+-+-+-+-+-+
'''

class ThatsRight(ImageTest):
    url='2003/www.acme-corp.com/teamGuest/7/images/thats-right.jpg'
    rows=12
    cols=12
    cells_with_text='''
*.**.*.*..**
.*.*........
....*....**.
..*.........
*....*.*..*.
....*.......
..***.......
.*.......***
..*.....*...
.**....*....
...*.**...*.
**..*.*.*.*.
'''

class PipeDream(ImageTest):
    url='2006/puzzles/epcot_center/pipe_dream/pipedreamgrid.png'
    rows=9
    cols=9
    fill='''
.........
...#.....
......#..
..#.....#
....#....
#.....#..
..#......
.....#...
.........
'''
    cells_with_text='''
**.*.**.*
..*.*...*
.....*.*.
*..**....
*.*...*.*
..*......
*........
*.*...*.*
*....**.*
'''

class WhenNotInRome(ImageTest):
    url='2007/puzzles/when_not_in_rome/grid.png'
    rows=13
    cols=13
    fill='''
.......#.....
.#.#.#.#.#.#.
.....#.......
.#.#.#.#.#.#.
........#....
.###.#.#.#.#.
#.....#.....#
.#.#.#.#.###.
....#........
.#.#.#.#.#.#.
.......#.....
.#.#.#.#.#.#.
.....#.......
'''

class HowFar(ImageTest):
    url='2016/puzzle/how_far/images/howfargrid.png'
    rows=17
    cols=17
    cells_with_text='auto'
    #broken
    #dark squares are considered as light squares with bars on all sides

class ManInTheMoon(ImageTest):
    url='2016/puzzle/the_man_in_the_moon/images/puzzle.pdf'
    rows=12
    cols=12
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+
|           |           |
+     +-+   + +-+ + +-+ +
|               | | | | |
+ + + +-+     +-+ + + + +
| | | |                 |
+ + + +-+ +   +-+     + +
|         |           | |
+     +-+ + + +-+     + +
|           |           |
+ +-+ +-+ +-+ +-+ + + + +
|             | | | | | |
+-+ +-+ + +   + + +-+ +-+
| | | | | |             |
+ + + + +-+ +-+ +-+ +-+ +
|           |           |
+ +     +-+ + + +-+     +
| |           |         |
+ +     +-+   + +-+ + + +
|                 | | | |
+ + + + +-+     +-+ + + +
| | | | |               |
+ +-+ + +-+ +   +-+     +
|           |           |
+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class CrossedSwords(ImageTest):
    url='2010/puzzles/1752/crossed_swords/crossed_swords.gif'
    rows=15
    cols=15
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|       |             |       |
+ +-+   +-+   +-+ +-+ + +-+ + +
|         |               | | |
+ +-+     + +     +-+ + +-+ + +
|           |         |       |
+ +-+     +-+ + + +-+ + +-+   +
|             | | | |         |
+ +-+-+     +-+ + + +-+     +-+
| | |           |           | |
+-+ +-+     + + +-+       +-+ +
|           | |               |
+   +-+     + +-+-+   +-+   + +
|               |           | |
+     +-+-+   +-+ +-+ +-+   + +
|         |         |         |
+ +   +-+ +-+ +-+   +-+-+     +
| |           |               |
+ +   +-+   +-+-+ +     +-+   +
|               | |           |
+ +-+       +-+ + +     +-+ +-+
| |           |           | | |
+-+     +-+ + + +-+     +-+-+ +
|         | | | |             |
+   +-+ + +-+ + + +-+     +-+ +
|       |         |           |
+ + +-+ + +-+     + +     +-+ +
| | |               |         |
+ + +-+ + +-+ +-+   +-+   +-+ +
|       |             |       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    #broken
    #cells_with_text works on my system but not on TravisCI
    #cells_with_text='auto'
    #highlighted squares on diagonal

class IndescribableAmorphousCryptic(ImageTest):
    url='2016/puzzle/the_indescribable_amorphous_cryptic/images/puzzle.pdf'
    rows=13
    cols=13
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           |             |
+     +-+ +-+-+ +-+ +-+ + +
|       | |         | | | |
+ + + +-+ + +-+ +-+ + + + +
| | |             |       |
+ + + +-+ + +-+ +-+   + + +
|         |           | | |
+-+ +-+ + + +-+ +-+   + + +
| | | | | |               |
+ + + + + + + +-+-+       +
|           | |           |
+ +-+ +     + +-+   + +-+ +
|     |             |     |
+ +-+ +   +-+ +     + +-+ +
|           | |           |
+       +-+-+ + + + + + + +
|               | | | | | |
+ + +   +-+ +-+ + + +-+ +-+
| | |           |         |
+ + +   +-+ +-+ + +-+ + + +
|       |             | | |
+ + + + +-+ +-+ + +-+ + + +
| | | |         | |       |
+ + +-+ +-+ +-+-+ +-+     +
|             |           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class TheCapriciousType(ImageTest):
    url='2010/puzzles/2000/the_capricious_type/the_capricious_type.gif'
    rows=12
    cols=12
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+
|           |           |
+ +-+     +-+ +-+   +-+ +
|         |           | |
+ + +     +     +   +-+ +
| | |           |       |
+ + +       +   + +-+   +
|           |     |     |
+ +     +-+ + +-+ +     +
| |       | |           |
+ +-+ +-+ + +   +-+     +
|     |                 |
+-+   +   +     +-+ +-+-+
|         |     |       |
+       +-+ +-+-+ +-+-+ +
|       | |     |       |
+ + +-+ + +-+ +-+ +-+   +
| | | |           |     |
+ + + +-+     +-+ +     +
|             | |       |
+ +-+ +-+ +   + +-+ + + +
|         |         | | |
+ +-+ +-+ +-+   +-+ +-+ +
|           |           |
+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

@unittest.skip('dimensions not detected correctly')
class CrossExamination(ImageTest):
    url='2008/cross_examination/images/crossexamination.gif'
    rows=13
    cols=13

class JoinedAtTheHip(ImageTest):
    url='2006/puzzles/mcmurdo_station/joined_at_the_hip/puzzle.pdf'
    rows=13
    cols=13
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         |             | |
+ +-+ +-+ + +-+ + +-+ +-+ +
| |           | |         |
+ +   +-+ + +-+ + +-+ + + +
|       | | |       | | | |
+-+ + +-+ + +-+ + +-+ + + +
| | | |         | |       |
+ + + +-+ + + +-+ +-+     +
|         | |             |
+ + + +-+-+ + +-+ + +-+ + +
| | |           | | | | | |
+ +-+     +-+ +-+ + + +-+ +
|           | |           |
+ +-+ + + +-+ +-+     +-+ +
| | | | | |           | | |
+ + +-+ + +-+ + +-+-+ + + +
|             | |         |
+     +-+ +-+ + + +-+ + + +
|       | |         | | | |
+ + + +-+ + +-+ + +-+ + +-+
| | | |       | | |       |
+ + + +-+ + +-+ + +-+   + +
|         | |           | |
+ +-+ +-+ + +-+ + +-+ +-+ +
| |             |         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class MysteriousCryQuietHabit(ImageTest):
    url='2006/puzzles/kuala_lumpur/mysterious_cry_quiet_habit/grid.png'
    rows=26
    cols=21
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     | |                                 |
+-+-+-+ +-+-+-+-+                         +
|               |                         |
+-+-+-+ +-+-+ +-+             +-+         +
|     | |   | |               | |         |
+     + +   + +     +-+       + +         +
|     | |   | |     | |       | |         |
+     + +   + + +-+ + +-+-+-+-+ +         +
|     | |   | | | | |           |         |
+     + +   + + + + + +-+-+-+-+ +         +
|     | |   | | | | | |       | |         |
+     + +-+-+ +-+ +-+ +       + +         +
|     |               |       | |         |
+     +-+-+-+-+-+ +-+ +       + +         +
|               | | | |       | |         |
+               + + +-+ +-+-+-+ +-+-+     +
|               | |     |           |     |
+     +-+   +-+-+ +-+-+ +-+-+-+ +-+-+     +
|     | |   |         |       | |         |
+     + +   + +-+-+ +-+       +-+         +
|     | |   | |   | |                     |
+     + +   + +   + +         +-+         +
|     | |   | |   | |         | |         |
+   +-+ +-+-+ +-+ + +-+-+-+-+-+ +         +
|   |           | |             |         |
+   +-+ +-+-+-+-+ +-+-+-+-+-+-+ +         +
|     | |                     | |         |
+     + +-+-+-+-+-+-+   +-+-+-+ +-+-+-+-+-+
|     |             |   |                 |
+     + +-+-+-+ +-+ +   +-+ +-+ +-+-+-+-+-+
|     | |     | | | |     | | | |         |
+     + + +-+-+ +-+ +-+-+ + +-+ +-+       +
|     | | |             | |       |       |
+     + + + +-+ +-+ +-+-+ + +-+ +-+       +
|     | | | | | | | |     | | | |         |
+     +-+ + + + + +-+     + + + +         +
|         | | | |         | | | |         |
+         + + + + +-+-+-+-+ + +-+         +
|         | | | | |         |             |
+         + + +-+ +-+-+-+-+-+             +
|         | |                             |
+         + +-+-+-+-+-+-+-+               +
|         |               |               |
+         + +-+-+ +-+-+ +-+               +
|         | |   | |   | |                 |
+         + +   + +   + +                 +
|         | |   | |   | |                 |
+         + +   + +-+-+ +-+-+-+           +
|         | |   |             |           |
+         + +   + +-+-+ +-+-+-+           +
|         | |   | |   | |                 |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''

class CommonBonds05(ImageTest):
    url='2005/setec/common_bonds/COMMON_BONDS.pdf'
    rows=13
    cols=13
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+
|       |         |       |
+       +       +-+       +
|               |         |
+               + +       +
|                 |       |
+ +-+-+ +-+   +-+ +-+     +
|       |       | |       |
+   +-+ + +-+-+ + +   +-+ +
|           |         | | |
+-+   +-+   + +     +-+ + +
|             |           |
+ + + + +     +   + + + + +
| | | | |         | | | | |
+ + + + +   +     + + + + +
|           |             |
+ + +-+     + +   +-+   +-+
| | |         |           |
+ +-+   + + +-+-+ + +-+   +
|       | |       |       |
+     +-+ +-+   +-+ +-+-+ +
|       |                 |
+       + +               +
|         |               |
+       +-+       +       +
|       |         |       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='auto'

class SixOfOne(ImageTest):
    url='2005/setec/six_of_one/six%20of%20one.pdf'
    rows=13
    cols=13
    fill='''
O............
O...........O
.............
...O.........
.........O...
..........O..
...........O.
.............
.....O.......
.............
.............
.........O...
....O........
'''
    bars='''
+-+-+-+-+-+-+-+-+-+-+-+-+-+
|             |           |
+-+     +-+   +   +-+   +-+
| |     |                 |
+ +     +-+     + +-+   +-+
|               | |       |
+ + + +-+       + +-+-+ +-+
| | | | |           |     |
+ + +-+ + + +-+   +-+     +
|         |       | |     |
+ + +-+   +-+-+   + +-+ + +
| | |               | | | |
+ +-+   +-+-+   +-+ + +-+ +
| |                     | |
+ +     + +-+ +-+   + +-+ +
|       |           |     |
+ + + +-+ +-+ +-+   +     +
| | | |                   |
+-+ +-+   +-+ +-+ + + + + +
| | |             | | | | |
+ + +     +-+   +-+ +-+ + +
|               |         |
+ + +   +-+-+   +-+-+ + + +
| | |               | | | |
+ + + +-+-+-+   +-+-+ + + +
|       |               | |
+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
    cells_with_text='''
.**..****.**.
.*...........
*...*....*...
....*.....*.*
*....*....*..
..*...*......
.*..*...*....
*...*.....**.
...*.........
*.*....*.....
*.......*.*..
.............
*............
'''

class LeadWithHydrogen(ImageTest):
    url='2017/assets/lead_with_hydrogen/puzzle.png'
    rows=11
    cols=11
    fill='''
.....#....#
.#.#.#.##.#
.....#.....
.#......#.#
...........
....#.#....
...........
#.#......#.
.....#.....
#.##.#.#.#.
#....#.....
'''
    cells_with_text='auto'

class CrimesAgainstCruciverbalism(ImageTest):
    url='2016/puzzle/crimes_against_cruciverbalism/images/puzzle.pdf'
    rows=15
    cols=15
    fill='''
....#.....#....
....#.....#....
....#.....#....
....#....#.....
...#....#...###
.......#...#...
##...##...#....
...............
....#...##...##
...#...#.......
###...#....#...
.....#....#....
....#.....#....
....#.....#....
....#.....#....
'''
    cells_with_text='auto'

del ImageTest
