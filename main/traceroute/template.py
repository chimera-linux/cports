pkgname = "traceroute"
pkgver = "2.1.3"
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
sha256 = "05ebc7aba28a9100f9bbae54ceecbf75c82ccf46bdfce8b5d64806459a7e0412"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
hardening = ["vis", "cfi"]
# no tests
options = ["!cross", "!check"]
