pkgname = "python-zipstream-ng"
pkgver = "1.7.1"
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
source = f"$(PYPI_SITE)/z/zipstream-ng/zipstream-ng-{pkgver}.tar.gz"
sha256 = "f92023b9ca578cd7fdd94ec733c65664ecf7ee32493e38cdf8e365a1316e9ffc"
