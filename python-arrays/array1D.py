import ctypes

# one dimensional array
class Array:
    def __init__(self, size):
        assert size > 0, 'array size must be greater than zero'
        self._size = size
        PyArraytype = ctypes.py_object * size
        self._elements = PyArraytype()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index <= len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index <= len(self)
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

    def __repr__(self):
        output="["
        for element in range(len(self)):
            if element==len(self)-1:
                output+=str(self._elements[element])
            else:
                output+=str(self._elements[element])+" "
           
        output+="] \n"

        return output


class _ArrayIterator():
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration

   
