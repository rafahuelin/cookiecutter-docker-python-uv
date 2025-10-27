from _pytest.capture import CaptureFixture, CaptureResult

from main import main


def test_main(capsys: CaptureFixture[str]):
    main()
    capture_result: CaptureResult[str] = capsys.readouterr()
    assert capture_result.out == "Python {{cookiecutter._supported_python_versions[cookiecutter.python_version].latest}} project.\n"
