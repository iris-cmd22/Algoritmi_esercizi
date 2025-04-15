
def dynamic_ladri(array,max_capacity):
    bag = [0 for _ in range(max_capacity+1)]

    for i in range(max_capacity+1):
        for j in range(len(array)):
            value=array[j]
            if(value<i):
                bag[i]=max(bag[i],bag[i-value]+value)
    return bag[max_capacity]


def readTestFile(path):
    
    file = open(path, "r")
    testsList = []

    for line in file:
        testsList.append([int(x) for x in line.split(' ')])
    
    return testsList

if __name__ == "__main__":

    with open("./test_file.txt") as file:

        num_test = int(file.readline())

        while num_test > 0:

            num_elements=int(file.readline())

            data = file.readline().strip().split()
            array = [int(x) for x in data]

            print(array)

            #Somma degli elementi e divido floor per 2 ladri
            sum=0
            for i in range(len(array)-1):
                sum+=array[i]
            min_partition=dynamic_ladri(array,sum//2)
            differenza=sum-min_partition
            print(differenza)

            num_elements=0

            num_test -= 1
        