pkgname = "python-tinycss2"
pkgver = "1.5.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python-webencodings"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "CSS parser for python"
license = "BSD-3-Clause"
url = "https://github.com/Kozea/tinycss2"
source = f"$(PYPI_SITE)/t/tinycss2/tinycss2-{pkgver}.tar.gz"
sha256 = "d339d2b616ba90ccce58da8495a78f46e55d4d25f9fd71dfd526f07e7d53f957"


def post_install(self):
    self.install_license("LICENSE")
