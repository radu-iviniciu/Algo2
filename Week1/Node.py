
class Node(object):
    def __init__(self, value, leader):
        self.value = value
        self.leader = leader
            
    # override less operator so that heapify will break ties comparing these in a random way
    # radom = take first operator (less always TRUE)
    # WARNING : do not call < on these in other circumstances 
    def __lt__(self, x):
        return True        

    def __str__(self):
        return str(self.leader) + ": " + self.value
    	
    def __unicode__(self):
        return self.__str__()
    def __repr__(self):
        return self.__str__()