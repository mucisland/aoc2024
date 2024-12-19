def occurrences_in_list(value: int, lst: list[int]) -> int:
    # Return the number of times value appears in lst.
    count: int = 0
    for ele in lst:
        if ele == value:
            count += 1
    return count

def main() -> int:
    left = []
    right = []
    with open("aoc2024_1_input.txt", "r") as f:
        for line in f:
            l, r = line.split()
            left.append(int(l.strip()))
            right.append(int(r.strip()))

    print(len(left))

    left.sort()
    right.sort()

    total_dist = 0
    for l, r in zip(left, right):
        dist = abs(l - r)
        print(l, r, dist)
        total_dist += dist

    print(f"Total distance: {total_dist}")


    similarity_score = 0
    for l, r in zip(left, right):
        tmp = l * occurrences_in_list(l, right)
        similarity_score += tmp

    print(f"Similarity Score: {similarity_score}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
