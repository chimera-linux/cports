pkgname = "python-glad"
pkgver = "2.0.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-jinja2",
    "python-setuptools",
]

depends = ["python-jinja2"]
pkgdesc = "Multi-language graphics API loader generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://glad.dav1d.de"
source = f"https://github.com/Dav1dde/glad/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "44f06f9195427c7017f5028d0894f57eb216b0a8f7c4eda7ce883732aeb2d0fc"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
