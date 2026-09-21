def job_sequencing(jobs):
    # jobs: (job_id, deadline, profit)
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    max_d = max((d for _, d, _ in jobs), default=0)
    slot = [None] * (max_d + 1)
    profit = 0
    for job, deadline, value in jobs:
        for t in range(min(deadline, max_d), 0, -1):
            if slot[t] is None:
                slot[t] = job
                profit += value
                break
    return [x for x in slot[1:] if x is not None], profit

if __name__ == "__main__":
    jobs = [("J1", 2, 100), ("J2", 1, 19), ("J3", 2, 27), ("J4", 1, 25), ("J5", 3, 15)]
    print(job_sequencing(jobs))