from statsmodels.stats.proportion import proportions_ztest

chat_id = 632165934  # Ваш chat ID, не меняйте название переменной
CONST = 0.03


def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    _, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='smaller')
    return p_value < CONST
