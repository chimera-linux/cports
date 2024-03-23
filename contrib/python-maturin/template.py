pkgname = "python-maturin"
pkgver = "1.5.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 OR MIT"
url = "https://www.maturin.rs"
source = f"https://github.com/PyO3/maturin/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "18198cc9421d04933586b9730abcdd80fe3484e209d2b8223aa7dc1f12c4c3fe"
# yeah no
options = ["!check"]


def do_prepare(self):
    from cbuild.util import cargo

    self.cargo = cargo.Cargo(self)
    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("license-mit")
