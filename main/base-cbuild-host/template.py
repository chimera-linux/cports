pkgname = "base-cbuild-host"
pkgver = "0.1"
pkgrel = 2
build_style = "meta"
depends = [
    "apk-tools",
    "openssl3",
    "git",
    "bubblewrap",
    "chimerautils",
    "python",
]
pkgdesc = "Everything one needs to use cbuild and cports"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
