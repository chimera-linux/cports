pkgname = "gavl"
pkgver = "1.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-doxygen"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Audiovisual library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gmerlin.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/gmerlin/gavl-{pkgver}.tar.gz"
sha256 = "51aaac41391a915bd9bad07710957424b046410a276e7deaff24a870929d33ce"
# funrolls loooops xDD
tool_flags = {"CFLAGS": ["-Wno-ignored-optimization-argument"]}


@subpackage("gavl-devel")
def _(self):
    return self.default_devel()
