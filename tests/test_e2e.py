import subprocess

import pytest


@pytest.fixture
def project_name() -> str:
    return 'testproject'


def test_e2e(tmpdir, project_name: str):
    subprocess.check_call(
        [
            'prefab',
            project_name,
        ],
        cwd=tmpdir,
    )
    subprocess.check_call(
        [
            'pipenv',
            'run',
            'pytest',
            'tests',
        ],
        cwd=tmpdir / project_name,
    )
