# Given a string, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        temp_length = 0 
        s_list = []
        for val in s: 
            if val in s_list:
                # value is a repeated character and we cut off string from that character
                if longest_length < temp_length: 
                    longest_length = temp_length
                # reset the list and temp_length appropriately
                newindex = s_list.index(val)+1
                s_list = s_list[newindex:]
                temp_length -= newindex 
            
            s_list.append(val)
            temp_length += 1

        if longest_length < temp_length: 
            longest_length = temp_length 
        return longest_length 