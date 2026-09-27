pkgname = "ragel"
pkgver = "6.11"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Finite state machine compiler"
license = "GPL-2.0-or-later"
url = "https://www.colm.net/open-source/ragel/index.html"
source = f"https://www.colm.net/files/ragel/ragel-{pkgver}.tar.gz"
sha256 = "47653e376554adbb617d2f1da15394b6a163264e2410c2bff3581347a14890e3"
tool_flags = {"CXXFLAGS": ["-std=gnu++98"]}
# tests need txl which is not open source http://www.txl.ca/
options = ["!check"]
