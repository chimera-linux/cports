pkgname = "base-minimal"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "chimerautils", "base-shells", "apk-tools", "awk",
    "bsdtar", "util-linux", "shadow", "procps-ng",
    "iana-etc", "tzdata", "dinit-chimera", "chimera-repo-main",
]
pkgdesc = "Minimal set of packages for a Chimera system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
