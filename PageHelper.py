class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.colection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.colection)

    # returns the number of pages
    def page_count(self):
        return len(self.colection) // self.items_per_page + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > self.page_count() - 1:
            return -1
        elif page_index < self.page_count() - 1:
            return self.items_per_page
        else:
            return self.page_count() % self.items_per_page


    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.colection):
            return -1
        return item_index // self.items_per_page


if __name__ == '__main__':
    helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
    print(helper.page_count())  # should == 2
    print(helper.item_count())  # should == 6
    print(helper.page_item_count(0))
    print(helper.page_item_count(1))
    print(helper.page_item_count(2))
    print(helper.page_index(5))  # should == 1 (zero based index)
    print(helper.page_index(2))  # should == 0
    print(helper.page_index(20))  # should == -1
    print(helper.page_index(-10))
