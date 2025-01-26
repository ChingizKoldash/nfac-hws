from main import load_ascii_art, text_to_ascii_art, text_to_ascii_art_file
import os

FILE_PATH = 'test.txt'

def test_load_ascii_art():
    ascii_art_dict = load_ascii_art(FILE_PATH)
    assert isinstance(ascii_art_dict, dict)


def test_text_to_ascii_art():
    ascii_art_dict = load_ascii_art(FILE_PATH)
    result = text_to_ascii_art("hello", ascii_art_dict)
    assert isinstance(result, list)
    assert len(result) == 8


def test_text_to_ascii_art_file():
    ascii_art_dict = load_ascii_art(FILE_PATH)
    output_file = 'test/output.txt'
    if os.path.exists(output_file):
        os.remove(output_file)
    text_to_ascii_art_file(output_file, "hello", ascii_art_dict)
    assert os.path.exists(output_file), "Файл не был создан"


def test_load_ascii_art_with_invalid_file():
    ascii_art_dict = load_ascii_art('test/empty.txt')
    assert ascii_art_dict == {}

