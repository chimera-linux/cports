pkgname = "mdbook"
pkgver = "0.4.48"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = (
    "Create book from markdown files. Like Gitbook but implemented in Rust"
)
license = "MPL-2.0"
url = "https://rust-lang.github.io/mdBook"
source = (
    f"https://github.com/rust-lang/mdBook/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "65021ceca2a2f5a1ceda243953ce764bf34c466b7a83db38e167a2b7d1131dcf"
