pkgname = "asciinema"
pkgver = "2.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Terminal session recorder"
maintainer = "cassiofb-dev <contact@cassiofernando.com>"
license = "GPL-3.0-only"
url = "https://github.com/asciinema/asciinema"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b0e05f0b5ae7ae4e7186c6bd824e6d670203bb24f1c89ee52fc8fae7254e6091"
