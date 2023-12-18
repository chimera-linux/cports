pkgname = "traceroute"
pkgver = "2.1.4"
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
sha256 = "b2e39a1d04ea45a6a60c976a2637d1a16224edd2eaa19a5870af83edb2ffe3fa"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
hardening = ["vis", "cfi"]
# no tests
options = ["!cross", "!check"]
