# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('StartUs')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    def test_merge_pairs1(self):
        ans1 = {1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: None}
        ans2 = {1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: 16}
        merger = CreateDictionary()
        lis1 = merger.merge_pairs1([1, 2, 3, 4, 5, 6, 7], [10, 11, 12, 13, 14, 15])
        lis2 = merger.merge_pairs1([1, 2, 3, 4, 5, 6, 7], [10, 11, 12, 13, 14, 15, 16, 17, 18])
        self.assertEqual(ans1, lis1)
        self.assertEqual(ans2, lis2)



    def test_merge_pairs2(self):
        ans1 = {1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: None}
        ans2 = {1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: 16}
        merger = CreateDictionary()
        lis1 = merger.merge_pairs2([1, 2, 3, 4, 5, 6, 7], [10, 11, 12, 13, 14, 15])
        lis2 = merger.merge_pairs2([1, 2, 3, 4, 5, 6, 7], [10, 11, 12, 13, 14, 15, 16, 17, 18])
        self.assertEqual(ans1, lis1)
        self.assertEqual(ans2, lis2)

    def test_merge_pairs3(self):
        ans1 = {1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: None}
        ans2 = {1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: 16}
        merger = CreateDictionary()
        lis1 = merger.merge_pairs3([1, 2, 3, 4, 5, 6, 7], [10, 11, 12, 13, 14, 15])
        lis2 = merger.merge_pairs3([1, 2, 3, 4, 5, 6, 7], [10, 11, 12, 13, 14, 15, 16, 17, 18])
        self.assertEqual(ans1, lis1)
        self.assertEqual(ans2, lis2)

    def test_read_logs(self):
        accesslog = ReadLogs('./access.log')
        top = accesslog.top_logs(10)
        ans = ['24.236.252.67', '123.125.71.35', '50.150.204.184', '200.49.190.100', '87.169.99.232', '121.107.188.202', '174.37.205.76', '24.233.162.179', '123.125.71.117', '220.181.108.153']

        self.assertEqual(top, ans)