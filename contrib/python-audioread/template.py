pkgname = "python-audioread"
pkgver = "3.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Cross-library audio decoding for Python"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/beetbox/audioread"
source = (
    f"https://github.com/beetbox/audioread/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "57766a926f522e9a05ccd07d438d0c8998fc53d0489efeb40a256d7ca42b1369"
# needs working audio backends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
