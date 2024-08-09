pkgname = "ethtool"
pkgver = "6.10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/ethtool-{pkgver}.tar.xz"
sha256 = "cc613fe8a2bcddee17a1e6e0d763c0f3ea33c7e930658d2d7f601aa65e426a1f"
# FIXME int
hardening = ["vis", "cfi", "!int"]
