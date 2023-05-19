pkgname = "ethtool"
pkgver = "6.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "86df0114064d4d73f6bf72bf03e85c33964a519ee0c1d1ba65005ad2d0e570e1"
# FIXME int
hardening = ["vis", "cfi", "!int"]

configure_gen = []
