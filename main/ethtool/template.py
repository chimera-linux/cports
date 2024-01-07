pkgname = "ethtool"
pkgver = "6.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "833a8493cb9cd5809ab59743092d9a38742c282290800e9626407511bbcebf9e"
# FIXME int
hardening = ["vis", "cfi", "!int"]
