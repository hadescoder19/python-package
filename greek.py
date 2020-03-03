class greek:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['zeus', 'poseidon', 'hades']
 
 
    def printMembers(self):
        print('printing the big three greek gods')
        for member in self.members:
            print('\t%s ' % member)