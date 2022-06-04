pkgname = "cbindgen"
pkgver = "0.23.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust"]
pkgdesc = "Tool to generate C bindings for Rust code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d7b82a7a4bfe7fc61c6f7c1b848bf586fef4057c84960739484b4f743bf0bab6"
# only expected to work with rust nightly
options = ["!check"]
