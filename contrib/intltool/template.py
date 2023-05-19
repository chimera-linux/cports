pkgname = "intltool"
pkgver = "0.51.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "perl-xml-parser"]
makedepends = ["perl-xml-parser", "gettext-tiny"]
depends = ["file"] + makedepends
pkgdesc = "Internationalization tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://edge.launchpad.net/intltool"
source = f"http://launchpad.net/intltool/trunk/{pkgver}/+download/{pkgname}-{pkgver}.tar.gz"
sha256 = "67c74d94196b153b774ab9f89b2fa6c6ba79352407037c8c14d5aeb334e959cd"

configure_gen = []
