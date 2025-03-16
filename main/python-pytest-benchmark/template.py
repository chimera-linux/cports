pkgname = "python-pytest-benchmark"
pkgver = "5.1.0"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-pytest"]
checkdepends = [*depends]
pkgdesc = "Pytest fixture for benchmarking"
license = "BSD-2-Clause"
url = "https://github.com/ionelmc/pytest-benchmark"
source = f"$(PYPI_SITE)/p/pytest-benchmark/pytest-benchmark-{pkgver}.tar.gz"
sha256 = "9ea661cdc292e8231f7cd4c10b0319e56a2118e2c09d9f50e1b3d150d2aca105"
# FIXME
options = ["!check"]

if self.profile().arch in [
    "aarch64",
    "ppc64le",
    "ppc64",
    "ppc",
    "x86_64",
]:
    depends += ["python-py-cpuinfo"]
    checkdepends += ["python-py-cpuinfo"]


def post_install(self):
    self.install_license("LICENSE")
