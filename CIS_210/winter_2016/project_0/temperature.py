'''
Temperature Conversion, Project 0, CIS 210
Authors: Thomas Rowland

Converts celsius temperature to fahrenheit temperature.
'''
def ctemp_to_ftemp_stub(ctemp):
    ''' (float) -> float
    description:
        convert ctemp from celsius to fahrenheit
    returns:
        float
    examples:
        >>> ctemp_to_ftemp(100)
        212.0
        >>> ctemp_to_ftemp(200)
        392.0
        >>> ctemp_to_ftemp(300)
        572.0
    '''
    pass
    return # return the fahrenheit value as a float

def ctemp_to_ftemp(ctemp):
    ''' (float) -> float
    description:
        convert ctemp from celsius to fahrenheit
    returns:
        float
    '''
    ftemp = (ctemp * (9/5)) + 32
    return ftemp # return the fahrenheit value as a float
