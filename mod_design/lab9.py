import json
# 1. Name:
#      Mike Downs
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This program is meant to take a list of numbers or strings and sort it by small peices.  

# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of the assignment was making a test runner that would work properly.  I would also say I had trouble figuring out how
#Large lists could sort correclty.  FOr some reason my code would struggle sorting large lists. After figuring out some indentation issues, I found th ebug that was causing the problem 
# 5. How long did it take for you to complete the assignment?
#      3 Hours


def main():
        #Uncomment this function to test program
        test_cases_runner()

        array = read_array()
        src = sort(array)
        show_result(src)

def test_cases_runner():
        """ This function is a test runner.  It will test the sorting program to make sure it sorts various lists properly."""

        assert sort([3,2,1]) == [1,2,3]
        print('Test 1 Successful')

        assert sort([2,1]) == [1,2]
        print('Test 2 Successful')

        assert sort(['dog','apple','cat','bacon','turkey','zebra']) == ['apple', 'bacon', 'cat', 'dog', 'turkey', 'zebra']
        print('Test 3 Successful')

        assert sort([2,3,4,1,6,10,7,20,22,8]) == [1, 2, 3, 4, 6, 7, 8, 10, 20, 22]
        print('Test 4 Successful')

        assert sort([]) == []
        print('Test 5 Successful')

        assert sort([3.0,2.0,.01]) == [.01,2.0,3.0]
        print('Test 6 Successful')


def read_array():
        """Thisfunction will read a file if the user enters an array."""
        accepted_file = False
        while not accepted_file:
                filename = input('Choose a file that contains an array you would like to sort:\n')
                try:
                        with open(filename, 'r') as file:
                                return json.load(file)['array']
                except:
                        print(f'File error.  Please try again. {filename} is not a valid file.')
                        accepted_file = False

def combine(source, destination, begin1, begin2, end2):
        """This Function will combine the source list into the destination list """
        end1 = begin2
        for i in range(begin1,end2):
                if begin1 < end1 and (begin2 == end2 or source[begin1] < source[begin2]):
                        destination[i] = source[begin1]
                        begin1 += 1
                else:
                        destination[i] = source[begin2] #E
                        begin2 += 1
        return destination

def sort(array):
        """This function will begin sorting the array.  It will determine the begin and end end points for each peice of the sub arrays """
        size = len(array)
        src = array
        des = [0] * len(array)
        num = 2
        while num > 1: 
                num = 0     
                begin1 = 0
                while begin1 < size: 
                        end1 = begin1 + 1
                        while end1 < size and src[end1  - 1]  <= src[end1]:
                                end1 += 1
                        begin2 = end1
                        if begin2 < size:
                                end2 = begin2 + 1
                        else:
                                end2 = begin2
                        while end2 < size and src[end2  - 1]  <= src[end2]:
                                end2 += 1

                        num += 1
                        combine(src, des, begin1, begin2, end2)
                        begin1 = end2
                src, des = des, src
        return src

def show_result(array):
        print(f'Your sorted Array:\n {array}')

main()