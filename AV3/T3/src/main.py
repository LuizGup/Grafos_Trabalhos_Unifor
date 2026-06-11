import sys
from tshirt_network import build_network
from ford_fulkerson import FordFulkerson


def main():
    data = sys.stdin.read().split()
    idx = 0

    T = int(data[idx]); idx += 1

    for _ in range(T):
        N = int(data[idx]); idx += 1
        M = int(data[idx]); idx += 1

        preferences = []
        for _ in range(M):
            s1 = data[idx]; idx += 1
            s2 = data[idx]; idx += 1
            preferences.append((s1, s2))

        G, source, sink = build_network(N, M, preferences)
        ff = FordFulkerson(G, source, sink)

        print("YES" if ff.value == M else "NO")


if __name__ == "__main__":
    main()
