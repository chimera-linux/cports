pkgname = "ethtool"
pkgver = "6.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "814171ea4b8026b081c0741dbbf32e6968311483ecf64711232faec2ac70a14c"
# FIXME int
hardening = ["vis", "cfi", "!int"]
