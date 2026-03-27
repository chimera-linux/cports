pkgname = "inferno"
pkgver = "0.12.6"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Stack trace visualizer"
license = "CDDL-1.0"
url = "https://github.com/jonhoo/inferno"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4b0e22ae5e701f6de8fdfbf13ddac501b421f4db6e527c296222fd885e68bcd5"
# some tests need an actual git checkout of a submodule (not tarball) and i cbf
options = ["!check"]
