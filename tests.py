# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()
# class Loh:
#     def __init__(self, name):
#         self.name = name
#         print('hi im ', self.name)
#     def rem(self):
#         del self
#         print('me deleted')
# mas = [[Loh('vasya'),Loh('vasya')],[]]
# print(len(mas[0]))
# print(mas[0])
# print(len(mas[0]))

for i in range(0,5):
    try:
        for j in range(0,5):
            print(j)
            if j == 4:
                raise(0)
    except:
        pass
