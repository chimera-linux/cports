pkgname = "rust-analyzer"
pkgver = "2026.04.20"
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
sha256 = "972a5ab7337bd07c3e35daf48ccfc0cc17ea214008718a6949157fafdead7707"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
