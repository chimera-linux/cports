pkgname = "python-confuse"
pkgver = "2.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
depends = ["python-pyyaml"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "YAML config files for Python"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "MIT"
url = "https://github.com/beetbox/confuse"
source = f"$(PYPI_SITE)/c/confuse/confuse-{pkgver}.tar.gz"
sha256 = "7379a2ad49aaa862b79600cc070260c1b7974d349f4fa5e01f9afa6c4dd0611f"


def post_install(self):
    self.install_license("LICENSE")
