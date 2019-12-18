#!/usr/bin/env python3

# Algorithm

FREE_CONTINGENT = 1024 # bytes
MULTIPLIER = 2 # atomics

def transaction_size_fee(size):
    paid_size = max(0, size - FREE_CONTINGENT)
    return (paid_size ** 2) * MULTIPLIER

# Simulation

SIZE_START=0
SIZE_END=500*1024
SIZE_STEP=256
IOV = 10**9 #atomics
ANTISPAM = 5 * 10**8 # i.e. 0.5 IOV

def print_csv_row(a, b, c):
    print("{},{},{}".format(a, b, c))

print_csv_row('"tx size"', '"size fee (IOV)"', '"price increase compared to anti spam"')

for tx_size in range(SIZE_START, SIZE_END + 1, SIZE_STEP):
    atomics = transaction_size_fee(tx_size)

    relative = (ANTISPAM+atomics)/ANTISPAM

    price_in_iov = atomics / IOV

    print_csv_row(
        tx_size,
        "{:.4f}".format(price_in_iov),
        "{:.4f}".format(relative)
        )
