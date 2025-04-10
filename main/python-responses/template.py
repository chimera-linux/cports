pkgname = "python-responses"
pkgver = "0.25.7"
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
license = "Apache-2.0"
url = "https://github.com/getsentry/responses"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c77e5800fb747f952a8222f3040b6f1c9023d3b8758cf4ef0372359847c66652"
# deprecated check dependencies
options = ["!check"]
