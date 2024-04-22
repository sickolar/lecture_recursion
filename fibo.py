def recursive_nth_fibo(cislo):
    if cislo <= 1:
        return cislo
    else:
        return recursive_nth_fibo(cislo - 1) + recursive_nth_fibo(cislo - 2)


def main():
    print(recursive_nth_fibo(8))
    pass


if __name__ == "__main__":
    main()
