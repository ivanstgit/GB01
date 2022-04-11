# python edit_sale.py 2 6666,5
import task_6_7

if __name__ == '__main__':

    import sys
    pos = 0
    new_value = 'n/a'
    if len(sys.argv) == 1:
        print('position & new value not specified')
    else:
        params = {index: value for index, value in zip(range(len(sys.argv) - 1), sys.argv[1:])}
        if params.get(0):
            pos = int(params[0])
        else:
            print('position not specified')
            exit(2)
        if params.get(1):
            new_value = params[1]
        else:
            print('new value not specified')
            exit(3)

        print(task_6_7.edit_record(pos, new_value))


