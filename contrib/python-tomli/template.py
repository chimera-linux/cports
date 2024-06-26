pkgname = "python-tomli"
pkgver = "2.0.1"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "TOML parser for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/hukkin/tomli"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ad22dbc128623e0c156ffaff019f29f456eba8a5d5a05164dd34f63e560449df"


def post_install(self):
    self.install_license("LICENSE")
