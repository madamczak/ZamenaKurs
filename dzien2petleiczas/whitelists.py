config_file_text = """
[app_a]
whitelist.0 = server1
whitelist.1 = server[0-9]p*
whitelist.2 = server[1458][0-5]
[app_a:wtf:chujwieco]
[app_b]
whitelist.0 = server1
[app_b:trololo]
"""
import re

def find_apps(config_file_text):
    all_apps = []

    for line in config_file_text.split('\n'):
        app = re.search(r"^\[.*", line)
        if app is not None:
            all_apps.append(app.group(0))

    return all_apps


def get_all_server_names_for_app(app_name, file_text):
    whitelist_server_names = []
    blacklist_server_names = []

    opening_tag_index = file_text.find(app_name) + len(app_name)
    closing_tag_index = file_text.rfind(app_name[:-1])

    app_file_fragment = file_text[opening_tag_index: closing_tag_index]

    for line in app_file_fragment.strip().split("\n"):
        if "white" in line:
            whitelist_server_names.append(line.split("=")[1].strip())
        elif "black" in line:
            blacklist_server_names.append(line.split("=")[1].strip())

    return whitelist_server_names, blacklist_server_names


def find_opening_and_closing_tag_for_all(all_apps_list):
    opening_and_closing_tags = {}

    for app in all_apps_list:
        if ":" not in app:
            starting_index = all_apps_list.index(app)
            for tag in all_apps_list[starting_index + 1:]:
                if app[:-1] in tag:
                    opening_and_closing_tags[app] = tag
                    break

    return opening_and_closing_tags


def combine_all_possible_machine_numbers(count_numbers_dictionary):
    # currently supporting up to 3 regex value segments
    combined_numbers = []
    max_depth_number = max(count_numbers_dictionary.keys())
    if max_depth_number > 2:
        raise Exception("Not supported")

    zero_order_numbers = count_numbers_dictionary.get(0)
    first_order_numbers = count_numbers_dictionary.get(1)
    second_order_numbers = count_numbers_dictionary.get(1)

    if max_depth_number == 0:
        return zero_order_numbers
    elif max_depth_number == 1:
        for zero_num in zero_order_numbers:
            for first_num in first_order_numbers:
                combined_numbers.append(zero_num + first_num)
    elif max_depth_number == 2:
        for zero_num in zero_order_numbers:
            for first_num in first_order_numbers:
                for second_num in second_order_numbers:
                    combined_numbers.append(zero_num + first_num + second_num)

    return combined_numbers


def evaluate_server_names(server_name):
    list_of_evaluated_names = []

    if "[" not in server_name:
        return [server_name]

    number_search = re.search(r"\[.*\]", server_name)
    if number_search is not None:
        numbers = number_search.group(0)
        count_of_elements_to_parse = numbers.count('[')
        split_numbers = [number[:-1] for number in numbers.split('[') if number.endswith(']')]

        numbers_per_count = {}

        for count in range(count_of_elements_to_parse):
            current_numbers_to_parse = split_numbers[count]
            parserd_current_numbers = []

            if "-" in current_numbers_to_parse:
                split_segment = current_numbers_to_parse.split('-')
                for machine_number in range(int(split_segment[0]), int(split_segment[1]) + 1):
                    parserd_current_numbers.append(str(machine_number))
            else:
                parserd_current_numbers = [n for n in current_numbers_to_parse]
            numbers_per_count[count] = parserd_current_numbers

        server_name_prefix = server_name[:server_name.find("[")]
        server_name_suffix = server_name[server_name.rfind("]") + 1:]

        all_combined_numbers = combine_all_possible_machine_numbers(numbers_per_count)
        for machine_number in all_combined_numbers:
            list_of_evaluated_names.append(f"{server_name_prefix}{machine_number}{server_name_suffix}")

    return list_of_evaluated_names


def create_new_config_file(old_config_file_text, new_file_path):
    all_apps = find_apps(old_config_file_text)
    opening_and_closing_tags = find_opening_and_closing_tag_for_all(all_apps)

    with open(new_file_path, "w") as new_file:
        for app in opening_and_closing_tags.keys():
            new_file.write(f"{app}\n")

            whitelist_server_names, blacklist_server_names = get_all_server_names_for_app(app, old_config_file_text)
            whitecount = 0
            for w_server_name in whitelist_server_names:
                evaluated_white_servers = evaluate_server_names(w_server_name)
                for evaluated_w_server_name in evaluated_white_servers:
                    line_to_write = f"whitelist.{whitecount} = {evaluated_w_server_name}\n"
                    new_file.write(line_to_write)
                    whitecount += 1

            blackcount = 0
            for b_server_name in blacklist_server_names:
                evaluated_b_servers = evaluate_server_names(b_server_name)
                for evaluated_b_server_name in evaluated_b_servers:
                    line_to_write = f"blacklist.{blackcount} = {evaluated_b_server_name}\n"
                    new_file.write(line_to_write)
                    blackcount += 1

            new_file.write(f"{opening_and_closing_tags.get(app)}\n")


create_new_config_file(config_file_text, "new_cfg_file.txt")
