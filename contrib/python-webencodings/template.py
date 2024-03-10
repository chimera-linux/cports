pkgname = "python-webencodings"
pkgver = "0.5.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python WHATWG encoding implementation"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/gsnedders/python-webencodings"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "082367f568a7812aa5f6922ffe3d9d027cd83829dc32bcaac4c874eeed618000"


def post_install(self):
    self.install_license("LICENSE")
