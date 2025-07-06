pkgname = "python-rpds-py"
pkgver = "0.26.0"
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
license = "MIT"
url = "https://github.com/crate-py/rpds"
source = f"$(PYPI_SITE)/r/rpds-py/rpds_py-{pkgver}.tar.gz"
sha256 = "20dae58a859b0906f0685642e591056f1e787f3a8b39c8e8749a45dc7d26bdb0"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def post_install(self):
    self.install_license("LICENSE")
