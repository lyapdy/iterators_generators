class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_iterator = iter(self.list_of_list)
        self.list_ = []
        self.cur = -1
        return self

    def __next__(self):
        self.cur += 1
        if len(self.list_) == self.cur:
            self.list_ = None
            self.cur = 0
            if self.list_ is None:
                self.list_ = next(self.list_iterator)
        return self.list_[self.cur]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    print(list(FlatIterator(list_of_lists_1)))


if __name__ == '__main__':
    test_1()