"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """

    if(ctx.start == ctx.goal):
        return [ctx.start]

    queue = deque([ctx.start])
    current = ctx.start
    frontier = []
    parent = {ctx.start: None}
    visited = set()
    visited.add(ctx.start)

    while queue:
        current = queue.popleft()

        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)

        frontier = ctx.expand(current, len(frontier) + 1)

        for nxt in frontier:
            if nxt not in visited:
                queue.append(nxt)
                parent[nxt] = current
                visited.add(nxt)

    return []


def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """

    if(ctx.start == ctx.goal):
        return [ctx.start]

    stack = [ctx.start]
    current = ctx.start
    frontier = []
    parent = {ctx.start: None}
    visited = set()
    visited.add(ctx.start)

    while stack:
        current = stack.pop()

        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)

        frontier = ctx.expand(current, len(frontier) + 1)

        for nxt in frontier:
            if nxt not in visited:
                stack.append(nxt)
                parent[nxt] = current
                visited.add(nxt)

    return []




def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """

    if(ctx.start == ctx.goal):
        return [ctx.start]

    frontier = []
    limit = 0
    num_rows = len(ctx.grid)
    num_cols = len(ctx.grid[0])
    max_depth = num_rows * num_cols - 1

    while limit <= max_depth:
        stack = [(ctx.start, 0, [ctx.start])]
        parent = {ctx.start: None}

        while stack:
            current, depth, path = stack.pop()

            if current == ctx.goal:
                return reconstruct(parent, ctx.goal)

            if depth >= limit:
                continue

            frontier = ctx.expand(current, len(frontier) + 1)

            for nxt in frontier:
                if nxt not in path:
                    stack.append((nxt, depth + 1, path + [nxt]))
                    parent[nxt] = current

        limit += 1

    return []



def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """

    if(ctx.start == ctx.goal):
        return [ctx.start]

    heap = []
    heappush(heap, (0 + ctx.heuristic(ctx.start), 0, ctx.start))
    frontier = []
    parent = {ctx.start: None}
    current_costs = {ctx.start: 0}

    while heap:
        priority, cost_so_far, current = heappop(heap)

        if cost_so_far != current_costs[current]:
            continue

        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)

        frontier = ctx.expand(current, len(frontier) + 1)

        for nxt in frontier:
            if nxt not in current_costs or cost_so_far + 1 < current_costs[nxt]:
                heappush(heap, (cost_so_far + 1 + ctx.heuristic(nxt), cost_so_far + 1, nxt))
                parent[nxt] = current
                current_costs[nxt] = cost_so_far + 1

    return []
