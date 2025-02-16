pkgname = "python-dotty-dict"
pkgver = "1.3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-poetry-core",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Dictionary wrapper for quick access to deeply nested keys"
maintainer = "Julie Koubova <julie@koubova.net>"
license = "MIT"
url = "https://github.com/pawelzny/dotty_dict"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "62d981357fae93a6133ae5788eb6d76b0c250d5af3cdbdb12914c78d85f6e535"


def post_install(self):
    self.install_license("LICENSE")
