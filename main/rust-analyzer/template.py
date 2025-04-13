pkgname = "rust-analyzer"
pkgver = "2025.04.07"
_pver = pkgver.replace(".", "-")
pkgrel = 0
build_style = "cargo"
make_env = {
    "CARGO_PROFILE_RELEASE_PANIC": "unwind",
    "CFG_RELEASE": _pver,
}
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["rust-src"]
pkgdesc = "Rust compiler LSP server"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-lang/rust-analyzer"
source = f"{url}/archive/refs/tags/{_pver}.tar.gz"
sha256 = "03f59db9cbb35962e3d850401e23bbe853d73b4d24850e2e0345f31044605fbf"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
