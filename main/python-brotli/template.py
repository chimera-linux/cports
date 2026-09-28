pkgname = "python-brotli"
pkgver = "1.2.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"USE_SYSTEM_BROTLI": "1"}
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-pkgconfig",
    "python-setuptools",
    "python-wheel",
]
makedepends = [
    "brotli-devel",
    "python-devel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python bindings for the Brotli compression library"
license = "MIT"
url = "https://github.com/google/brotli"
source = f"$(PYPI_SITE)/b/brotli/brotli-{pkgver}.tar.gz"
sha256 = "e310f77e41941c13340a95976fe66a8a95b01e783d430eeaf7a2f87e0a57dd0a"


def post_install(self):
    self.install_license("LICENSE")
