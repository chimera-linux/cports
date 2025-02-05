pkgname = "monolith"
pkgver = "2.8.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "CLI tool for saving complete web pages as a single HTML file"
maintainer = "Sudan <sudanchapagain@proton.me>"
license = "CC0-1.0"
url = "https://github.com/Y2Z/monolith"
source = f"{url}/archive/v{pkgver}/monolith-{pkgver}.tar.gz"
sha256 = "51769e6505d5708ac296e5d93e280c9fefa7873452d471c5106aaeb7c3667f9f"
