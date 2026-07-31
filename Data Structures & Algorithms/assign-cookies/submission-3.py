class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        s_ptr = 0
        g_ptr = 0
        content = 0
        while s_ptr < len(s) and g_ptr < len(g):
            if(g[g_ptr] <= s[s_ptr]):
                content += 1
                g_ptr += 1
            s_ptr += 1

        return content