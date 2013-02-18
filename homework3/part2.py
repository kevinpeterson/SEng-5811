'''
Predicate:     ((a + b) < c and not p) or (r > s)
Constraints:    t1: > F = 
                t2: = F < 
                t3: < T = 
                t4: < F = 
                t5: > F >
'''

#Correctly implemented predicate
def correct_predicate(a,b,c,p,r,s): 
    '((a + b) < c and not p) or (r > s)'
    return ((a + b) < c and not p) or (r > s)

def bad_predicate1(a,b,c,p,r,s): 
    '((a + b) < c and not p) or (r > s)'
    return ((a + b) < c or not p) or (r < s)

def bad_predicate2(a,b,c,p,r,s): 
    '((a + b) < c and not p) or (r < s)'
    return ((a + b) < c and not p) or (r < s)

def bad_predicate3(a,b,c,p,r,s): 
    '((a + b) < c and not p) and (r > s)'
    return ((a + b) < c and not p) and (r > s)

def bad_predicate4(a,b,c,p,r,s): 
    '((a + b) < c and p) and (r > s)'
    return ((a + b) < c and p) and (r > s)

def bad_predicate5(a,b,c,p,r,s): 
    '((a - b) > c and p) and (r > s)'
    return ((a - b) > c and p) and (r > s)

test_predicates = [bad_predicate1, bad_predicate2,
                    bad_predicate3, bad_predicate4,
                    bad_predicate5]

# Test Cases for -> ((a + b) < c and not p) or (r > s)
# With Given Constraints
t1 = dict(a=1,b=2,c=1,p=False,r=5,s=5)# t1: > F =
t2 = dict(a=1,b=1,c=2,p=False,r=5,s=4)# t2: = F < 
t3 = dict(a=1,b=1,c=3,p=False,r=5,s=5)# t3: < T = 
t4 = dict(a=1,b=1,c=3,p=True, r=5,s=5)# t4: < F = 
t5 = dict(a=1,b=1,c=1,p=False,r=5,s=4)# t5: > F >

tests = [t1,t2,t3,t4,t5]

def test(test_predicate):
    '''Test a test predicate against the known correct one,
    using test cases for all of the defined constraints'''
    
    print "Correct predicate: %s" % correct_predicate.__doc__
    print "Test predicate:    %s" % test_predicate.__doc__

    for i,test in enumerate(tests, start=1):
        if (not (correct_predicate(**test) == test_predicate(**test))):
            print "  -- Test %i yielded different results" % i  
            
    print 

# Part II (a)
# Test all of the test predicates
for test_predicate in test_predicates:           
    test(test_predicate)


#####################################################################
# Part II (b)
# Test all permutations of the predicate against the test cases (T).
# When there is a case where the test predicate makes only one
# test-case fail, add that test case to set (F). Take `T Difference F` -
# and the result is unnecessary tests.

def test_eval(first,second,third,fourth,fifth,a,b,c,p,r,s):
    return eval("((a %s b) < c %s %s p) %s (r %s s)" % (first, second, third, fourth, fifth))

and_or = ['and', 'or']
not_nothing = ['not', '']
comparisions = ['>', '>=', '<', '<=', '==', '!=']

all_constraints = set((1,2,3,4,5))
necessary_constraints = set()

for first_op in comparisions:
    for second_op in and_or:
        for third_op in not_nothing:
            for fourth_op in and_or:
                for fifth_op in comparisions:
                    failures = set()
                    for i,test in enumerate(tests, start=1):
                        if not (correct_predicate(**test) == test_eval(first_op,second_op,third_op,fourth_op,fifth_op,**test)):
                            failures.add(i)
                            
                    if len(failures) == 1:
                        necessary_constraints.add(failures.pop())

unnecessary_constraints = all_constraints - necessary_constraints    

if(len(unnecessary_constraints) == 0):
    print "No unnecessary constraints."
else:
    print "Unnecessary constraints: " + ",".join(str(s) for s in unnecessary_constraints)
        