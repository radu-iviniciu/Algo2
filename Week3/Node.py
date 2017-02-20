class Node(object):

    def __init__(self, weight, left = None, right = None):
        self._weight = weight
        self._left = left
        self._right = right
        self._code = ''
    
    def append(self, c):
        if(self.is_leaf()):
            self._code = c + self._code
        else:
            self._left.append(c)
            self._right.append(c)

    def is_leaf(self):
        return not self._left and not self._right

    def weight(self):
        return self._weight

    def code(self):
        if self._left or self._right:
            raise Exception('Just leaves have a code')
        return self._code