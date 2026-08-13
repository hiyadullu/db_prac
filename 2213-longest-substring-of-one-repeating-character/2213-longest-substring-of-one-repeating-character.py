class SegmentTreeNode:
    __slots__ = ['cl', 'cr', 'lmx', 'rmx', 'mx', 'len']
    def __init__(self):
        self.cl = ''
        self.cr = ''
        self.lmx = 0
        self.rmx = 0
        self.mx = 0
        self.len = 0

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        tree = [SegmentTreeNode() for _ in range(4 * n)]

        def merge(i):
            left, right = 2 * i, 2 * i + 1
            tree[i].cl = tree[left].cl
            tree[i].cr = tree[right].cr
            tree[i].lmx = tree[left].lmx
            tree[i].rmx = tree[right].rmx
            tree[i].mx = max(tree[left].mx, tree[right].mx)

            if tree[left].cr == tree[right].cl:
                tree[i].mx = max(tree[i].mx, tree[left].rmx + tree[right].lmx)
                if tree[left].lmx == tree[left].len:
                    tree[i].lmx = tree[left].len + tree[right].lmx
                if tree[right].rmx == tree[right].len:
                    tree[i].rmx = tree[right].len + tree[left].rmx

        def build(i, l, r):
            tree[i].len = r - l + 1
            if l == r:
                tree[i].cl = tree[i].cr = s[l]
                tree[i].lmx = tree[i].rmx = tree[i].mx = 1
                return
            mid = (l + r) // 2
            build(2 * i, l, mid)
            build(2 * i + 1, mid + 1, r)
            merge(i)

        def update(i, l, r, idx, val):
            if l == r:
                tree[i].cl = tree[i].cr = val
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * i, l, mid, idx, val)
            else:
                update(2 * i + 1, mid + 1, r, idx, val)
            merge(i)

        build(1, 0, n - 1)
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1].mx)
            
        return ans
      