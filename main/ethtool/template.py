pkgname = "ethtool"
pkgver = "6.14"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/ethtool-{pkgver}.tar.xz"
sha256 = "9338bb00e492878d3bbe3cd2894e60db35813634c208db0b20f5c7ee84da69b1"
# FIXME int
hardening = ["vis", "cfi", "!int"]
