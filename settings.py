''' User Settings '''

''' Other example functions: 
-0.1*x**2 + 4*x + 7
-0.25*x**2 + 5*x + 6
'''

# FUNCTION = lambda x: -0.4*x**2 + 4*x + 6
FUNCTION = lambda x: -0.1*x**2 + 4*x + 7

X_START = -1

X_END = 41
##X_END = 21

MAX_HIST_SIZE = 20
''' end of user settings '''


############################################################
############################################################
''' development settings '''
f = FUNCTION
MUTATION_TYPE = 'NEGATION'
OFFSET = -X_START
m = min([f(x) for x in range(X_START, X_END+1)])
FUNCTION_OFFSET = abs(m)if m < 0 else 0
''' end '''
