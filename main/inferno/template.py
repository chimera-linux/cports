pkgname = "inferno"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Stack trace visualizer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "CDDL-1.0"
url = "https://github.com/jonhoo/inferno"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7c045ad20db6284b0f1312a60e13438723bc6273e49ca2544000027794638396"
# some tests need an actual git checkout of a submodule (not tarball) and i cbf
options = ["!check"]
