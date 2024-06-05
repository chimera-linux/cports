pkgname = "python-maturin"
pkgver = "1.6.0"
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
sha256 = "10809d4df85532cb70d9f186117cac8b2d2fa9b03c8f2fb53a8dc8a531f5afeb"
# yeah no
options = ["!check"]


def do_prepare(self):
    from cbuild.util import cargo

    self.cargo = cargo.Cargo(self)
    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("license-mit")
