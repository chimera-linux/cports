pkgname = "python-magic"
pkgver = "0.4.27"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
depends = ["libmagic"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python wrapper for libmagic"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/ahupp/python-magic"
source = (
    f"https://github.com/ahupp/python-magic/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "3978a25d43d9a7b8a89ae9d726bd4962fc90dc4f69ae852e399f3c56d4b0bd63"


def init_check(self):
    # required for testsuite
    self.env["LC_ALL"] = "en_US.UTF-8"


def post_install(self):
    self.install_license("LICENSE")
