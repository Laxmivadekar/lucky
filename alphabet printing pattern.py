for row in range(5):
    for col in range(5):
        if row==0:
            print('*',end='')
        elif (row in{1})and(col in{3}):
            print('*',end='')
        elif (row in{2})and(col in{2}):
            print('*',end='')
        elif (row in{3})and(col in{1}):
            print('*',end='')
        elif row==4:
            print('*',end='')
        else:
            print('',end='')