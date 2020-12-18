import BondGraphTools as bgt
import modularBondGraph as mbg
import sympy as sp

def model():
    """ Acausal bond graph SGLT_abg.py
    Created by svgBondGraph at Fri Dec 18 12:28:15 2020 from SGLT_abg.svg

    Usage:
    import SGLT_abg; model = SGLT_abg.model()
    """

    model = bgt.new(name="SGLT")

    ## Junction 0:BGT1
    BGT1 = bgt.new('0')
    model.add(BGT1)

    ## Junction 0:BGT14
    BGT14 = bgt.new('0')
    model.add(BGT14)

    ## Junction 0:BGT16
    BGT16 = bgt.new('0')
    model.add(BGT16)

    ## Junction 0:BGT17
    BGT17 = bgt.new('0')
    model.add(BGT17)

    ## Junction 0:BGT18
    BGT18 = bgt.new('0')
    model.add(BGT18)

    ## Junction 0:BGT19
    BGT19 = bgt.new('0')
    model.add(BGT19)

    ## Junction 0:BGT20
    BGT20 = bgt.new('0')
    model.add(BGT20)

    ## Junction 0:BGT4
    BGT4 = bgt.new('0')
    model.add(BGT4)

    ## Junction 0:BGT7
    BGT7 = bgt.new('0')
    model.add(BGT7)

    ## Junction 0:BGT8
    BGT8 = bgt.new('0')
    model.add(BGT8)

    ## Junction 1:BGT0
    BGT0 = bgt.new('1')
    model.add(BGT0)

    ## Junction 1:BGT10
    BGT10 = bgt.new('1')
    model.add(BGT10)

    ## Junction 1:BGT11
    BGT11 = bgt.new('1')
    model.add(BGT11)

    ## Junction 1:BGT12
    BGT12 = bgt.new('1')
    model.add(BGT12)

    ## Junction 1:BGT13
    BGT13 = bgt.new('1')
    model.add(BGT13)

    ## Junction 1:BGT15
    BGT15 = bgt.new('1')
    model.add(BGT15)

    ## Junction 1:BGT2
    BGT2 = bgt.new('1')
    model.add(BGT2)

    ## Junction 1:BGT21
    BGT21 = bgt.new('1')
    model.add(BGT21)

    ## Junction 1:BGT3
    BGT3 = bgt.new('1')
    model.add(BGT3)

    ## Junction 1:BGT5
    BGT5 = bgt.new('1')
    model.add(BGT5)

    ## Junction 1:BGT6
    BGT6 = bgt.new('1')
    model.add(BGT6)

    ## Junction 1:BGT9
    BGT9 = bgt.new('1')
    model.add(BGT9)

    ## Component C:CNai
    CNai =  sp.symbols('CNai')
    CNai = bgt.new('C',name='CNai',value={'C':CNai})
    model.add(CNai)

    ## Component C:CNao
    CNao =  sp.symbols('CNao')
    CNao = bgt.new('C',name='CNao',value={'C':CNao})
    model.add(CNao)

    ## Component C:Ci
    Ci =  sp.symbols('Ci')
    Ci = bgt.new('C',name='Ci',value={'C':Ci})
    model.add(Ci)

    ## Component C:Co
    Co =  sp.symbols('Co')
    Co = bgt.new('C',name='Co',value={'C':Co})
    model.add(Co)

    ## Component C:Nai
    Nai =  sp.symbols('Nai')
    Nai = bgt.new('C',name='Nai',value={'C':Nai})
    model.add(Nai)

    ## Component C:Nao
    Nao =  sp.symbols('Nao')
    Nao = bgt.new('C',name='Nao',value={'C':Nao})
    model.add(Nao)

    ## Component C:SCNai
    SCNai =  sp.symbols('SCNai')
    SCNai = bgt.new('C',name='SCNai',value={'C':SCNai})
    model.add(SCNai)

    ## Component C:SCNao
    SCNao =  sp.symbols('SCNao')
    SCNao = bgt.new('C',name='SCNao',value={'C':SCNao})
    model.add(SCNao)

    ## Component C:Si
    Si =  sp.symbols('Si')
    Si = bgt.new('C',name='Si',value={'C':Si})
    model.add(Si)

    ## Component C:So
    So =  sp.symbols('So')
    So = bgt.new('C',name='So',value={'C':So})
    model.add(So)

    ## Component Re:r12
    kappa_r12 =  sp.symbols('kappa_r12')
    RT = sp.symbols('RT')
    r12 = bgt.new('Re',name='r12',value={'r':kappa_r12,'R':RT,'T':1},library='BioChem')
    model.add(r12)

    ## Component Re:r23
    kappa_r23 =  sp.symbols('kappa_r23')
    RT = sp.symbols('RT')
    r23 = bgt.new('Re',name='r23',value={'r':kappa_r23,'R':RT,'T':1},library='BioChem')
    model.add(r23)

    ## Component Re:r25
    kappa_r25 =  sp.symbols('kappa_r25')
    RT = sp.symbols('RT')
    r25 = bgt.new('Re',name='r25',value={'r':kappa_r25,'R':RT,'T':1},library='BioChem')
    model.add(r25)

    ## Component Re:r34
    kappa_r34 =  sp.symbols('kappa_r34')
    RT = sp.symbols('RT')
    r34 = bgt.new('Re',name='r34',value={'r':kappa_r34,'R':RT,'T':1},library='BioChem')
    model.add(r34)

    ## Component Re:r45
    kappa_r45 =  sp.symbols('kappa_r45')
    RT = sp.symbols('RT')
    r45 = bgt.new('Re',name='r45',value={'r':kappa_r45,'R':RT,'T':1},library='BioChem')
    model.add(r45)

    ## Component Re:r56
    kappa_r56 =  sp.symbols('kappa_r56')
    RT = sp.symbols('RT')
    r56 = bgt.new('Re',name='r56',value={'r':kappa_r56,'R':RT,'T':1},library='BioChem')
    model.add(r56)

    ## Component Re:r61
    kappa_r61 =  sp.symbols('kappa_r61')
    RT = sp.symbols('RT')
    r61 = bgt.new('Re',name='r61',value={'r':kappa_r61,'R':RT,'T':1},library='BioChem')
    model.add(r61)

    ## Bonds
    bgt.connect(BGT0,(r61,0))
    bgt.connect(BGT1,BGT0)
    bgt.connect(BGT6,(r56,0))
    bgt.connect((r56,1),BGT2)
    bgt.connect(BGT2,BGT1)
    bgt.connect(BGT1,Ci)
    bgt.connect((r61,1),BGT3)
    bgt.connect(BGT3,BGT4)
    bgt.connect(BGT4,BGT21)
    bgt.connect(BGT21,(r12,0))
    bgt.connect((r12,1),BGT5)
    bgt.connect(BGT4,Co)
    bgt.connect(BGT5,BGT14)
    bgt.connect(BGT8,BGT6)
    bgt.connect((r25,1),BGT10)
    bgt.connect((r34,1),BGT11)
    bgt.connect(BGT7,(r45,0))
    bgt.connect((r45,1),BGT9)
    bgt.connect(BGT9,BGT8)
    bgt.connect(BGT10,BGT8)
    bgt.connect(BGT9,BGT19)
    bgt.connect(BGT7,SCNai)
    bgt.connect(BGT8,CNai)
    bgt.connect(BGT11,BGT7)
    bgt.connect(BGT12,(r25,0))
    bgt.connect(BGT13,(r34,0))
    bgt.connect(BGT15,(r23,0))
    bgt.connect((r23,1),BGT16)
    bgt.connect(BGT18,BGT15)
    bgt.connect(BGT14,BGT15)
    bgt.connect(BGT14,BGT12)
    bgt.connect(BGT14,CNao)
    bgt.connect(BGT16,SCNao)
    bgt.connect(BGT16,BGT13)
    bgt.connect(BGT17,Nao)
    bgt.connect(BGT18,So)
    bgt.connect(BGT19,Si)
    bgt.connect(BGT20,Nai)
    bgt.connect(BGT2,BGT20)
    bgt.connect(BGT2,BGT20)
    bgt.connect(BGT17,BGT21)
    bgt.connect(BGT17,BGT21)

    return model
