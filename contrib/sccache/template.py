pkgname = "sccache"
pkgver = "0.8.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "openssl-devel",
    "zstd-devel",
]
pkgdesc = "Compilation caching tool with Rust support"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/mozilla/sccache"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "30b951b49246d5ca7d614e5712215cb5f39509d6f899641f511fb19036b5c4e5"
# fails due to comparing ldd output to a glibc bin
options = ["!check"]
