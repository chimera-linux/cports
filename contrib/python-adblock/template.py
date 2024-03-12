pkgname = "python-adblock"
pkgver = "0.6.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "python-build",
    "python-installer",
    "python-maturin",
    "python-setuptools",
    "python-setuptools-rust",
    "python-wheel",
]
makedepends = ["rust-std"]
checkdepends = ["python-pytest-xdist"]
pkgdesc = "Python wrapper for brave's adblocking library"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/ArniDagur/python-adblock"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cdde5db640f1d9205785641665b79e6edb7c51092a68536bc4907560c71136b2"
# XXX: requires pre-installing the package
options = ["!check"]


def do_prepare(self):
    from cbuild.util import cargo

    self.cargo = cargo.Cargo(self)
    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENSE-MIT")
