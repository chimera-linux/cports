pkgname = "python-jaraco.context"
pkgver = "5.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
checkdepends = [
    "python-jaraco.functools",
    "python-portend",
    "python-pytest",
    "python-tempora",
]
pkgdesc = "Python decorators and context managers"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jaraco/jaraco.context"
source = f"$(PYPI_SITE)/j/jaraco.context/jaraco.context-{pkgver}.tar.gz"
sha256 = "c2f67165ce1f9be20f32f650f25d8edfc1646a8aeee48ae06fb35f90763576d2"


def post_install(self):
    self.install_license("LICENSE")
