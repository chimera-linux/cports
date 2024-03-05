pkgname = "python-maturin"
pkgver = "1.5.0"
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
sha256 = "19eacc3befa15ff6302ef08951ed1a0516f5edea5ef1fae7f98fd8bd669610ff"
# yeah no
options = ["!check"]


def do_prepare(self):
    from cbuild.util import cargo

    self.cargo = cargo.Cargo(self)
    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("license-mit")
