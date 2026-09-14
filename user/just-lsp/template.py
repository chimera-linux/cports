pkgname = "just-lsp"
pkgver = "0.8.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Language server for just"
license = "CC0-1.0"
url = "https://terror.github.io/just-lsp"
source = f"https://github.com/terror/just-lsp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b4d4122b8698f47cb80912d274d1abcf00af1a93d7d84cc2f0d84e8f32596782"


def prepare(self):
    # "vendor" dir already exists for a different purpose
    self.cargo.vendor(["vendored-crates"])


def post_install(self):
    self.install_license("LICENSE")
