import numpy

def pi_estimate(iterations,i,n,S):

    if i > iterations-1:
        print("Done")

    else:
        s_2 = S/2
        a = numpy.sqrt(1-numpy.square(s_2))
        b = 1-a
        new_S = numpy.sqrt(numpy.square(b)+numpy.square(s_2))
        P = S*n
        P_D = P/2
        print(P_D)
        pi_estimate(iterations, i+1, n*2, new_S)