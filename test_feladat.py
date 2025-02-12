import pytest
from bs4 import BeautifulSoup

def test_container_exists(html):
    assert html.find('div', class_='container') is not None

def test_h1_exists(html):
    container = html.find('div', class_='container')
    assert container.find('h1') is not None
    assert container.find('h1').text == 'Lorem ipsum'

def test_h2_exists(html):
    container = html.find('div', class_='container')
    assert container.find('h2') is not None
    assert container.find('h2').text == 'DOLOR EST AMET'

def test_note1_exists(html):
    container = html.find('div', class_='container')
    assert container.find('aside', class_='note1') is not None


def test_p_elements_exist(html):
    container = html.find('div', class_='container')
    assert len(container.find_all('p')) == 3

def test_note2_exists(html):
    container = html.find('div', class_='container')
    assert container.find('aside', class_='note2') is not None

def test_style_link_exists(html):
    assert html.find('link', rel='stylesheet', href='style.css') is not None

def test_container_styles(css):
    assert 'margin: 5%' in css
    assert 'background-color: lemonchiffon' in css
    assert 'padding: 15px' in css
    assert 'overflow: auto' in css

def test_h1_styles(css):
    assert 'font-family: sans-serif' in css

def test_h2_styles(css):
    assert 'font-variant: small-caps' in css

def test_note1_note2_styles(css):
    assert 'width: 105px' in css
    assert 'height: 105px' in css

def test_note1_styles(css):
    assert 'float: left' in css
    assert 'border-right: 3px solid burlywood' in css
    assert 'margin-right: 10px' in css

def test_note2_styles(css):
    assert 'float: right' in css
    assert 'border-left: 3px solid burlywood' in css
    assert 'margin-left: 10px' in css

def test_eligendi_style(css):
    assert 'font-weight: bold' in css

@pytest.fixture
def html():
    with open('index.html', 'r') as f:
        return BeautifulSoup(f, 'html.parser')

@pytest.fixture
def css():
    with open('style.css', 'r') as f:
        return f.read()