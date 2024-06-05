pkgname = "python-astor"
pkgver = "0.8.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--deselect=tests/test_rtrip.py::RtripTestCase::test_convert_stdlib",
    "--deselect=tests/test_code_gen.py::CodegenTestCase::test_type_parameter_function",
]
hostmakedepends = [
    "python-build",
    "python-setuptools",
    "python-wheel",
    "python-installer",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python AST read/write"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://github.com/berkerpeksag/astor"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "eee1edbf7d58dbc01f0e42fa1a6a1e15470335ec6b82f090dfcf18c10d27c89c"


def post_install(self):
    self.install_license("LICENSE")
