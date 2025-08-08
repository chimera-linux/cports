pkgname = "python-fonttools"
pkgver = "4.59.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = [
    "python-brotli",
    "python-lxml",
    "python-pytest-xdist",
]
pkgdesc = "Library to manipulate font files from Python"
license = "MIT AND OFL-1.1 AND BSD-3-Clause AND Apache-2.0"
url = "https://github.com/fonttools/fonttools"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "cf7d72742235f72485e0fe5bfa839902e7275fbe3e6f203f3c63b38bd8880f56"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
