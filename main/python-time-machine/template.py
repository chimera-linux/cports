pkgname = "python-time-machine"
pkgver = "2.19.0"
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
sha256 = "1f255174a36d89e8791d0cd22ebdec28e683480c967e58085c8bd1b70b9207f2"


def post_install(self):
    self.install_license("LICENSE")
