pkgname = "python-glad"
pkgver = "2.0.4"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-jinja2",
    "python-setuptools",
    "python-wheel",
]

depends = ["python", "python-jinja2"]
pkgdesc = "Multi-language graphics API loader geneeeerator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://glad.dav1d.de"
source = f"https://github.com/Dav1dde/glad/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "02629644c242dcc27c58222bd2c001d5e2f3765dbbcfd796542308bddebab401"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
