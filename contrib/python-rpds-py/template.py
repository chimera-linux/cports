pkgname = "python-rpds-py"
pkgver = "0.19.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "python-build",
    "python-installer",
    "python-maturin",
]
makedepends = ["rust-std"]
checkdepends = [
    "python-iniconfig",
    "python-packaging",
    "python-pluggy",
    "python-pytest",
]
depends = ["python"]
pkgdesc = "Python bindings to the Rust rpds crate"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/crate-py/rpds"
source = f"$(PYPI_SITE)/r/rpds-py/rpds_py-{pkgver}.tar.gz"
sha256 = "4fdc9afadbeb393b4bbbad75481e0ea78e4469f2e1d713a90811700830b553a9"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENSE")
