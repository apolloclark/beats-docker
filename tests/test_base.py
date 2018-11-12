import os


def test_base_os(SystemInfo):
    assert SystemInfo.distribution == os.getenv('BASE_OS')
    assert SystemInfo.release == os.getenv('BASE_OS_VER')
