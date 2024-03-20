pkgname = "nihtest"
pkgver = "1.5.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-dateutil"]
checkdepends = ["cmake", "ninja"] + depends
pkgdesc = "Testing tool for command line utilities"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/nih-at/nihtest"
source = f"{url}/releases/download/v{pkgver}/nihtest-{pkgver}.tar.gz"
sha256 = "a83f7c92f5c15cdbaa2d4e4305e565a72db0ab09d9679d932bd9cdceb4d5b229"


def do_check(self):
    from cbuild.util import cmake

    for func in [cmake.configure, cmake.build, cmake.ctest]:
        func(pkg=self, build_dir="build")


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("manpages/nihtest-case.man", name="nihtest-case", cat=5)
    self.install_man("manpages/nihtest.conf.man", name="nihtest.conf", cat=5)
    self.install_man("manpages/nihtest.man", name="nihtest", cat=1)
