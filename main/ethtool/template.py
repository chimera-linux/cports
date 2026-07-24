pkgname = "ethtool"
pkgver = "7.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/ethtool-{pkgver}.tar.xz"
sha256 = "4d78c26edc0255bc92f4b995b5fd66108d75ff966ed4694f6025a6d370bc2496"
# FIXME int
hardening = ["vis", "cfi", "!int"]
