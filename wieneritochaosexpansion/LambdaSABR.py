# -*- coding,  utf-8 -*-
from BaseWienerItoChaosExpansion import USE_SYMENGINE
from BaseWienerItoChaosExpansion import BaseWienerItoChaosExpansion
from StopWatch import StopWatch

if USE_SYMENGINE:
    from symengine import Symbol
else:
    from sympy import Symbol

class LambdaSABR(BaseWienerItoChaosExpansion):
    def __init__(self):
        super().__init__()
        self.model_name = 'Lambda SABR'
        self.v0 = Symbol('alpha', positive=True)
        self.beta = Symbol('beta', positive=True)
        self.nu = Symbol('nu')
        self.r0 = Symbol('r0', positive=True)
        self.lam = Symbol('lambda', position=True)
        self.th = Symbol('theta', positive=True)

    def r(self, t=Symbol('t', positive=True)):
        return 0

    def sigma(self, s=Symbol('s', positive=True),
              v=Symbol('v', positive=True)):
        return v * s ** (self.beta - 1)

    def theta(self, t=Symbol('t', positive=True)):
        return self.lam * self.th

    def kappa(self, t=Symbol('t', positive=True)):
        return self.lam

    def gamma(self, v=Symbol('v', positive=True)):
        return self.nu * v

if __name__  ==  '__main__':
    sw = StopWatch()
    proc = LambdaSABR()
    proc.show_model_spec()
    print(proc.print_in_r(proc.f_Xt(simplify=False)))
    sw.show_elapsed_time()