import sys

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    with open('bubble_sort_data', 'a') as f:
        for i in range(len(data)):
            f.write(data[i]+" ")
    f.close()

def main(unsort_data):
    f = open(unsort_data, 'r')
    data = f.read().split()
    bubble_sort(data)
    f.close()

if __name__ == '__main__':
    main(sys.argv[1])
