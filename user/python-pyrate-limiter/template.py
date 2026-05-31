pkgname = "python-pyrate-limiter"
pkgver = "4.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
    "python-setuptools",
    "python-uv-dynamic-versioning",
]
depends = ["python-filelock"]
checkdepends = [
    "python-pytest",
    "python-pytest-asyncio",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Rate-limiter using leaky-bucket algorithm"
license = "MIT"
url = "https://github.com/vutran1710/PyrateLimiter"
source = f"$(PYPI_SITE)/p/pyrate-limiter/pyrate_limiter-{pkgver}.tar.gz"
sha256 = "2c0c720c4fa16c5d8199e4821bf34507fb49c007a25b786cec6fb94ffd0844aa"
# tests need a bunch of stuff
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
