pkgname = "ethtool"
pkgver = "6.11"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/ethtool-{pkgver}.tar.xz"
sha256 = "8d91f5c72ae3f25b7e88d4781279dcb320f71e30058914370b1c574c96b31202"
# FIXME int
hardening = ["vis", "cfi", "!int"]
