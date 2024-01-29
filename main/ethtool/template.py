pkgname = "ethtool"
pkgver = "6.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c3ae526b01ce4d8df6c794ab170de4a4104d111ea8d8db3f1fd7c25fcb905619"
# FIXME int
hardening = ["vis", "cfi", "!int"]
