# app.py
# Test commit to verify github action - upon push/commit to main branch myfirst-action.yml will trigger
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
