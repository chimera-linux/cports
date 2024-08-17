pkgname = "kakoune-lsp"
pkgver = "17.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Kakoune language server protocol client"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT OR Unlicense"
url = "https://github.com/kakoune-lsp/kakoune-lsp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2a7c83eb1eb7e0e119879ee9be9b0868c07028c4925c317a78e7f2bbe8dc7d0f"


def post_install(self):
    self.install_license("MIT")
