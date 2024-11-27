pkgname = "python-docopt"
pkgver = "0.6.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "CLI creating helper for python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/docopt/docopt"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2113eed1e7fbbcd43fb7ee6a977fb02d0b482753586c9dc1a8e3b7d541426e99"
# broken in new pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
