import BondGraphTools as bgt
import modularBondGraph as mbg
import sympy as sp

def model():
    """ Acausal bond graph ProtonPump_abg.py
    Created by svgBondGraph at Thu Dec 17 09:32:53 2020 from ProtonPump_abg.svg

    Usage:
    import ProtonPump_abg; model = ProtonPump_abg.model()
    """

    model = bgt.new(name="ProtonPump")

    ## Junction 0:BGT1
    BGT1 = bgt.new('0')
    model.add(BGT1)

    ## Junction 0:BGT2
    BGT2 = bgt.new('0')
    model.add(BGT2)

    ## Junction 0:BGT4
    BGT4 = bgt.new('0')
    model.add(BGT4)

    ## Junction 0:BGT5
    BGT5 = bgt.new('0')
    model.add(BGT5)

    ## Junction 0:BGT6
    BGT6 = bgt.new('0')
    model.add(BGT6)

    ## Junction 0:BGT7
    BGT7 = bgt.new('0')
    model.add(BGT7)

    ## Junction 1:BGT0
    BGT0 = bgt.new('1')
    model.add(BGT0)

    ## Junction 1:BGT3
    BGT3 = bgt.new('1')
    model.add(BGT3)

    ## Component C:E1
    E1 =  sp.symbols('E1')
    E1 = bgt.new('C',name='E1',value={'C':E1})
    model.add(E1)

    ## Component C:E2
    E2 =  sp.symbols('E2')
    E2 = bgt.new('C',name='E2',value={'C':E2})
    model.add(E2)

    ## Component C:Ee
    Ee =  sp.symbols('Ee')
    Ee = bgt.new('C',name='Ee',value={'C':Ee})
    model.add(Ee)

    ## Component C:Ei
    Ei =  sp.symbols('Ei')
    Ei = bgt.new('C',name='Ei',value={'C':Ei})
    model.add(Ei)

    ## Component C:He
    He =  sp.symbols('He')
    He = bgt.new('C',name='He',value={'C':He})
    model.add(He)

    ## Component C:Hi
    Hi =  sp.symbols('Hi')
    Hi = bgt.new('C',name='Hi',value={'C':Hi})
    model.add(Hi)

    ## Component Re:rp
    kappa_rp =  sp.symbols('kappa_rp')
    RT = sp.symbols('RT')
    rp = bgt.new('Re',name='rp',value={'r':kappa_rp,'R':RT,'T':1},library='BioChem')
    model.add(rp)

    ## Bonds
    bgt.connect((rp,1),BGT0)
    bgt.connect(BGT1,He)
    bgt.connect(BGT4,BGT3)
    bgt.connect(BGT4,Hi)
    bgt.connect(BGT0,BGT1)
    bgt.connect(BGT5,Ei)
    bgt.connect(BGT2,Ee)
    bgt.connect(BGT5,BGT3)
    bgt.connect(BGT0,BGT2)
    bgt.connect(BGT0,BGT1)
    bgt.connect(BGT0,BGT2)
    bgt.connect(BGT5,BGT3)
    bgt.connect(BGT4,BGT3)
    bgt.connect(BGT3,(rp,0))
    bgt.connect(BGT6,BGT3)
    bgt.connect(BGT0,BGT7)
    bgt.connect(BGT6,E1)
    bgt.connect(BGT7,E2)

    return model
