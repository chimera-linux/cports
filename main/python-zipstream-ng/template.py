pkgname = "python-zipstream-ng"
pkgver = "1.8.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Streamable zip file generator"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-3.0-only"
url = "https://github.com/pR0Ps/zipstream-ng"
source = f"$(PYPI_SITE)/z/zipstream-ng/zipstream_ng-{pkgver}.tar.gz"
sha256 = "b7129d2c15d26934b3e1cb22256593b6bdbd03c553c26f4199a5bf05110642bc"
