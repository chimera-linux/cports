pkgname = "traceroute"
pkgver = "2.1.6"
pkgrel = 0
build_style = "makefile"
make_build_args = ["prefix=/usr"]
make_install_args = ["prefix=/usr"]
makedepends = ["linux-headers"]
pkgdesc = "Traces the route taken by packets over an IPv4/IPv6 network"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://traceroute.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/traceroute/traceroute-{pkgver}.tar.gz"
sha256 = "9ccef9cdb9d7a98ff7fbf93f79ebd0e48881664b525c4b232a0fcec7dcb9db5e"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
hardening = ["vis", "cfi"]
# no tests
options = ["!cross", "!check"]
