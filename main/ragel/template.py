pkgname = "ragel"
pkgver = "6.10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Finite state machine compiler"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "GPL-2.0-or-later"
url = "https://www.colm.net/open-source/ragel/index.html"
source = f"https://www.colm.net/files/ragel/ragel-{pkgver}.tar.gz"
sha256 = "5f156edb65d20b856d638dd9ee2dfb43285914d9aa2b6ec779dac0270cd56c3f"
tool_flags = {"CXXFLAGS": ["-std=gnu++98"]}
# tests need txl which is not open source http://www.txl.ca/
options = ["!check"]
