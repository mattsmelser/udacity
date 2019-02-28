N = 8

def solve_parking_puzzle(start, N=N):
    """Solve the puzzle described by the starting position (a tuple
    of (object, locations) pairs).  Return a path of [state, action, ...]
    alternating items; an action is a pair (object, distance_moved),
    such as ('B', 16) to move 'B' two squares down on the N=8 grid."""
    return shortest_path_search(grid(start, N), psuccessors, is_goal)

def is_goal(state):
    "Goal is when the car (*) overlaps a goal square (@)."
    d = dict(state)
    return set(d['*']) & set(d['@'])

def psuccessors(state):
    """State is a tuple of (('c': sqs),...); return a {state:action} dict
    where action is of form ('c', dir), where dir is +/-1 or +/-N."""
    results = {}
    occupied = set(s for (c, sqs) in state for s in sqs if c != '@')
    for (c, sqs) in state:
        if c not in '|@': # Walls and goals can't move
            diff = sqs[1]-sqs[0]
            # Either move the max of sqs up, or the min of sqs down
            for (d, start) in [(diff, max(sqs)), (-diff, min(sqs))]:
                for i in range(1, N-2):
                    s = start + d*i
                    if s in occupied:
                        break # Stop when you hit something
                    results[update(state,c,tuple(q+d*i for q in sqs))]=(c,d*i)
    return results

def update(tuples, key, val):
    "Return a new (key, val) tuple, dropping old value of key and adding new."
    # Sort the keys to make sure the result is canonical.
    d = dict(tuples)
    d[key] = val
    return tuple(sorted(d.items()))

def locs(start, n, incr=1):
    "Return a tuple of n locations, starting at start and go up by incr."
    return tuple(start+i*incr for i in range(n))

def grid(cars, N=N):
    """Return a tuple of (object, locations) pairs -- the format expected for
    this puzzle.  This function includes a wall pair, ('|', (0, ...)) to
    indicate there are walls all around the NxN grid, except at the goal
    location, which is the middle of the right-hand wall; there is a goal
    pair, like ('@', (31,)), to indicate this. The variable 'cars'  is a
    tuple of pairs like ('*', (26, 27)). The return result is a big tuple
    of the 'cars' pairs along with the walls and goal pairs."""
    goals = ((N**2)//2 - 1,)
    walls = (locs(0, N) + locs(N*(N-1), N) + locs(N, N-2, N)
             + locs(2*N-1, N-2, N))
    walls = tuple(w for w in walls if w not in goals)
    return cars + (('|', walls), ('@', goals))