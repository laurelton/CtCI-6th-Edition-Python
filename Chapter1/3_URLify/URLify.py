# O(N)
import unittest


def urlify(string, length):
    char_list = list(string)
    idx = len(char_list) - 1
    s_idx = length - 1

    while idx >= 0:
        if string[s_idx] != ' ':
            char_list[idx] = string[s_idx]
            s_idx -= 1
            idx -= 1
        else:
            char_list[idx] = '0'
            idx -= 1
            char_list[idx] = '2'
            idx -= 1
            char_list[idx] = '%'
            idx -= 1
            s_idx -= 1
            
    return char_list


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
