pkgname = "ethtool"
pkgver = "6.15"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/ethtool-{pkgver}.tar.xz"
sha256 = "9477c365114d910120aaec5336a1d16196c833d8486f7c6da67bedef57880ade"
# FIXME int
hardening = ["vis", "cfi", "!int"]
