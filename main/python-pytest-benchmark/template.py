pkgname = "python-pytest-benchmark"
pkgver = "4.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
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
sha256 = "fb0785b83efe599a6a956361c0691ae1dbb5318018561af10f3e915caa0048d1"
# FIXME
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
