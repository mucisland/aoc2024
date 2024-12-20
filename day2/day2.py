
# INPUT_FILE = "day2_example_input.txt"
INPUT_FILE = "day2_input.txt"

def main() -> int:
    safe_report_count = 0
    with open(INPUT_FILE, "r") as f:
        for i, line in enumerate(f):
            report = [int(level.strip()) for level in line.split()]
            if is_safe(report):
                print(f"safe report: {i}")
                safe_report_count += 1
            else:
                print(f"unsafe report: {i}")
    print(f"{safe_report_count=}")

    # Consider the problem dampener.
    safe_report_count = 0
    with open(INPUT_FILE, "r") as f:
        for i, line in enumerate(f):
            report = [int(level.strip()) for level in line.split()]
            for x in range(len(report)):
                new_report = report[:]
                del new_report[x]
                if is_safe(new_report):
                    safe_report_count += 1
                    break
    print(f"With Problem Dampener: {safe_report_count=}")

    return 0

def sign(num: int) -> int:
    if num < 0:
        return -1
    return 1

def is_safe(report: list[int]) -> bool:
    return not is_unsafe(report)

def is_unsafe(report: list[int]) -> bool:
    refsign = sign(report[1] - report[0])
    for i in range(len(report) - 1):
        dist = report[i + 1] - report[i]
        # print(f"{report[i + 1]} {report[i]} {dist}")
        if sign(dist) != refsign:
            return True
        if 1 <= abs(dist) <= 3:
            continue
        return True
    return False



if __name__ == "__main__":
    raise SystemExit(main())
