pkgname = "python-tomli-w"
pkgver = "1.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
makedepends = ["python-pytest"]
checkdepends = ["python-tomli"]
depends = ["python"]
pkgdesc = "TOML writer for Python"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/hukkin/tomli-w"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4fe1fb4696899c01356ef4e028c975103abf62e5fa9472f31f1714100f1b065d"


def post_install(self):
    self.install_license("LICENSE")
