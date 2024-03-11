pkgname = "rust-analyzer"
pkgver = "2024.03.11"
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
sha256 = "31df3464840a79ad9303a2df9abb12f46d555e210112e80faa5ab665a8fb7202"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def do_install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
