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
    n = 0
    while n < len(balls): #trying to iterate through the list of balls thrown and basically look at the odd ones, or the first one for each frame
        if balls[n] % 2 == 1:  # if the number is odd
            frame_score(balls) #if the number is odd, I want to calculate the score in that specific frame, if the throw isn't an odd number, then it's the second throw of a frame
        else:
            continue

def frame_score(balls): # here is where I'm trying to impliment the counting for each ball thrown and including the different rules for spares and strikes
    ball1 = balls[n] #first ball thrown in a given frame
    ball2 = balls[n + 1] #second ball thrown in a given frame
    next_one = balls[n + 2] #the first ball from the next frame
    next_two = next_one + balls[n + 3] #the second ball from the next frame, which I now see a bug I don't know how to fix.
    #bug to be fixed: ball1 = 10, so it's a strike, so then I take the next two balls and add them to it.  If ball3 is a 10, I also need to add ball5, if ball3 is not a 10, I just add ball4
    for ball1 in balls:
        if ball1 == 10:
            ball1 += next_two #if it's a strike, add the next two balls
        elif ball1 + ball2 == 10:
            ball2 += next_one #if it's a spare, add the next ball
        running_score += ball1 + ball2 #add both totals from this frame to the score
        return running_score #return the score and exit this loop


def test_bowling():
    assert   0 == bowling([0] * 20)
    assert  20 == bowling([1] * 20)
    assert  80 == bowling([4] * 20)
    assert 190 == bowling([9,1] * 10 + [9])
    assert 300 == bowling([10] * 12)
    assert 200 == bowling([10, 5,5] * 5 + [10])
    assert  11 == bowling([0,0] * 9 + [10,1,0])
    assert  12 == bowling([0,0] * 8 + [10, 1,0])

test_bowling()