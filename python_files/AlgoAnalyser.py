# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 16:40:28 2018

@author: 13383861
"""

from sklearn import linear_model
from math import factorial, log, floor
from scipy.optimize import basinhopping
from scipy.stats import pearsonr
import numpy as np
import itertools


#%%
#helper decorator for docstrings
def docstring_parameter(*sub):
     def dec(obj):
         obj.__doc__ = obj.__doc__.format(*sub)
         return obj
     return dec

class AlgoProfiler:
    '''A class which analyses the runtime of an algorithm given the algorithm and its data type'''
    
    class PossibleAlgos:
        def __init__(self):
            def log_(x):
                '''log_e_(x)'''
                return log(x, 2)
            def factorial_(x):
                '''factorial(x)'''
                return factorial(x)
            expected_algos_log = [log_]
            expected_algos_factorial = [factorial]
            expected_algos_exponential = []
            expected_algos_poly = []
            expected_algos_combination = []
            
            max_power = 8
            #generate exponential and polynomial algos - x**power and base**x
            for power in range(1,max_power):
                #doesn't work: i is bound to the closure of all of these functions. z = lambda x=x: x**i
                @docstring_parameter(power)
                def polynomial(x,power=power):
                    '''x**{0}'''
                    return x**power
                expected_algos_poly.append(polynomial)
                if (power == 1):
                    continue
                else:
                    @docstring_parameter(power)
                    def exponential(x,power=power):
                        '''{0}**x'''
                        return power**x                    
                    expected_algos_exponential.append(exponential)
            
            assert expected_algos_poly[2](3) == 3**3
            assert expected_algos_poly[4](2) == 2**5
            assert expected_algos_exponential[3](3) == 5**3
            assert expected_algos_exponential[5](4) == 7**4
            assert expected_algos_log[0](4) == log(4,2)
            assert expected_algos_factorial[0](12) == factorial(12)
            
            for l, poly in list(itertools.product(expected_algos_log, expected_algos_poly)):
                @docstring_parameter(l.__doc__ + ' * ' + poly.__doc__)
                def comb(x,l = l, poly = poly):
                    '''{}'''
                    return l(x) * poly(x)
                expected_algos_combination.append(comb)
            
            for exp, poly in itertools.product(expected_algos_exponential, expected_algos_poly):
                @docstring_parameter(exp.__doc__ + ' * ' + poly.__doc__)
                def comb(x,exp = exp, poly = poly):
                    '''{}'''
                    return exp(x) * poly(x)
                expected_algos_combination.append(comb)    
            
            for exp, l in itertools.product(expected_algos_exponential, expected_algos_log):
                @docstring_parameter(exp.__doc__ + ' * ' + 'log(x)')
                def comb(x,l = l, exp = exp):
                    '''{}'''
                    return l(x) * exp(x)
                expected_algos_combination.append(comb)
            
            common_runtimes = expected_algos_log + expected_algos_factorial + expected_algos_exponential + expected_algos_poly + expected_algos_combination 
            #should be 98
            #print(len(common_runtimes))
            #print((2*(max_power-1)) + 2*(max_power - 2) + ((max_power-1) * (max_power - 2)) + 2)
            assert len(common_runtimes) == (2*(max_power-1)) + 2*(max_power - 2) + ((max_power-1) * (max_power - 2)) + 2
            [runtime(40) for runtime in common_runtimes]
            
            #only expose these to the outer class
            #sort in order of smallest time to biggest time
            self.common_runtimes = sorted(common_runtimes, key = lambda x: x(50))
            self.common_runtimes__vals = {runtime: runtime(50) for runtime in common_runtimes}
            
    def __init__(self):
        self.possible_algos = self.PossibleAlgos()
        
    def _sim_annealing_algo(self, ):
        pass
        
    def analyse_gradient_desc(self, input_sizes, output_times):
        pass
        
    def analyse_brute(self, input_sizes , output_times):
        '''Returns the most likely runtime functions given input sizes and corresponding output times'''
        reg = linear_model.LinearRegression(fit_intercept = False)
        r2_scores = []
        #currently efficient to search through all
        for runtime in self.possible_algos.common_runtimes:
            try:
                y_pred = [runtime(inp) for inp in input_sizes]
            except OverflowError:
                #give a default time
                y_pred = [1 for inp in input_sizes]
            
            #reg.coef_
            #print(reg.score(np.array([[i] for i in y]),y_pred))
            #r2_scores.append(reg.score(np.array([[i] for i in y]),y_pred))
            #r2_scores.append(r2_score(y_pred, output_times))
#            print(list(zip(y_pred, output_times)))
            try:
                reg.fit(np.array([[i] for i in output_times]), np.array(y_pred))
                #print(reg.coef_)
                #print(reg.intercept_)
                r2_scores.append(pearsonr([y_pred_val * reg.coef_[0] for y_pred_val in y_pred], output_times)[0])
            except OverflowError:
                r2_scores.append(0)
            #print(pearsonr(y_pred, output_times))
        #print('r2_scores: ', r2_scores)
        r2_scores = [0 if np.isnan(score) else score for score in r2_scores]
        #print('Identified possible runtime bound: ', self.possible_algos.common_runtimes[r2_scores.index(max(r2_scores))].__doc__)
        return self.possible_algos.common_runtimes[r2_scores.index(max(r2_scores))]
        
    def analyse_sim_annealing(self, input_sizes, output_times):
        #def opt_func(runtime_func_index):
        #    pearson_val = pearsonr(output_times, [self.possible_algos.common_runtimes[int(runtime_func_index)](inp) for inp in input_sizes])[0]
        #    if np.isnan(pearson_val):
        #        return 0
        #    else:
        #        return pearson_val
        upperbound = len(self.possible_algos.common_runtimes)
        class MyTakeStep(object):
            def __init__(self, stepsize=0.5):
                self.stepsize = stepsize
                self.lowerbound = 0
                self.upperbound = upperbound
            def __call__(self, x):
                #s = self.stepsize
                #print('x before: ', x)
                proposed_step = np.random.uniform(-x, self.upperbound - x) * 0.5
                x += proposed_step
                #print('proposed step: ', proposed_step)
                #print('x after: ', x)
                return x
        def opt_func(runtime_index_func):
            try:
                pearson_r_val = pearsonr(output_times, [self.possible_algos.common_runtimes[floor(runtime_index_func)](inp) for inp in input_sizes])[0]
                if np.isnan(pearson_r_val):
                    return 0
                else:
                    return -pearson_r_val
            except OverflowError:
                return 0
        #opt_func = lambda runtime_func_index: 0.000000000000000001 if np.isnan(pearsonr(output_times, [self.possible_algos.common_runtimes[floor(runtime_func_index)](inp) for inp in input_sizes])[0]) else -pearsonr(output_times, [self.possible_algos.common_runtimes[floor(runtime_func_index)](inp) for inp in input_sizes])[0]
        #print(opt_func(10))
        x0 = [len(self.possible_algos.common_runtimes)/2]
        #accept_test = lambda soln: True if abs(1-soln) <= 0.01 else False
        my_step = MyTakeStep()
        return self.possible_algos.common_runtimes[int(basinhopping(func=opt_func, x0=x0, niter = 5000, take_step = my_step).x)]
        
        
        
        
def main():
    import random
    inputs = [i for i in range(1,200)]
    runtimes_x2 = [(inp + (random.random() * inp))**2 for inp in inputs]
    runtimes_x7 = [(inp + (random.random() * inp))**7 for inp in inputs]
    runtimes_3x = [3**(inp + (random.random())) for inp in inputs]
    print('brute force found: ',AlgoProfiler().analyse_brute(inputs, runtimes_x2).__doc__, 'should be x**2')
    print('brute force found: ',AlgoProfiler().analyse_brute(inputs, runtimes_x7).__doc__, 'should be x**7')
    print('brute force found: ',AlgoProfiler().analyse_brute(inputs, runtimes_3x).__doc__, 'should be 3**x')
    #should be 45
    print('Simulated annealing found: ', AlgoProfiler().analyse_sim_annealing(inputs, runtimes_3x).__doc__, 'should be 3**x')
    print(AlgoProfiler().analyse_sim_annealing(inputs, runtimes_3x))
    print('Simulated annealing found: ', AlgoProfiler().analyse_sim_annealing(inputs, runtimes_x7).__doc__, 'should be x**7') 
    
        
if __name__ == '__main__':
    main()        
        
        
        
        
        
        
        
    