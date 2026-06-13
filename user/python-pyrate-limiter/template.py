pkgname = "python-pyrate-limiter"
pkgver = "4.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-hatchling", "python-uv-dynamic-versioning"]
depends = ["python", "python-filelock"]
pkgdesc = "Rate-limiter using leaky-bucket algorithm"
license = "MIT"
url = "https://github.com/vultran1710/PyrateLimiter"
source = f"$(PYPI_SITE)/p/pyrate-limiter/pyrate_limiter-{pkgver}.tar.gz"
sha256 = "be1ac413a263aa410b98757d1b01a880650948a1fc3a959512f15865eb58dbf3"
# needs pytest, is a dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
