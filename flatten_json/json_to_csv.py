"""General function for turning a json into a header and value lists"""


def get_flat_json(json_data, header_string, header, row):
    """Parse json files with nested key-vales into flat lists using nested column labeling"""
    for root_key, root_value in json_data.items():
        if isinstance(root_value, dict):
            get_flat_json(root_value, header_string + '_' + str(root_key), header, row)
        elif isinstance(root_value, list):
            for value_index in range(len(root_value)):
                for nested_key, nested_value in root_value[value_index].items():
                    header[0].append((header_string +
                                      '_' + str(root_key) +
                                      '_' + str(nested_key) +
                                      '_' + str(value_index)).strip('_'))
                    if nested_value is None:
                        nested_value = ''
                    row[0].append(str(nested_value))
        else:
            if root_value is None:
                root_value = ''
            header[0].append((header_string + '_' + str(root_key)).strip('_'))
            row[0].append(root_value)
    return header, row


if __name__ == '__main__':
    get_flat_json({'test_key': 'test_value'}, '', [[]], [[]])
