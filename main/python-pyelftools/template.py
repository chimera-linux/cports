pkgname = "python-pyelftools"
pkgver = "0.29"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "ELF and DWARF parsing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unlicense"
url = "https://github.com/eliben/pyelftools"
source = f"$(PYPI_SITE)/p/pyelftools/pyelftools-{pkgver}.tar.gz"
sha256 = "ec761596aafa16e282a31de188737e5485552469ac63b60cfcccf22263fd24ff"
# FIXME: tests cannot locate utils module?
options = ["!check"]
