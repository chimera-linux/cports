pkgname = "python-rpds-py"
pkgver = "0.27.0"
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
sha256 = "8b23cf252f180cda89220b378d917180f29d313cd6a07b2431c0d3b776aae86f"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def post_install(self):
    self.install_license("LICENSE")
