from itertools import product


def calculate_a_payoff(a_strategy, current_state, payoff_matrix):
    """
    计算玩家a采用某个策略时的总收益
    :param a_strategy: 玩家a考虑采用的策略
    :param current_state: 当前局势（其他n个玩家的策略组合）
    :param payoff_matrix: 收益矩阵
    :return: 玩家a的总收益
    """
    total_payoff = 0
    for opponent_strategy in current_state:
        # 玩家a总是收益元组的第一个元素
        payoff = payoff_matrix[a_strategy][opponent_strategy][0]
        total_payoff += payoff
    return total_payoff


def build_a_strategy_transition_table(n, k, payoff_matrix):
    """
    构建玩家a的策略转移表
    :param n: 与玩家a博弈的玩家数量
    :param k: 策略数量
    :param payoff_matrix: 收益矩阵
    :return: 转移表（字典：其他玩家的局势->玩家a的最佳策略）
    """
    transition_table = {}
    all_possible_states = product(range(k), repeat=n)

    for current_state in all_possible_states:
        current_state = tuple(current_state)
        max_payoff = -float('inf')
        best_strategy = 0  # 默认策略

        # 测试玩家a的所有可能策略
        for a_strategy in range(k):
            payoff = calculate_a_payoff(a_strategy, current_state, payoff_matrix)

            if payoff > max_payoff:
                max_payoff = payoff
                best_strategy = a_strategy
            elif payoff == max_payoff:
                # 收益相同时选择编号较小的策略
                best_strategy = min(best_strategy, a_strategy)

        transition_table[current_state] = best_strategy

    return transition_table


# 示例使用
if __name__ == "__main__":
    # 囚徒困境收益矩阵
    k = 2
    payoff_matrix = [
        [(-6, -6), (-5, -7)],  # 策略0: 合作
        [(-7, -5), (-3, -3)]  # 策略1: 背叛
    ]

    n = 2  # 3个玩家与玩家a博弈

    # 构建玩家a的策略转移表
    a_transition_table = build_a_strategy_transition_table(n, k, payoff_matrix)

    # 打印转移表
    print("玩家a的策略转移表（其他玩家局势 -> 玩家a的最佳策略）:")
    for state, a_strategy in a_transition_table.items():
        print(f"{state} -> {a_strategy}")


