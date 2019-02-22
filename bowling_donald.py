def bowling(balls):
    "Compute the total score for a player's game of bowling."
    ## bowling([int, ...]) -> int
    ## your code here
    frame_scores = []
    idx = 0
    while idx < len(balls):
        val = balls[idx]
        if val == 10:
            bonus_ball_1 = balls[idx + 1]
            bonus_ball_2 = balls[idx + 2]
            frame_scores.append(val + bonus_ball_1 + bonus_ball_2)
            idx += 1
        else: #Not a strike, could be spare or other
            if val + balls[idx + 1] == 10:
                next_ball = balls[idx + 1]
                bonus_ball = balls[idx + 2]
                frame_scores.append(val + next_ball + bonus_ball)
            else:
                next_ball = balls[idx + 1]
                frame_scores.append(val + next_ball)
            idx += 2  # skip second ball