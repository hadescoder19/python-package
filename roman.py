class roman:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['jupiter', 'neptune', 'pluto']
 
 
    def printMembers(self):
        print('Printing the big three roman gods')
        for member in self.members:
           print('\t%s ' % member)