# O(N)
import unittest


def urlify(string, length):
    reader = length - 1
    writer = len(string) - 1

    while reader >= 0:
        if string[reader] != ' ':
            string[writer] = string[reader]
            writer -= 1
            reader -= 1
        else:
            string[writer] = '0'
            writer -= 1
            string[writer] = '2'
            writer -= 1
            string[writer] = '%'
            writer -= 1

            reader -= 1

    return string


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
