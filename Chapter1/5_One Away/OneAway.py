# O(N)
import unittest


def one_away(s1, s2):
    N1 = len(s1)
    N2 = len(s2)
    diffs = 0

    if abs(N1 - N2) > 1:
        return False

    if N1 == N2:
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diffs += 1

        return diffs < 2
    else:
        shorter = s1 if N1 < N2 else s2
        longer  = s1 if N1 > N2 else s2  
        
        s_idx = 0
        l_idx = 0
        
        while s_idx < len(shorter):
            if shorter[s_idx] != longer[l_idx]:
                diffs += 1
                if diffs == 2:
                    return False
                l_idx += 1
            else:
                s_idx += 1
                l_idx += 1

    return True



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pae','pale',True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False),
        ('walk', 'ball', False),
        ('wlk', 'walk', True),
        ('wlk', 'wall', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
