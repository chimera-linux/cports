pkgname = "rust-analyzer"
pkgver = "2024.01.15"
pkgrel = 0
build_style = "cargo"
make_env = {"CARGO_PROFILE_RELEASE_PANIC": "unwind"}
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "Rust compiler LSP server"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-lang/rust-analyzer"
source = f"{url}/archive/refs/tags/{pkgver.replace('.', '-')}.tar.gz"
sha256 = "d1bf6864d7d711c879744da8d142fdc083da722118412d7e3b3cde6c662695b8"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def do_install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
