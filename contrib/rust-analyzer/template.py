pkgname = "rust-analyzer"
pkgver = "2023.10.30"
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
sha256 = "3944a14569164efd2c0548d90afae3f892cda23ef9fc5378fbb4d0b2b3269ec2"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def do_install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
