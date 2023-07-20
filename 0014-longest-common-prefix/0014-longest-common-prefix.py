class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        word_1 = strs[0]

        if(len(strs) > 1):
            
            for i in range(1 , len(word_1) + 1):

                flag = 0

                for word in strs:

                    if(word_1[0:i] == word[0:i]):
                        flag += 1

                if(flag == len(strs)):
                    prefix = word_1[0:i]


        else:
            prefix = word_1

        return prefix