pkgname = "python-rpds-py"
pkgver = "0.22.3"
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
sha256 = "e32fee8ab45d3c2db6da19a5323bc3362237c8b653c70194414b892fd06a080d"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def post_install(self):
    self.install_license("LICENSE")
