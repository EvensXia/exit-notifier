import argparse


def main():
    parser = argparse.ArgumentParser(description='测试脚本参数传递')
    parser.add_argument('-n', '--number', type=int, help='一个整数参数')
    parser.add_argument('-s', '--string', type=str, help='一个字符串参数')
    parser.add_argument('-l', '--list', nargs='+', help='一个列表参数')
    parser.add_argument('--flag', action='store_true', help='一个布尔标志参数')

    args = parser.parse_args()

    print("收到的参数如下：")
    print(f"整数参数 number: {args.number}")
    print(f"字符串参数 string: {args.string}")
    print(f"列表参数 list: {args.list}")
    print(f"布尔标志参数 flag: {args.flag}")


if __name__ == "__main__":
    main()
