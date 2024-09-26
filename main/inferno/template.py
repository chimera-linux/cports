pkgname = "inferno"
pkgver = "0.11.21"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Stack trace visualizer"
maintainer = "psykose <alice@ayaya.dev>"
license = "CDDL-1.0"
url = "https://github.com/jonhoo/inferno"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8650bcb44715ecf83b00d36ed0e28e8b6c1f11d9de8e25a54554d72c0d67dc87"
# some tests need an actual git checkout of a submodule (not tarball) and i cbf
options = ["!check"]
