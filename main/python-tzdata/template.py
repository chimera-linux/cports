pkgname = "python-tzdata"
pkgver = "2024.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-attrs", "tzdata"]
checkdepends = ["python-pytest", "python-pytest-subtests", *depends]
pkgdesc = "Python package wrapping the IANA time zone database"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/python/tzdata"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1091c44555ab376a136cf32763f746e35137c20038d5013745685b7276e47b6b"
