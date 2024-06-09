pkgname = "python-parsedatetime"
pkgver = "2.6"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Parse human-readable date/time strings"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://github.com/bear/parsedatetime"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0cbf3fe4dee18c88df343bc568d35fdc67774846cb4aec2b2626d1bee7a0c6c5"
