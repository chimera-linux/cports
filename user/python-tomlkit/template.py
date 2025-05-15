pkgname = "python-tomlkit"
pkgver = "0.13.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
checkdepends = [
    "python-pytest",
    "python-pyyaml",
]
pkgdesc = "Style preserving TOML library for Python"
license = "MIT"
url = "https://github.com/python-poetry/tomlkit"
source = f"$(PYPI_SITE)/t/tomlkit/tomlkit-{pkgver}.tar.gz"
sha256 = "430cf247ee57df2b94ee3fbe588e71d362a941ebb545dec29b53961d61add2a1"


def post_install(self):
    self.install_license("LICENSE")
