pkgname = "ethtool"
pkgver = "6.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d5446c93de570ce68f3b1ea69dbfa12fcfd67fc19897f655d3f18231e2b818d6"

# FIXME visibility
hardening = ["!vis"]
