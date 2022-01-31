pkgname = "cbindgen"
pkgver = "0.20.0"
pkgrel = 0
build_style = "cargo"
# TODO: maybe cargo should depend on ca-certificates
hostmakedepends = ["cargo", "ca-certificates"]
makedepends = ["rust"]
pkgdesc = "Tool to generate C bindings for Rust code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "70f810d2b9e5a2db570431872c26377813fb27a63d817cb16b2d69fa3741d066"
# only expected to work with rust nightly
options = ["!check"]
