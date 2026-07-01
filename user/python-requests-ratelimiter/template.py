pkgname = "python-requests-ratelimiter"
pkgver = "0.10.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-hatchling"]
depends = ["python", "python-pyrate-limiter", "python-requests-pycache"]
pkgdesc = "Rate-limiting support for python-request"
license = "MIT"
url = "https://github.com/JWCook/requests-ratelimiter"
source = (
    f"$(PYPI_SITE)/r/requests-ratelimiter/requests_ratelimiter-{pkgver}.tar.gz"
)
sha256 = "9c1a78d7646caa5ccf211a6c341abd16d329be2c8c35044a418aa9da7c0e7a33"
# needs pytest, is a dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
