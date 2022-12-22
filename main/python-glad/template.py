pkgname = "python-glad"
pkgver = "2.0.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "python-jinja2"]
depends = ["python", "python-jinja2"]
pkgdesc = "Multi-language graphics API loader geneeeerator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://glad.dav1d.de"
source = f"https://github.com/Dav1dde/glad/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0326d59b1ccf8ccae1fface5bfb71bec1bb41fbe2341e722b31f6acac3068aeb"
# unpackaged checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

# FIXME visibility
hardening = ["!vis"]
