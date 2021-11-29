pkgname = "traceroute"
pkgver = "2.1.0"
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
sha256 = "3669d22a34d3f38ed50caba18cd525ba55c5c00d5465f2d20d7472e5d81603b6"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# no tests
options = ["!cross", "!check", "lto"]
