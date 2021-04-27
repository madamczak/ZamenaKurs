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


config_file_text2 = """
# EMA ESVC TEST CRQ000081175218 20151127 MC
#######################################################
[serverClass:nordea_intg_ema_esvc_test_na]
whitelist.0 = ap-nex3[01]t
[serverClass:nordea_intg_ema_esvc_test_na:app:nordea_intg_ema_esvc_test_na]

# EMA ESVC PREPROD CRQ000081175093 20151127 TP
#######################################################
[serverClass:nordea_intg_ema_esvc_preprod_na]
whitelist.0 = ap-nex3[01]d
[serverClass:nordea_intg_ema_esvc_preprod_na:app:nordea_intg_ema_esvc_preprod_na]
"""

config_file_text3 = """
[serverClass:nordea_intg_appl_cba_test_na-nix]
whitelist.0 = ap-cbpwl[2-9]t*
whitelist.1 = ap-cbpwl[1-8][0-9]t*
[serverClass:nordea_intg_appl_cba_test_na-nix:app:nordea_preprod_uf_limitsconf]
[serverClass:nordea_intg_appl_cba_test_na-nix:app:nordea_intg_appl_cba_test_na-nix]
"""


config_file_text4 = """
## CRQ000081453033 TKCLI PREPROD Linux - TE 20171208
############################################
[serverClass:nordea_intg_infra_tkcli_preprod_linux]
whitelist.0 = apz-ion1d*
#CRQ000081457323 AB DEC192017
whitelist.1 = ap-calyp[1234]d
[serverClass:nordea_intg_infra_tkcli_preprod_linux:app:nordea_intg_infra_tkcli_preprod_linux]
"""

config_file_text5 = """
# ZW DEV CRQ000081444637 WK 20171214
# ZW DEV CRQ001000007813 PL 20200708
#######################################################
[serverClass:nordea_intg_appl_zw_dev_na]
#CRQ000081457323 AB DEC192017
whitelist.0 = ap-njgowls20c.oneadr.net
whitelist.1 = ap-njgowls39c.oneadr.net
whitelist.2 = ap-njgowls11[23]c*
[serverClass:nordea_intg_appl_zw_dev_na:app:nordea_intg_appl_zw_dev_na]
"""


import re


def find_apps(config_file_text):
    all_apps = []

    for line in config_file_text.split('\n'):
        app = re.search(r"^\[.*", line)
        if app is not None:
            all_apps.append(app.group(0))

    return all_apps

apss1 = find_apps(config_file_text)
apss2 = find_apps(config_file_text2)
apss3 = find_apps(config_file_text3)
apss4 = find_apps(config_file_text4)

# print(apss1)
# print(apss2)
# print(apss3)

def find_opening_and_closing_tag_for_all(all_apps_list):
    opening_and_closing_tags = {}

    for app in all_apps_list:
        if ":" not in app.replace("serverClass:", ""):
            starting_index = all_apps_list.index(app)
            opening_and_closing_tags[app] = []
            for tag in all_apps_list[starting_index + 1:]:
                if app[:-1] in tag:
                    opening_and_closing_tags[app].append(tag)

    return opening_and_closing_tags


openclose1 = find_opening_and_closing_tag_for_all(apss1)
openclose2 = find_opening_and_closing_tag_for_all(apss2)
openclose3 = find_opening_and_closing_tag_for_all(apss3)
openclose4 = find_opening_and_closing_tag_for_all(apss4)

# print(openclose1)
# print(openclose2)
# print(openclose3)

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


def get_all_comments_for_app(app_name, file_text):
    comments = []

    opening_tag_index = file_text.find(app_name) + len(app_name)
    closing_tag_index = file_text.rfind(app_name[:-1])

    app_file_fragment = file_text[opening_tag_index: closing_tag_index]

    for line in app_file_fragment.strip().split("\n"):
        if line.startswith("#"):
            comments.append(line)

    return comments


keys1 = list(openclose1.keys())
keys2 = list(openclose2.keys())
keys3 = list(openclose3.keys())
keys4 = list(openclose4.keys())

for key in keys4:
    comments = get_all_comments_for_app(key, config_file_text4)
    for comment in comments:
        print(comment)

# print()

# for key in keys1:
#     white_list_servers = get_all_server_names_for_app(key, config_file_text)[0]
#     for w_server_name in white_list_servers:
#         print(f"For server regex: {w_server_name}", evaluate_server_names(w_server_name))


# for key2 in keys2:
#     white_list_servers = get_all_server_names_for_app(key2, config_file_text2)[0]
#     for w_server_name in white_list_servers:
#         print(f"For server regex: {w_server_name}", evaluate_server_names(w_server_name))
#
# for key3 in keys3:
#     white_list_servers = get_all_server_names_for_app(key3, config_file_text3)[0]
#     for w_server_name in white_list_servers:
#         print(f"For server regex: {w_server_name}", evaluate_server_names(w_server_name))


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

            for closing_tag in opening_and_closing_tags.get(app):
                new_file.write(f"{closing_tag}\n")


create_new_config_file(config_file_text2, "nowy.txt")

#
# if __name__ == "__main__":
#     import argparse
#
#     my_parser = argparse.ArgumentParser(description='Unparse config file machine names. Usage: "python whitelists.py [input_config_path] [output_config_name]"')
#     my_parser.add_argument('Path', type=str, help='the path to config file')
#     my_parser.add_argument('OutFile', type=str, help='the path to config file')
#
#     args = my_parser.parse_args()
#     config_file_path = args.Path
#     output_file = args.OutFile
#
#     with open(config_file_path) as f:
#         create_new_config_file(f.read(), output_file)
