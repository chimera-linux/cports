pkgname = "python-tomlkit"
pkgver = "0.13.2"
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
pkgdesc = "Style preserving TOML library"
license = "MIT"
url = "https://github.com/sdispater/tomlkit"
source = f"$(PYPI_SITE)/t/tomlkit/tomlkit-{pkgver}.tar.gz"
sha256 = "fff5fe59a87295b278abd31bec92c15d9bc4a06885ab12bcea52c71119392e79"


def post_install(self):
    self.install_license("LICENSE")
