pkgname = "cbindgen"
pkgver = "0.25.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust"]
pkgdesc = "Tool to generate C bindings for Rust code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "363ac6317a5788de8f2b0104a472a747883d4b9126fa119c681879509dbdbc28"
# only expected to work with rust nightly
options = ["!check"]
