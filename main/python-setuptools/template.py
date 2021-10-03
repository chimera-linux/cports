pkgname = "python-setuptools"
pkgver = "57.0.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools"
sources = [f"$(PYPI_SITE)/s/setuptools/setuptools-{pkgver}.tar.gz"]
sha256 = ["401cbf33a7bf817d08014d51560fc003b895c4cdc1a5b521ad2969e928a07535"]

options = ["!check", "!lint", "!spdx"]

env = {
    "SETUPTOOLS_INSTALL_WINDOWS_SPECIFIC_FILES": "0",
    "SETUPTOOLS_DISABLE_VERSIONED_EASY_INSTALL_SCRIPT": "1"
}

def post_install(self):
    self.install_license("LICENSE")
