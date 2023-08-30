import re


def sort_text_order(text_string):

    text_segments = text_string.split("|")

    result = []

    for text_segment in text_segments:
        text_list = text_segment.split(",")

        if not re.search(r'[123456789一二三四五六七八九]+', text_list[0]):

            item = {'text': text_list[0], 'x': text_list[1], 'y': text_list[2]}

            result.append(item)

    result = sorted(result, key=lambda x: int(x['x']))

    return result


text_string = "一13,23,23|大,444,23|够,3,16|吃,194,17|123459,34,78|一二三六七八九,56,89"

sort_text_order(text_string)
