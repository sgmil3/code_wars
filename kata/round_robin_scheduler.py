"""
Name: Round Robin Scheduler
Link: https://www.codewars.com/kata/561c20edc71c01139000017c
Level: 4kyu
Desc.: Organize a round-robin tournament schedule for a given number of teams
Finished: Yes
"""


def shift_round_wheel(top: list[int], bottom: list[int]) -> list[int]:

    first = top.pop(0)
    assert first == 1

    new_top = [bottom.pop(0)] + top[:-1]
    new_bottom = bottom + [top[-1]]

    return [first] + new_top, new_bottom


if __name__ == "__main__":
    N = 2
    teams = [i for i in range(1, N + 1)]
    schedule = []

    top, bottom = teams[: N // 2], teams[N // 2 :][::-1]

    for rnd in range(1, N):
        schedule.append(list(zip(top, bottom)))

        if len(schedule) == N - 1:
            break

        top, bottom = shift_round_wheel(top, bottom)

    print(schedule)
