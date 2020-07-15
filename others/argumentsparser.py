import argparse
# 在3.2版本后 optparser被取代， 功能转移到argparser模块中


def args_parse():
    usage = """




"""
    # 创建 参数解析器
    parser = argparse.ArgumentParser(description='Process some integers.')
    # 添加参数处理
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulator', action='store_const',
                        const=sum, default=max,
                        help='sum the integers(default:find the max)')
    # 解析参数
    args = parser.parse_args()
    print(args.accumulator(args.integers))


if __name__ == "__main__":
    args_parse()
