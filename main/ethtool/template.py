pkgname = "ethtool"
pkgver = "6.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5eaa083e8108e1dd3876b2c803a1942a2763942715b7f6eb916e189adbb44972"
# FIXME int
hardening = ["vis", "cfi", "!int"]
