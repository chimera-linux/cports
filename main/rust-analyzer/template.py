pkgname = "rust-analyzer"
pkgver = "2025.12.22"
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
sha256 = "d65c0edd42d3f1c658bcd02c1d6555cb187c91ffceb4f83508047008831fdb12"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
