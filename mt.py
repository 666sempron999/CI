import numpy as np

def main():
    res = np.random.rand(100, 100)
    with open('test.npy', 'wb') as f:
        np.save(f, res)


if __name__ == '__main__':
    main()
