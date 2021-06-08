pkgname = "gdbm"
version = "1.19"
revision = 1
build_style = "gnu_configure"
configure_args = ["--enable-libgdbm-compat", "--disable-rpath"]
short_desc = "GNU database routines"
maintainer = "Orphaned <orphan@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "http://www.gnu.org.ua/software/gdbm/"

from cbuild import sites

distfiles = [f"{sites.gnu}/{pkgname}/{pkgname}-{version}.tar.gz"]
checksum = ["37ed12214122b972e18a0d94995039e57748191939ef74115b1d41d8811364bc"]

CFLAGS = ["-fcommon"]

def post_install(self):
    self.install_dir("usr/include/gdbm")
    self.install_link("../gdbm.h", "usr/include/gdbm/gdbm.h")
    self.install_link("../ndbm.h", "usr/include/gdbm/ndbm.h")
    self.install_link("../dbm.h", "usr/include/gdbm/dbm.h")

@subpackage("gdbm-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [f"gdbm>={version}_{revision}"]

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")
        self.take("usr/share/info")
        self.take("usr/share/man/man3")

    return install
