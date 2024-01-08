pkgname = "python-rpds-py"
pkgver = "0.16.2"
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
pkgdesc = (
    "Python bindings to the Rust rpds crate for persistent data structures"
)
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/crate-py/rpds"
source = f"$(PYPI_SITE)/r/rpds-py/rpds_py-{pkgver}.tar.gz"
sha256 = "781ef8bfc091b19960fc0142a23aedadafa826bc32b433fdfe6fd7f964d7ef44"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENSE")
