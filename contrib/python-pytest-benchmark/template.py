pkgname = "python-pytest-benchmark"
pkgver = "4.0.0"
pkgrel = 0
build_style = "python_pep517"
# elastic search not packaged, others need importlib_metadata
make_check_args = [
    "-W",
    "ignore::DeprecationWarning",
    "--ignore",
    "tests/test_elasticsearch_storage.py",
    "--deselect=tests/test_cli.py::test_compare",
    "--deselect=tests/test_benchmark.py::test_histogram",
    "--deselect=tests/test_storage.py::test_rendering",
    "--deselect=tests/test_storage.py::test_regression_checks",
    "--deselect=tests/test_storage.py::test_compare_1",
    "--deselect=tests/test_storage.py::test_compare_2",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-py-cpuinfo", "python-pytest"]
checkdepends = [
    "git",
    "python-aspectlib",
    "python-freezegun",
    "python-pygal",
    "python-pygaljs",
    "python-pytest-xdist",
] + depends
pkgdesc = "Pytest fixture for benchmarking code"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "BSD-2-Clause"
url = "https://github.com/ionelmc/pytest-benchmark"
source = f"$(PYPI_SITE)/p/pytest-benchmark/pytest-benchmark-{pkgver}.tar.gz"
sha256 = "fb0785b83efe599a6a956361c0691ae1dbb5318018561af10f3e915caa0048d1"


def post_install(self):
    self.install_license("LICENSE")
