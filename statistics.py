def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values) / 2)  # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index - 1]) / 2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    return sum(list_of_values) / len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average) ** 2 for x in list_of_values])
    return squared_sum / (len(list_of_values) - 1)


def covariance(first_list_of_values, second_list_of_values):
    average_first_list = mean(first_list_of_values)
    average_second_list = mean(second_list_of_values)
    x_and_y_correlation_at_lists = sum([(x - average_first_list) * (y - average_second_list)
                                        for x, y in zip(first_list_of_values, second_list_of_values)])
    result = x_and_y_correlation_at_lists / (len(first_list_of_values) - 1)

    return result


def correlation(first_list_of_values, second_list_of_values):
    standard_deviation_first_list = variance(first_list_of_values) ** 0.5
    standard_deviation_second_list = variance(second_list_of_values) ** 0.5

    covariance_of_two_lists = covariance(first_list_of_values, second_list_of_values)

    result = covariance_of_two_lists / (standard_deviation_first_list * standard_deviation_second_list)
    return result
