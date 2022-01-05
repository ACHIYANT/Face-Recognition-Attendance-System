import time
import sys

def main(load1):
    for x in range(3):
        sys.stdout.write('\r{} |'.format(load1))
        time.sleep(0.1)
        sys.stdout.write('\r{} /'.format(load1))
        time.sleep(0.1)
        sys.stdout.write('\r{} -'.format(load1))
        time.sleep(0.1)
        sys.stdout.write('\r{} \\'.format(load1))
        time.sleep(0.1)
    # sys.stdout.write('\rLogin Success')

if __name__ == "__main__":
    main()