pkgname = "python-configobj"
pkgver = "5.0.8"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python-six"]
pkgdesc = "Simple but powerful config file reader and writer"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "BSD-3-Clause"
url = "https://github.com/DiffSK/configobj"
source = f"https://github.com/DiffSK/configobj/archive/v{pkgver}.tar.gz"
sha256 = "547dc047e31c71d7a8732016336769ed450588f34a7c13077aa7acc7df245eda"
# testing requires a pip environment
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
