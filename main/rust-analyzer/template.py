pkgname = "rust-analyzer"
pkgver = "2026.04.13"
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
sha256 = "501ffe115c7fea3e151af9dbee37d1a8f6a873b530722deb12dea297ed89d43b"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
