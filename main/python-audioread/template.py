pkgname = "python-audioread"
pkgver = "3.0.1"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Cross-library audio decoding for Python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/beetbox/audioread"
source = (
    f"https://github.com/beetbox/audioread/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "98367fc46c436922e5c5b6aae59606c60c7ced36a0336cb8845fe85d0b2de383"
# needs working audio backends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
