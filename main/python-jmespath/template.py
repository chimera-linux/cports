pkgname = "python-jmespath"
pkgver = "1.0.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = [
    "python-hypothesis",
    "python-pytest-xdist",
]
pkgdesc = "JSON matching expressions"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://jmespath.org"
source = (
    f"https://github.com/jmespath/jmespath.py/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "6a02470b1716ec7a32abe89a873a4795c41c938468225f8a53d860980ec9e3c6"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]


def post_install(self):
    self.install_license("LICENSE.txt")
