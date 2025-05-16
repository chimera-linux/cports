pkgname = "python-fonttools"
pkgver = "4.58.0"
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
sha256 = "a4aea9d4bd7596fca7e7f8cca2b19535e43778895f228cbd8e3d4a9f13df52df"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
