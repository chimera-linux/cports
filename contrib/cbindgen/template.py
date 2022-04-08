pkgname = "cbindgen"
pkgver = "0.21.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust"]
pkgdesc = "Tool to generate C bindings for Rust code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "c254a68039a85fe17c63781e67d09b0bfabc32446615d7c63cd805052ac5b155"
# only expected to work with rust nightly
options = ["!check"]
