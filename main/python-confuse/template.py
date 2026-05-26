pkgname = "python-confuse"
pkgver = "2.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-poetry-core", "python-installer"]
depends = ["python-pyyaml", "python-typing_extensions"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "YAML config files for Python"
license = "MIT"
url = "https://github.com/beetbox/confuse"
source = f"$(PYPI_SITE)/c/confuse/confuse-{pkgver}.tar.gz"
sha256 = "35c1b53e81be125f441bee535130559c935917b26aeaa61289010cd1f55c2b9e"


def post_install(self):
    self.install_license("LICENSE")
