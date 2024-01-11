#!/usr/bin/env python3
"""A command-line utility to test the load-bearing capability of a website."""

import argparse
import multiprocessing.dummy as mp
import requests
import statistics
import sys


def setup_arg_parser():
    parser = argparse.ArgumentParser(
        description="A command-line utility to test the load-bearing capability of a website."
    )
    parser.add_argument(
        "-u", "--url", type=str, help="the URL of the website to test", required=True
    )
    parser.add_argument(
        "-n", "--num", type=int, help="the amount of requests to make", default=10
    )
    parser.add_argument(
        "-c",
        "--threads",
        type=int,
        help="the amount of threads to use for the test",
        default=2,
    )
    return parser.parse_args()


successful_requests = 0
failed_requests = 0
request_times: list[float] = []

args = setup_arg_parser()


def ping_provided_url(_: int) -> None:
    global successful_requests, failed_requests

    try:
        response = requests.get(args.url, timeout=1000)
        request_times.append(response.elapsed.total_seconds())

        if response.ok:
            successful_requests += 1
        else:
            failed_requests += 1
    except requests.exceptions.RequestException as ex:
        failed_requests += 1
        print(ex, file=sys.stderr, flush=True)


def print_stats() -> None:
    length = 46
    align_char = "."

    print("Results:")
    print(" Successful Requests".ljust(length, align_char) + ":", successful_requests)
    print(" Failed Requests".ljust(length, align_char) + ":", failed_requests)
    print()

    print(
        "Total Request Time (s) (Min, Max, Mean)".ljust(length, align_char) + ":",
        ", ".join(
            [
                f"{n:.4f}"
                for n in [
                    min(request_times),
                    max(request_times),
                    statistics.mean(request_times),
                ]
            ]
        ),
    )


def main() -> None:
    p = mp.Pool(args.num)
    p.map(ping_provided_url, range(args.num))
    p.close()
    p.join()

    print_stats()


if __name__ == "__main__":
    main()
