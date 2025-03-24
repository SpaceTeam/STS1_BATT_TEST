import argparse

def battery_test(dummy_arg):
    print(dummy_arg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script automatically tests battery cells.")
    parser.add_argument("-d", help="This is a dummy argument", default="dummy")
    args = parser.parse_args()

    battery_test(args.d)

    print("Bye.")
