pkgname = "ethtool"
pkgver = "7.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/ethtool-{pkgver}.tar.xz"
sha256 = "660bf9725a7871343a0d232068a7634fbcfb69b6c2f8eff455827faefb0cd162"
# FIXME int
hardening = ["vis", "cfi", "!int"]
