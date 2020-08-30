import json
# Might need a numpy import for label vectors


def _clean_up_values(info, value):
    # TODO: might have to add additional replace statements if there are more irregular characters
    if info == 'name':
        output = value if value else ''
    elif info == 'mana_cost':
        output = value.replace('{', '').replace('}', '') if value else '0'
    elif info == 'cmc':
        output = str(int(value)) if value else str(0)
    elif info == 'type_line':
        output = value.replace('\u2014', '') if value else ''
    elif info == 'oracle_text':
        output = value.replace('\u2014', '').replace('\u2022', '').replace('\n', '') if value else ''
    elif info == 'power':
        output = value if value else ''
    elif info == 'toughness':
        output = value if value else ''
    elif info == 'colors':
        output = ' '.join(value) if value else ''
    elif info == 'color_identity':
        output = ' '.join(value) if value else ''
    elif info == 'keywords':
        output = ' '.join(value) if value else ''
    elif info == 'rarity':
        output = value if value else ''
    elif info == 'flavor_text':
        output = value.replace('\u2014', '').replace('\u2022', '').replace('\n', '') if value else ''
    else:
        raise ValueError()
    return output


def _unite_card_info_into_single_string(card, to_predict):
    text = []
    for info in card:
        if info != to_predict:
            text.append(_clean_up_values(info, card[info]))
    return ' '.join(text)


def load_data(dataset, to_predict):
    with open(f'../data/{dataset}.json', 'r') as json_file:
        data = json.load(json_file)
        print(data['cards'][0])

    pass


if __name__ == '__main__':
    load_data('pioneer_no_lands')
