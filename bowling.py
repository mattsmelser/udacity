"""
UNIT 1: Bowling:

You will write the function bowling(balls), which returns an integer indicating
the score of a ten-pin bowling game.  balls is a list of integers indicating
how many pins are knocked down with each ball.  For example, a perfect game of
bowling would be described with:

    >>> bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    300

The rules of bowling are as follows:

(1) A game consists of 10 frames. In each frame you roll one or two balls,
except for the tenth frame, where you roll one, two, or three.  Your total
score is the sum of your scores for the ten frames.
(2) If you knock down fewer than ten pins with your two balls in the frame,
you score the total knocked down.  For example, bowling([8, 1, 7, ...]) means
that you knocked down a total of 9 pins in the first frame.  You score 9 point
for the frame, and you used up two balls in the frame. The second frame will
start with the 7.
(3) If you knock down all ten pins on your second ball it is called a 'spare'
and you score 10 points plus a bonus: whatever you roll with your next ball.
The next ball will also count in the next frame, so the next ball counts twice
(except in the tenth frame, in which case the bonus ball counts only once).
For example, bowling([8, 2, 7, ...]) means you get a spare in the first frame.
You score 10 + 7 for the frame; the second frame starts with the 7.
(4) If you knock down all ten pins on your first ball it is called a 'strike'
and you score 10 points plus a bonus of your score on the next two balls.
(The next two balls also count in the next frame, except in the tenth frame.)
For example, bowling([10, 7, 3, ...]) means that you get a strike, you score
10 + 7 + 3 = 20 in the first frame; the second frame starts with the 7.

"""

running_score = 0

def bowling(balls):
    "Compute the total score for a player's game of bowling."
    ## bowling([int, ...]) -> int
    ## your code here
    total = 0
    frame_scores = []
    idx = 0
    while idx < len(balls):
        val = balls[idx]
        if len(frame_scores) >= 10:
            frame_scores.append(val)
            idx += 1
        elif val == 10:
            if idx == len(balls)-2:
                bonus_ball_1 = balls[idx + 1]
                idx += 1
                frame_scores.append(val + bonus_ball_1)
            elif idx == len(balls)-1:
                idx += 1
                frame_scores.append(val)
            else:
                bonus_ball_1 = balls[idx + 1]
                bonus_ball_2 = balls[idx + 2]
                frame_scores.append(val + bonus_ball_1 + bonus_ball_2)
                idx += 1
        else:  # Not a strike, could be spare or other
            if val + balls[idx + 1] == 10:
                next_ball = balls[idx + 1]
                bonus_ball = balls[idx + 2]
                frame_scores.append(val + next_ball + bonus_ball)
            else:
                next_ball = balls[idx + 1]
                frame_scores.append(val + next_ball)
            idx += 2  # skip second ball
    total = sum(frame_scores)
    return total







"""def test_bowling():
    assert   0 == bowling([0] * 20)
    assert  20 == bowling([1] * 20)
    assert  80 == bowling([4] * 20)
    assert 190 == bowling([9,1] * 10 + [9])
    assert 300 == bowling([10] * 12)
    assert 200 == bowling([10, 5,5] * 5 + [10])
    assert  11 == bowling([0,0] * 9 + [10,1,0])
    assert  12 == bowling([0,0] * 8 + [10, 1,0])

test_bowling()"""



print (bowling([10,10,10,10,10,10,10,10,10,10,10,9]))