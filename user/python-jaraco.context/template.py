pkgname = "python-jaraco.context"
pkgver = "6.0.1"
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
source = f"$(PYPI_SITE)/j/jaraco.context/jaraco_context-{pkgver}.tar.gz"
sha256 = "9bae4ea555cf0b14938dc0aee7c9f32ed303aa20a3b73e7dc80111628792d1b3"


def post_install(self):
    self.install_license("LICENSE")
