class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            i = 0
            j = 0
          
            lenght = len(numbers)-1
            for i, num in enumerate(numbers):

                print(i, num, j, 'x')
                j = i+1

                while j <= lenght:
                    print(num, numbers[j], num + numbers[j], 'y')
                    if num + numbers[j] == target:
                        return [i+1, j+1]

                    else:
                        j = j+1