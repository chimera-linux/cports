pkgname = "python-time-machine"
pkgver = "2.17.0"
pkgrel = 0
build_style = "python_pep517"
# missing tokenize-rt
make_check_args = ["--ignore=tests/test_cli.py"]
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
]
depends = ["python-dateutil"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python library for mocking the current time"
license = "MIT"
url = "https://github.com/adamchainz/time-machine"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1cd8965cdd841a24d5f8e9c35a49c56f15a02e273186300360cfec621c0c5ef6"


def post_install(self):
    self.install_license("LICENSE")
