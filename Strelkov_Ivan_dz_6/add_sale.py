# python add_sale.py 5978,5
import task_6_7

if __name__ == '__main__':

    import sys

    if len(sys.argv) > 1:
        error_str = task_6_7.add_record(sys.argv[1])
        if error_str:
            print(error_str)
    else:
        print('Sale amount not specified!')