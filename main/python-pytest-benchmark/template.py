pkgname = "python-pytest-benchmark"
pkgver = "5.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-py-cpuinfo",
    "python-pytest",
]
checkdepends = [*depends]
pkgdesc = "Pytest fixture for benchmarking"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://github.com/ionelmc/pytest-benchmark"
source = f"$(PYPI_SITE)/p/pytest-benchmark/pytest-benchmark-{pkgver}.tar.gz"
sha256 = "cd0adf68516eea7ac212b78a7eb6fc3373865507de8562bb3bfff2f2f852cc63"
# FIXME
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
