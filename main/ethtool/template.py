pkgname = "ethtool"
pkgver = "6.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d9425f0a3df138734001fccc4175fe178c025f938460ac25c4ebc39960168822"
# FIXME int
hardening = ["vis", "cfi", "!int"]
