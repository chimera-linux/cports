pkgname = "python-glad"
pkgver = "2.0.7"
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
sha256 = "45f5754fc91de428a840e6ad0237a5577c342b53448527ee073d055c9f8fc767"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
