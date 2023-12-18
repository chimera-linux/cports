pkgname = "traceroute"
pkgver = "2.1.5"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["prefix=/usr"]
make_install_args = ["prefix=/usr"]
hostmakedepends = ["gmake"]
makedepends = ["linux-headers"]
pkgdesc = "Traces the route taken by packets over an IPv4/IPv6 network"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://traceroute.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "9c6c260d96eaab51e3ce461b0a84fe87123ebc6dd6c9a59fab803f95b35a859e"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
hardening = ["vis", "cfi"]
# no tests
options = ["!cross", "!check"]
