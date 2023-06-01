pkgname = "cbindgen"
pkgver = "0.24.6"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust"]
pkgdesc = "Tool to generate C bindings for Rust code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "af0591e687128f7fb4300b0fe24c6091f24593d3a8acadf4fe860bd82c20c4c5"
# only expected to work with rust nightly
options = ["!check"]
