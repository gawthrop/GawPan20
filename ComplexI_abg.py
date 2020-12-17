import BondGraphTools as bgt
import modularBondGraph as mbg
import sympy as sp

def model():
    """ Acausal bond graph ComplexI_abg.py
    Created by svgBondGraph at Thu Dec 17 09:32:54 2020 from ComplexI_abg.svg

    Usage:
    import ComplexI_abg; model = ComplexI_abg.model()
    """

    model = bgt.new(name="ComplexI")

    ## Junction 0:BGT0
    BGT0 = bgt.new('0')
    model.add(BGT0)

    ## Junction 0:BGT1
    BGT1 = bgt.new('0')
    model.add(BGT1)

    ## Component C:E1
    E1 =  sp.symbols('E1')
    E1 = bgt.new('C',name='E1',value={'C':E1})
    model.add(E1)

    ## Component C:E2
    E2 =  sp.symbols('E2')
    E2 = bgt.new('C',name='E2',value={'C':E2})
    model.add(E2)

    ## Subsystem ProtonPump:pp
    import ProtonPump_abg
    pp = ProtonPump_abg.model()
    pp.name = 'pp'
    model.add(pp)
    bgt.expose(pp / 'E1','E1')
    bgt.expose(pp / 'E2','E2')
    mbg.renameSub(pp,portList=['E1', 'E2'])

    ## Subsystem Redox:rr
    import Redox_abg
    rr = Redox_abg.model()
    rr.name = 'rr'
    model.add(rr)
    bgt.expose(rr / 'E1','E1')
    bgt.expose(rr / 'E2','E2')
    mbg.renameSub(rr,portList=['E1', 'E2'])

    ## Bonds
    bgt.connect(BGT0,E2)
    bgt.connect(BGT0,(rr,'E2'))
    bgt.connect((pp,'E2'),BGT0)
    bgt.connect((rr,'E1'),BGT1)
    bgt.connect(BGT1,(pp,'E1'))
    bgt.connect(BGT1,E1)

    return model
