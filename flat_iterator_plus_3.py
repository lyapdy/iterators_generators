class FlatIterator:
    my_list = []
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.extract_from_the_list(self.list_of_list)
        return self

    def __next__(self):
        if not self.my_list:
            raise StopIteration
        return self.my_list.pop(0)

    def extract_from_the_list(self, initial_list):
        for item in initial_list:
            if isinstance(item, list):
                self.extract_from_the_list(item)
                continue
            else:
                self.my_list.append(item)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    print(list(FlatIterator(list_of_lists_2)))