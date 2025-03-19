pkgname = "python-regex"
pkgver = "2024.11.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
makedepends = ["python-devel"]
pkgdesc = "Alternative regular expression module, to replace re"
license = "Apache-2.0"
url = "https://github.com/mrabarnett/mrab-regex"
source = f"$(PYPI_SITE)/r/regex/regex-{pkgver}.tar.gz"
sha256 = "7ab159b063c52a0333c884e4679f8d7a85112ee3078fe3d9004b2dd875585519"
