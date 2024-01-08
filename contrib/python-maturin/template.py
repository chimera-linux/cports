pkgname = "python-maturin"
pkgver = "1.4.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {
    "MATURIN_SETUP_ARGS": "--features=full,native-tls,password-storage"
}
hostmakedepends = [
    "cargo",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools-rust",
    "python-wheel",
]
makedepends = ["rust-std", "openssl-devel"]
checkdepends = ["pytest"]
depends = ["python-tomli"]
pkgdesc = "Tool for building and publishing Rust-based Python packages"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "Apache-2.0 OR MIT"
url = "https://www.maturin.rs"
source = f"https://github.com/PyO3/maturin/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cd2cd3d465619bb997b41594398310e8b257d0c17854a58ca0598efa11e6d698"
# yeah no
options = ["!check"]


def post_patch(self):
    from cbuild.util import cargo

    self.cargo = cargo.Cargo(self)
    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("license-mit")
