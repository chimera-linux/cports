pkgname = "base-minimal"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "base-bootstrap", "dinit-chimera", "nyagetty", "bsdtar",
    "shadow", "procps-ng",
]
pkgdesc = "Minimal set of packages for a bootable Chimera system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
