pkgname = "rust-analyzer"
pkgver = "2023.08.14"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust"]
pkgdesc = "Rust compiler LSP server"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-lang/rust-analyzer"
source = f"{url}/archive/refs/tags/{pkgver.replace('.', '-')}.tar.gz"
sha256 = "3fa6d28ece1f8952c29a375aab41e50502d20c8a9c0c5f1e44a9576d8f635224"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def do_install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
