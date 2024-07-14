pkgname = "python-autobahn"
pkgver = "23.6.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = [
    "python-attrs",
    "python-cryptography",
    "python-hyperlink",
    "python-setuptools",
    "python-twisted",
    "python-txaio",
    "python-zope.interface",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python implementation of websocket and WAMP protocols"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://autobahn.readthedocs.io"
source = f"$(PYPI_SITE)/a/autobahn/autobahn-{pkgver}.tar.gz"
sha256 = "ec9421c52a2103364d1ef0468036e6019ee84f71721e86b36fe19ad6966c1181"
# https://github.com/crossbario/autobahn-python/issues/1117
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
