pkgname = "inferno"
pkgver = "0.12.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Stack trace visualizer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "CDDL-1.0"
url = "https://github.com/jonhoo/inferno"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "913145c6087a5dd24c8ca976c079309a4fdd15983e392b1dbd13b8658daceb57"
# some tests need an actual git checkout of a submodule (not tarball) and i cbf
options = ["!check"]
