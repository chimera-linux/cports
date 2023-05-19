pkgname = "cdparanoia"
pkgver = "10.2"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
# messy build system
make_dir = "."
make_check_target = "test"
hostmakedepends = ["gmake", "pkgconf", "automake", "libtool"]
makedepends = ["linux-headers"]
pkgdesc = "CDDA reading utility with extra data verification features"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-only"
url = "https://www.xiph.org/paranoia"
source = f"https://downloads.xiph.org/releases/{pkgname}/{pkgname}-III-{pkgver}.src.tgz"
sha256 = "005db45ef4ee017f5c32ec124f913a0546e77014266c6a1c50df902a55fe64df"
tool_flags = {"CFLAGS": ["-Du_int16_t=uint16_t", "-Du_int32_t=uint32_t"]}
# missing target in some place?
options = ["!check", "!parallel"]

@subpackage("libcdparanoia")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("cdparanoia-devel")
def _devel(self):
    return self.default_devel()
