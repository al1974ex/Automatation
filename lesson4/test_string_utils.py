import pytest
from string_utils import StringUtils

utils=StringUtils()

 #capitilize

def test_capitilize():
#позитивные
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello cak") == "Hello cak"
    assert utils.capitilize("161") == "161"
#негативные
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("456код") == "456код"

 #trim
def test_trim():
#позитивные
    assert utils.trim("  skypro") == "skypro"
    assert utils.trim("  hello cak") == "hello cak"
    assert utils.trim("  BMW") == "BMW"
#негативные
    assert utils.trim("") == ""
    assert utils.trim("2569") == "2569"
    assert utils.trim("!!!") == "!!!"   

#to_list
@pytest.mark.parametrize('string,delimeter,result',[
#позитивные
    ("рыба,краб,рак", ",", ["рыба", "краб", "рак"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
#негативные
    ("", None, []),
    ("рыба,краб рак", None, ["рыба", "краб рак"]),
])
def test_to_list(string,delimeter,result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string,delimeter)
    assert res == result

    #def contains
@pytest.mark.parametrize('string,symbol,result',[
#позитивные
    ("рыба", "р", True),
    ("стул", "л", True),
    ("диван-кровать", "-", True),
#негативные
    ("Ростов", "к", False),
    ("12354", "z", False),
])
def test_contains(string,symbol,result):
    res = utils.contains(string, symbol)
    assert res == result 

 # delete_symbol 
@pytest.mark.parametrize('string,symbol,result',[
#позитивные
    ("вода", "в", "ода"),
    ("столик", "к", "столи"),
    ("8547", "8", "547"),
#негативные
    ("Ростов", "к", "Ростов"),
    ("12354", " ", "12354"),
])
def test_delete_symbol(string,symbol,result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

# starts_with  
@pytest.mark.parametrize('string,symbol,result',[
#позитивные
    ("машина", "м", True),
    ("стул", "с", True),
#негативные
    ("Ростов", "р", False),
    ("", "@", False),
])
def test_starts_with(string,symbol,result):
    res = utils.starts_with(string, symbol)
    assert res == result 

#end_with 
@pytest.mark.parametrize('string,symbol,result',[
#позитивные
    ("собака", "а", True),
    ("ПИРОГ", "Г", True),
#негативные
    ("Ростов", "р", False),
    ("лев", "ч", False),
])
def test_end_with (string,symbol,result):
    res = utils.end_with (string, symbol)
    assert res == result 

#is_empty
@pytest.mark.parametrize('string,result',[
#позитивные
    ("",  True),
    (" ",  True),
#негативные
    ("Ника",  False),
    ("лев",  False),
])
def test_is_empty(string,result):
    res = utils.is_empty (string)
    assert res == result 

 # list_to_string 
@pytest.mark.parametrize('lst,joiner,result',[
#позитивные
    (["h", "e", "l", "l", "o"], ",","h,e,l,l,o"),
    (["л", "о", "д", "к", "а"], ",","л,о,д,к,а"),
#негативные
    ([], None, ""),
    ([], ",", ""),
])
def test_list_to_string (lst,joiner,result):
    if joiner == None:
        res = utils.list_to_string (lst)
    else:
        res = utils.list_to_string (lst,joiner)
    assert res == result  

