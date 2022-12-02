from __future__ import annotations

import argparse
import os.path

import pytest

import support

import heapq

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')



def compute(s: str) -> int:
    top3 = [0,0,0]
    s = s[0:-1]
    for elf_list in s.split('\n\n'):
        elf_sum = 0
        for line in elf_list.split('\n'):
            elf_sum += int(line)
        heapq.heappushpop(top3,elf_sum)
    return sum(top3)



INPUT_S = '''\

'''
EXPECTED = 1


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
