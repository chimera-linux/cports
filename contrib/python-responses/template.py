pkgname = "python-responses"
pkgver = "0.25.3"
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
sha256 = "3c3f3cd9f9c00bfe962a895cdbd961fd33d258c1c1f66b79c7a3ceff6ec1615e"
# deprecated check dependencies
options = ["!check"]
