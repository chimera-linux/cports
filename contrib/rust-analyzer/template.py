pkgname = "rust-analyzer"
pkgver = "2024.07.01"
pkgrel = 0
build_style = "cargo"
make_env = {"CARGO_PROFILE_RELEASE_PANIC": "unwind"}
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Rust compiler LSP server"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-lang/rust-analyzer"
source = f"{url}/archive/refs/tags/{pkgver.replace('.', '-')}.tar.gz"
sha256 = "6b5eafbc1d105c2823a960c29f4f69c1ddb898da547bcbd0097022967887cf8a"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def do_install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
