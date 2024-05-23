pkgname = "ethtool"
pkgver = "6.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a71b0354010661c5cf178bc606ed50fcb91805cf1897ad0eb2818387a5fd0cd9"
# FIXME int
hardening = ["vis", "cfi", "!int"]
