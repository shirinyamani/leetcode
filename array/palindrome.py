class Solution:
    def getallsub(self,s):
        return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

    def palindrome(self,s):
        return all(a==b for a,b in zip(s, reversed(s)))

    def longestpalindrome(self, s):
        palis = list(filter(lambda x: self.palindrome(x), self.getallsub(s)))
        return max(palis, key=lambda pali: len(pali))


if __name__ == '__main__':
    s = Solution()
    print(s.longestpalindrome("babad"))
