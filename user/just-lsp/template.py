pkgname = "just-lsp"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Language server for just"
license = "CC0-1.0"
url = "https://terror.github.io/just-lsp"
source = f"https://github.com/terror/just-lsp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b9fc878286b054b630c48e458f09f47dfb4cf6047cae2636225ab66a378b8773"


def prepare(self):
    # "vendor" dir already exists for a different purpose
    self.cargo.vendor(["vendored-crates"])


def post_install(self):
    self.install_license("LICENSE")
