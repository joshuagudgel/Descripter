import pytest
from movie_script import *

# Constants
knivesPath = r"C:\src\Descripter\movie_scripts\knivesout-script-3.pdf"
knivesCast = ['FRAN', 'MOM', 'ALICE']
knivesDialogue = {
    'FRAN' : ['Morning Mr Thrombey', 'Mr Thrombey you up there? Mr Thrombey I\'m coming in', 'Shit.'],
    'MOM' : ['Now please just turn it off. Turn it off. Now. Alice. Off. They\'re talking about murder on it, your sister just had a friend she loves slit his throat open she doesn\'t need to be hearing that right now let\'s be sensitive!'],
    'ALICE' : ['Alice, turn that off now.', ]
}

dunePath = r"C:\src\Descripter\movie_scripts\dune-script-3.pdf"
duneCast = ['FRAN', 'MOM', 'ALICE']
duneDialogue = {
    'FRAN' : ['Morning Mr Thrombey', 'Mr Thrombey you up there? Mr Thrombey I\'m coming in', 'Shit.'],
    'MOM' : ['Now please just turn it off. Turn it off. Now. Alice. Off. They\'re talking about murder on it, your sister just had a friend she loves slit his throat open she doesn\'t need to be hearing that right now let\'s be sensitive!'],
    'ALICE' : ['Alice, turn that off now.', ]
}

# Knives Out tests
# The first 3 pages of pdf
@pytest.fixture
def knivesscript():
    return MovieScript(knivesPath)

# Test cases
def test_knives_cast():
    assert set(knivesscript.cast) is set(knivesCast)

def test_knives_dialogue():
    assert set(knivesscript.dialogue) is set(knivesDialogue)

# Dune tests
# The first 3 pages of pdf
@pytest.fixture
def dunescript():
    return MovieScript(dunePath)

# Test cases
def test_dune_cast():
    assert set(dunescript.cast) is set(duneCast)

def test_dune_dialogue():
    assert set(dunescript.dialogue) is set(duneDialogue)