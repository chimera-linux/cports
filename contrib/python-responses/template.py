pkgname = "python-responses"
pkgver = "0.25.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-pyyaml",
    "python-requests",
    "python-urllib3",
]
pkgdesc = "Utility library for mocking out the requests python library"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/getsentry/responses"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "aadd7764d734f28f43570702df1ae77dbeb78c45fbf1c015bc989909ee1eb11b"
# deprecated check dependencies
options = ["!check"]
