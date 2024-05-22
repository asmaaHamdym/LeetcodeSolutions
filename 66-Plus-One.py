class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=''
        list=[]
        for i in digits:
            number+=str(i)
        number=int(number)+1
        for i in str(number):
            list.append(int(i))
        return list