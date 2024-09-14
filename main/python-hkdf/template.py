pkgname = "python-hkdf"
pkgver = "0.0.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
pkgdesc = "HKDF Python implementation"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://github.com/casebeer/python-hkdf"
source = f"$(PYPI_SITE)/h/hkdf/hkdf-{pkgver}.tar.gz"
sha256 = "622a31c634bc185581530a4b44ffb731ed208acf4614f9c795bdd70e77991dca"
# Tests and license file are both not in tarball (and no tags on repo)
options = ["!check", "!distlicense"]
