pkgname = "python-requests-ratelimiter"
pkgver = "0.10.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = ["python-pyrate-limiter", "python-requests"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Rate-limiting support for requests"
license = "MIT"
url = "https://github.com/JWCook/requests-ratelimiter"
source = (
    f"$(PYPI_SITE)/r/requests-ratelimiter/requests_ratelimiter-{pkgver}.tar.gz"
)
sha256 = "9c1a78d7646caa5ccf211a6c341abd16d329be2c8c35044a418aa9da7c0e7a33"
# tests need requests-mock
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
