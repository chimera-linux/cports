pkgname = "python-fastjsonschema"
pkgver = "2.19.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "-W",
    "ignore::DeprecationWarning",
    "--deselect=tests/test_pattern_properties.py::test_pattern_with_escape_no_warnings",
    "--deselect=tests/test_string.py::test_pattern_with_escape_no_warnings",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest", "python-pytest-benchmark"]
pkgdesc = "Fast JSON schema validator"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "BSD-3-Clause"
url = "https://github.com/horejsek/python-fastjsonschema"
source = f"$(PYPI_SITE)/f/fastjsonschema/fastjsonschema-{pkgver}.tar.gz"
sha256 = "e3126a94bdc4623d3de4485f8d468a12f02a67921315ddc87836d6e456dc789d"


def post_install(self):
    self.install_license("LICENSE")
