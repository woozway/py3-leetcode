class MyStack:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.queue = collections.deque()


  def push(self, x: int) -> None:
    """
    Push element x onto stack.
    """
    n = len(self.queue)
    self.queue.append(x)
    for _ in range(n):
      self.queue.append(self.queue.popleft())


  def pop(self) -> int:
    """
    Removes the element on top of the stack and returns that element.
    """
    return self.queue.popleft()


  def top(self) -> int:
    """
    Get the top element.
    """
    return self.queue[0]


  def empty(self) -> bool:
    """
    Returns whether the stack is empty.
    """
    return not self.queue
