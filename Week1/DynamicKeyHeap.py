import heapq
import math

class DynamicKeyHeap(object):
    """
    Key,Value pair heap

    Pass in a KeyLambda and initial data list and it will heapify by the key lambda in Key,Value pairs

    Also supports updating the KeyFunciton with alternateKeys resulting in the min of them all
    """
    def __init__(self, initial=None, keyFunc=lambda x:x):
        self.keyFunc = keyFunc
        if initial:
            self._data = [(keyFunc(item), item) for item in initial]
            heapq.heapify(self._data)

        else:
            self._data = []

    def pop_kvp(self):        
        return heapq.heappop(self._data)  

    def pop_value(self):        
        return heapq.heappop(self._data)[1]           
       
    def update_data(self, alternateKeyFunc = lambda x:x):
        """
        Updates each Heap key with the min of the </self.key/> and the </alternateKey/>
        and rebalances the Heap
        """
        self._data = [(min(x[0], alternateKeyFunc(x[1])), x[1]) for x in self._data]
        heapq.heapify(self._data)
        
        # Updating keyFunc so that it is still up to date. This should make calling push still correct
        # TODO: Investigate if keeping track of so many lamdas is a performance hit ?!?!?!?!?
        # NOTE: Push was not used or tested
        self.keyFunc = lambda x : min(alternateKeyFunc(x), self.keyFunc(x))                
