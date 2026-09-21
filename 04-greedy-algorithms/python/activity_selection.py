def activity_selection(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    chosen = []
    end = None
    for start, finish in intervals:
        if end is None or start >= end:
            chosen.append((start, finish))
            end = finish
    return chosen

if __name__ == "__main__":
    print(activity_selection([(1, 3), (2, 4), (3, 5), (0, 7), (5, 9), (8, 9)]))