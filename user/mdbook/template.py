pkgname = "mdbook"
pkgver = "0.4.45"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
pkgdesc = (
    "Create book from markdown files. Like Gitbook but implemented in Rust"
)
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "MPL-2.0"
url = "https://rust-lang.github.io/mdBook"
source = (
    f"https://github.com/rust-lang/mdBook/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "bba66446316de17cdaea918b195ee7420bf3259746b196d4a5e0eda4d9612122"
