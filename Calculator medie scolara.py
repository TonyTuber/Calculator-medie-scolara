#                          /$\
#                         /$$$\
#                        /$$$$$\
#                       /$$$$$$$\
#                      /$$$$$$$$$\
#                     /$$$$$$$$$$$\
#                    /$$$$$$$$$$$$$\
#                   /$$$$$$$$$$$$$$$\
#                  /$$$$$$$$$$$$$$$$$\
#                 /$$$$$$$$$$$$$$$$$$$\
#                /$$$$$$$$$$$$$$$$$$$$$\
#               /$$$$ Made by t0sky $$$$\
#              /$$$$$$$$$$$$$$$$$$$$$$$$$\
#             /$$$$$$$$$$$$$$$$$$$$$$$$$$$\
#            /$$$$$$$$*************$$$$$$$$\
#           /$$$$$$$$$*************$$$$$$$$$\
#          /$$$$$$$$$$*************$$$$$$$$$$\
#         /$$$$$$$$$$$*************$$$$$$$$$$$\
#        /$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\
#       /$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\
#      /00000000000000000000000000000000000000000\


note=[9,10]

teza=[10]

#Media notelor

x = sum(note) / len(note)

#Media generala

y = (3*x + teza[0]) / 4

#Cate note sunt la array-ul "teza"

z = len(teza)

if( z == 0 ):
    print(x)

else:
    print(y)

