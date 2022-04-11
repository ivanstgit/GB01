# python show_sales.py 1 3
# python show_sales.py 1
# python show_sales.py
import task_6_7

if __name__ == '__main__':

    import sys

    start = 1
    end = 0

    if len(sys.argv) > 1:
        params = {index: value for index, value in zip(range(len(sys.argv) - 1), sys.argv[1:])}
        if params.get(0):
            start = int(params[0])
        if params.get(1):
            end = int(params[1])

    sales_list = task_6_7.get_records(start, end)
    if not sales_list:
        print('Nothing found')
    else:
        for sale in sales_list:
            print(sale)
