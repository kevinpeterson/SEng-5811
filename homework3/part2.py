print '''
##############
Kevin Peterson
SEng 5811 
Homework #3
Part 2
https://github.com/kevinpeterson/SEng-5811/blob/master/homework3/part2.py
##############

'''  
'''
Predicate:     ((a + b) < c and not p) or (r > s)
Constraints:    t1: > F = 
                t2: = F < 
                t3: < T = 
                t4: < F = 
                t5: > F >
'''
constraints = dict(t1='> F =',t2='= F <',t3='< T =',t4='< F =',t5='> F >')


#Correctly implemented predicate
def correct_predicate(a,b,c,p,r,s): 
    '(( a + b ) < c and not p ) or ( r > s )'
    return ((a + b) < c and not p) or (r > s)

def bad_predicate1(a,b,c,p,r,s): 
    '(( a + b ) < c and p ) or ( r > s )'
    return ((a + b) < c and p) or (r > s)

def bad_predicate2(a,b,c,p,r,s): 
    '(( a + b ) < c or not p ) or ( r > s )'
    return ((a + b) < c or not p) or (r > s)

def bad_predicate3(a,b,c,p,r,s): 
    '(( a + b ) < c and not p ) and ( r > s )'
    return ((a + b) < c and not p) and (r > s)

def bad_predicate4(a,b,c,p,r,s): 
    '(( a + b ) > c and not p ) or ( r < s ) '
    return ((a + b) > c and not p) or (r < s)

def bad_predicate5(a,b,c,p,r,s): 
    '(( a + b ) > c and p ) and ( r > s )'
    return ((a + b) > c and p) and (r > s)

test_predicates = [bad_predicate1, bad_predicate2,
                    bad_predicate3, bad_predicate4,
                    bad_predicate5]

# Test Cases for -> ((a + b) < c and not p) or (r > s)
# With Given Constraints
t1 = dict(a=1,b=1,c=1,p=True,r=5,s=5)# t1: > F =
t2 = dict(a=1,b=1,c=2,p=True,r=5,s=4)# t2: = F < 
t3 = dict(a=1,b=1,c=3,p=False,r=5,s=5)# t3: < T = 
t4 = dict(a=1,b=1,c=3,p=True, r=5,s=5)# t4: < F = 
t5 = dict(a=1,b=1,c=1,p=True,r=5,s=4)# t5: > F >

tests = [t1,t2,t3,t4,t5]

def run_test_predicates(test_predicate):
    '''Test a test predicate against the known correct one,
    using test cases for all of the defined constraints'''
    
    print '==========================='
    print 'Testing Incorrect Predicate'    
    print '==========================='
    print "Correct predicate: %s" % correct_predicate.__doc__
    print "Test predicate:    %s" % test_predicate.__doc__
    print "  ================="
    print "  Test Differences:"
    print "  ================="
    for i,test in enumerate(tests, start=1):
        correct_predicate_eval = correct_predicate(**test) 
        test_predicate_eval = test_predicate(**test)
        if (not (correct_predicate_eval == test_predicate_eval)):
            print "  -- Test %i (Constraint: '%s') yielded different results:" % (i, constraints['t'+str(i)])
            print "      * Test values were: " + str(test)
            print "      -- Good Predicate: " + _add_variables_to_predicate(correct_predicate,test) + " == " + str(correct_predicate_eval)
            print "      -- Test Predicate: " + _add_variables_to_predicate(test_predicate,test) + " == " + str(test_predicate_eval)
            
    print 

def _add_variables_to_predicate(predicate,values):
    return reduce(lambda x, y: x.replace(' ' +y+' ', ' '+str(values[y])+' ', 1), values, predicate.__doc__)

# Part II (a)
# Test all of the test predicates
print('(a)')
for test_predicate in test_predicates:           
    run_test_predicates(test_predicate)


#####################################################################
# Part II (b)
# Test all permutations of the predicate against the test cases (T).
# When there is a case where the test predicate makes only one
# test-case fail, add that test case to set (F). Take `T Difference F` -
# and the result is unnecessary tests.
print('(b)')

def test_eval(first,second,third,fourth,fifth,sixth,a,b,c,p,r,s):
    '''Construct and eval a given permutation of the predicate'''
    predicate = "( %s (a + b) %s c %s %s p) %s (r %s s)" % (first, second, third, fourth, fifth, sixth)
    return eval(predicate)

and_or = ['and', 'or']
not_nothing = ['not', '']
comparisions = ['>', '>=', '<', '<=', '==', '!=']

all_constraints = set((1,2,3,4,5))
necessary_constraints = set()

permutations = 0

for first_op in not_nothing:
    for second_op in comparisions:
        for third_op in and_or:
            for fourth_op in not_nothing:
                for fifth_op in and_or:
                    for sixth_op in comparisions:
                        permutations += 1
                        failures = set()
                        for i,test in enumerate(tests, start=1):
                            if not (correct_predicate(**test) == test_eval(first_op,second_op,third_op,fourth_op,fifth_op,sixth_op,**test)):
                                failures.add(i)
                                
                        if len(failures) == 1:
                            necessary_constraints.add(failures.pop())

unnecessary_constraints = all_constraints - necessary_constraints    

if(len(unnecessary_constraints) == 0):
    print "No unnecessary constraints."
else:
    print "Unnecessary constraints: " + ",".join("'"+constraints['t'+str(s)]+"'" for s in unnecessary_constraints)
    print '''Approach:
    Brute force... I took all permutations of ((a + b) < c and not p) or (r > s)
    and tested all %s of them against the set of all test cases T.
    If there was a permutation where the defect was caught by only ONE test, I
    assumed that test was necessary and added that test to set N. Finally, I took
    T difference N, and the result was the set of unnecessary tests.

    I believe to prove a constraint necessary, you need to show that given a test-case,
    it will show defect where all other test cases won't. If a constraint only shows a
    defect when another constraint does as well, then it isn't necessary.

    So either there is an error in my approach, and error in my code, or maybe the above
    listed constraint(s) really aren't necessary for this predicate.''' % permutations



    