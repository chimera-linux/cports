pkgname = "ethtool"
pkgver = "6.19"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/ethtool-{pkgver}.tar.xz"
sha256 = "1c2114ab6e0c0d2aa67d699960eb11df4f341e2403139cdf28ae9da858a6025f"
# FIXME int
hardening = ["vis", "cfi", "!int"]
