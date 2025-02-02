from find_similar.tokenize import (
    spacing,
    replacing,
    split_text_and_digits,
    get_normal_form,
    tokenize,
    STOP_WORDS,
    remove_part_speech,
    get_parsed_text,
    prepare_dictionary,
    HashebleSet,
    replace_yio,
)


def test_spacing():
    chars = ['a', 'b']
    label = 'ivonailonbi'
    label = spacing(label, chars)
    assert label == 'ivon ilon i'


def test_replacing():
    chars = ['a', 'b']
    label = 'ivonailonbi'
    label = replacing(label, chars)
    assert label == 'ivoniloni'


def test_split_text_and_digits():
    s = '1some2string5with9'
    result = split_text_and_digits(s)
    assert result == ['1', 'some', '2', 'string', '5', 'with', '9']


def test_get_normal_form():
    word = 'рыбы'
    normal_form = get_normal_form(get_parsed_text(word))
    assert normal_form == 'рыба'


def test_tokenize():
    text = 'Иван,родил/девченку-веле¶л 1тащить2пеленку3'
    result = {'пелёнка', '3', 'девчёнка', '2', '1', 'иван'}
    # without dictionary
    assert tokenize(text, STOP_WORDS) == result
    # with dictionary
    dictionary = {
        '3': 'новый конь'
    }
    result = {'пелёнка', 'новый', 'конь', 'девчёнка', '2', '1', 'иван'}
    dictionary = prepare_dictionary(dictionary)
    assert tokenize(text, STOP_WORDS, dictionary) == result


def test_remove_part_speech():
    words = ['рыбы', 'велел', 'тащить', 'пелёнку']
    non_verb_form = []
    for word in words:
        non_verb_form.append(remove_part_speech(get_parsed_text(word)))
    assert non_verb_form == ['рыба', None, None, 'пелёнка']

    word_ad = ['быстрый', '1', 'тащить', 'коня']
    non_ad_form = []
    for word in word_ad:
        non_ad_form.append(remove_part_speech(get_parsed_text(word), {'ADJF'}))
    assert non_ad_form == [None, '1', 'тащить', 'конь']


def test_get_parsed_text():
    word = "текст"
    parsed_object = get_parsed_text(word)
    assert parsed_object.word == "текст"


class TestHahsebleSet:

    def test_hash(self):
        hs = HashebleSet(['one'])
        assert hash(hs) == hash("HashebleSet({'one'})")


def test_prepare_dictionary():
    dictionary = {
        'one two': 'two three'
    }
    dictionary = prepare_dictionary(dictionary)
    assert dictionary == {HashebleSet(['one', 'two']): {'two', 'three'}}


def test_replace_yio():
    assert 'новье' == replace_yio('новьё')