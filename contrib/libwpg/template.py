pkgname = "libwpg"
pkgver = "0.3.4"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["librevenge-devel", "boost-devel", "libwpd-devel"]
pkgdesc = "Library for importing WordPerfect graphics"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://libwpg.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b55fda9440d1e070630eb2487d8b8697cf412c214a27caee9df69cec7c004de3"


@subpackage("libwpg-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libwpg-devel")
def _devel(self):
    return self.default_devel()
