from square import square
import numpy as np

'''Modulo di test
'''

def test_square():
    '''Testa la funzione square del file square
    '''
    assert square(3) == 9
    assert square(2.) == 4.
    assert square(-2.) == 4.
    assert square(0.) == 0.
    assert square(2) == 4
    assert square(-2) == 4
    assert square(0) == 0
    assert np.allclose(square(np.ones(100)), np.ones(100))
    print('yeee')
