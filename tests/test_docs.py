
import pytest
from pytest_examples import find_examples, CodeExample, EvalExample
import pathlib

FDIR_DOCS = pathlib.Path(__file__).parent.parent / "docs"

@pytest.mark.parametrize('example', find_examples(FDIR_DOCS), ids=str)
def test_get_project(example: CodeExample, eval_example: EvalExample):
    eval_example.run_print_check(example)