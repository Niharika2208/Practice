class DoublyLinkedNode:
    def __init__(
            self,
            item: int = None,
            prev: "DoublyLinkedNode | None" = None,
            next: "DoublyLinkedNode | None" = None
    ) -> None:
        self._item = item
        self._prev = prev
        self._next = next

    # TODO: Implement the needed methods
    def set_next(self, _tail):
        pass


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head = DoublyLinkedNode()
        self._tail = DoublyLinkedNode(prev=self._head)
        # self._head.set_next(self._tail)
        self._size = 0

    def add_first(self, item: int) -> None:
        NewNode = DoublyLinkedNode(item)
        NewNode.next = self._head

        if self._head is not None:
            self._head._prev = NewNode
        self._head = NewNode


if __name__ == "__main__":
    A1 = DoublyLinkedList()
    A1.add_first(9)
    print(A1.head._item)
    A1.add_first(8)
    print(A1._head.next._item)
    A1.add_first(5)
    print(A1._head._next._next.item)
