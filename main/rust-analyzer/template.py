pkgname = "rust-analyzer"
pkgver = "2025.02.10"
pkgrel = 0
build_style = "cargo"
make_env = {"CARGO_PROFILE_RELEASE_PANIC": "unwind"}
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["rust-src"]
pkgdesc = "Rust compiler LSP server"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-lang/rust-analyzer"
source = f"{url}/archive/refs/tags/{pkgver.replace('.', '-')}.tar.gz"
sha256 = "6f5815ff1ae29c9097e3e6054d60763ad5e520095b9709ecec088812757d65fe"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
