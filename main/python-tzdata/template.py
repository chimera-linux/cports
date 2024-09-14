pkgname = "python-tzdata"
pkgver = "2024.1"
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
sha256 = "ee55197750b6002030c370f72c93f5f8fa863b98c7a3312850781cdc1e9f1037"
