# O(N)
import unittest


def unique(string):
    char_set_size = 128
    if len(string) > char_set_size:
        return False

    found_chars = [False for _ in range(char_set_size)]

    for char in string:
        idx = ord(char)
        if found_chars[idx]:
            return False
        
        found_chars[idx] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
