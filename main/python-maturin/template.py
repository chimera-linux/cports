pkgname = "python-maturin"
pkgver = "1.8.2"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {
    "MATURIN_SETUP_ARGS": "--features=full,native-tls,password-storage"
}
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools-rust",
    "python-wheel",
]
makedepends = ["rust-std", "openssl3-devel"]
checkdepends = ["pytest"]
depends = ["python"]
pkgdesc = "Tool for building and publishing Rust-based Python packages"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 OR MIT"
url = "https://www.maturin.rs"
source = f"https://github.com/PyO3/maturin/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "204f22de5c56a3d599f427344e7389270d71ea183bcc0c719c3725931459180b"
# yeah no
options = ["!check"]


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_license("license-mit")
