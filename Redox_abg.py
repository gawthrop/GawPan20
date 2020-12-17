import BondGraphTools as bgt
import modularBondGraph as mbg
import sympy as sp

def model():
    """ Acausal bond graph Redox_abg.py
    Created by svgBondGraph at Thu Dec 17 09:32:52 2020 from Redox_abg.svg

    Usage:
    import Redox_abg; model = Redox_abg.model()
    """

    model = bgt.new(name="Redox")

    ## Junction 0:BGT2
    BGT2 = bgt.new('0')
    model.add(BGT2)

    ## Junction 0:BGT3
    BGT3 = bgt.new('0')
    model.add(BGT3)

    ## Junction 0:BGT4
    BGT4 = bgt.new('0')
    model.add(BGT4)

    ## Junction 0:BGT7
    BGT7 = bgt.new('0')
    model.add(BGT7)

    ## Junction 1:BGT0
    BGT0 = bgt.new('1')
    model.add(BGT0)

    ## Junction 1:BGT1
    BGT1 = bgt.new('1')
    model.add(BGT1)

    ## Junction 1:BGT5
    BGT5 = bgt.new('1')
    model.add(BGT5)

    ## Junction 1:BGT6
    BGT6 = bgt.new('1')
    model.add(BGT6)

    ## Component C:E1
    E1 =  sp.symbols('E1')
    E1 = bgt.new('C',name='E1',value={'C':E1})
    model.add(E1)

    ## Component C:E2
    E2 =  sp.symbols('E2')
    E2 = bgt.new('C',name='E2',value={'C':E2})
    model.add(E2)

    ## Component C:H
    H =  sp.symbols('H')
    H = bgt.new('C',name='H',value={'C':H})
    model.add(H)

    ## Component C:NAD
    NAD =  sp.symbols('NAD')
    NAD = bgt.new('C',name='NAD',value={'C':NAD})
    model.add(NAD)

    ## Component C:NADH
    NADH =  sp.symbols('NADH')
    NADH = bgt.new('C',name='NADH',value={'C':NADH})
    model.add(NADH)

    ## Component C:Q
    Q =  sp.symbols('Q')
    Q = bgt.new('C',name='Q',value={'C':Q})
    model.add(Q)

    ## Component C:QH2
    QH2 =  sp.symbols('QH2')
    QH2 = bgt.new('C',name='QH2',value={'C':QH2})
    model.add(QH2)

    ## Component Re:r1
    kappa_r1 =  sp.symbols('kappa_r1')
    RT = sp.symbols('RT')
    r1 = bgt.new('Re',name='r1',value={'r':kappa_r1,'R':RT,'T':1},library='BioChem')
    model.add(r1)

    ## Component Re:r2
    kappa_r2 =  sp.symbols('kappa_r2')
    RT = sp.symbols('RT')
    r2 = bgt.new('Re',name='r2',value={'r':kappa_r2,'R':RT,'T':1},library='BioChem')
    model.add(r2)

    ## Bonds
    bgt.connect((r1,1),BGT1)
    bgt.connect(BGT1,BGT3)
    bgt.connect(NADH,BGT0)
    bgt.connect(BGT0,(r1,0))
    bgt.connect(BGT1,NAD)
    bgt.connect(BGT1,BGT2)
    bgt.connect(BGT1,BGT2)
    bgt.connect(BGT3,H)
    bgt.connect(BGT2,E1)
    bgt.connect(BGT3,BGT7)
    bgt.connect(BGT5,(r2,0))
    bgt.connect((r2,1),BGT6)
    bgt.connect(Q,BGT5)
    bgt.connect(BGT6,QH2)
    bgt.connect(BGT7,BGT5)
    bgt.connect(BGT7,BGT5)
    bgt.connect(BGT4,BGT5)
    bgt.connect(BGT4,BGT5)
    bgt.connect(E2,BGT4)

    return model
