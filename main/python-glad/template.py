pkgname = "python-glad"
pkgver = "2.0.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-jinja2",
    "python-setuptools",
    "python-wheel",
]

depends = ["python", "python-jinja2"]
pkgdesc = "Multi-language graphics API loader generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://glad.dav1d.de"
source = f"https://github.com/Dav1dde/glad/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "850351f1960f3fed775f0b696d7f17615f306beb56be38a20423284627626df1"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
