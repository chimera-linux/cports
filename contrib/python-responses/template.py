pkgname = "python-responses"
pkgver = "0.24.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = [
    "python-pytest",
    "python-pytest-asyncio",
    "python-pyyaml",
    "python-requests",
    "python-tomli-w",
]
pkgdesc = "Utility library for mocking out the requests python library"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/getsentry/responses"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "de03bb56d7f07229b1743e63e326a62ad9705f939484754abe74c294dcb74f27"
# FIXME: broken tests
options = ["!check"]
