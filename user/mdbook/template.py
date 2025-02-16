pkgname = "mdbook"
pkgver = "0.4.44"
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
sha256 = "af801a377aec2e671e6c6fe5ed3043c3e8cab674cbaa0a2faed36b8b6987ce10"
