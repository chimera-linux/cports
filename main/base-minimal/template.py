pkgname = "base-minimal"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "base-bootstrap", "base-shells", "apk-tools", "bsdutils-extra", "bsddiff",
    "bsded", "bsdgzip", "bsdtar", "util-linux", "shadow", "procps-ng",
    "iana-etc", "tzdata", "dinit-chimera"
]
pkgdesc = "Minimal set of packages for a Chimera system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
