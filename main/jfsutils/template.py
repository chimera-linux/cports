pkgname = "jfsutils"
pkgver = "1.1.15"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
]
makedepends = ["util-linux-uuid-devel"]
pkgdesc = "JFS filesystem utilities"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://jfs.sourceforge.net"
source = f"{url}/project/pub/jfsutils-{pkgver}.tar.gz"
sha256 = "244a15f64015ce3ea17e49bdf6e1a0fb4f9af92b82fa9e05aa64cb30b5f07a4d"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
