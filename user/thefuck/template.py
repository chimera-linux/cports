pkgname = "thefuck"
pkgver = "3.32"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # https://github.com/nvbn/thefuck/issues/1438
    "--deselect=tests/test_utils.py::TestGetValidHistoryWithoutCurrent",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-colorama",
    "python-decorator",
    "python-psutil",
    "python-pyte",
    "python-six",
]
checkdepends = ["python-pytest-mock", *depends]
pkgdesc = "Command-line tool to correct errors in shell commands"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://github.com/nvbn/thefuck"
# pypi tarball missing tests
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "76cbb014473672d1c384922857f8fbc1f6f7774f74f784149ad88751854ecfdf"


def post_install(self):
    self.install_license("LICENSE.md")
