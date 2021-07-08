pkgname = "acl"
version = "2.3.1"
revision = 0
bootstrap = True
build_style = "gnu_configure"
configure_args = [
    f"--libdir=/usr/lib",
    f"--libexecdir=/usr/lib"
]
makedepends = ["attr-devel"]
short_desc = "Access Control List filesystem support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
homepage = "https://savannah.nongnu.org/projects/acl"

from cbuild import sites

distfiles = [f"{sites.nongnu}/acl/acl-{version}.tar.gz"]
checksum = ["760c61c68901b37fdd5eefeeaf4c0c7a26bdfdd8ac747a1edff1ce0e243c11af"]

def pre_configure(self):
    if not self.bootstrapping:
        return

    from cbuild.core import paths

    self.CFLAGS.append("-I" + str(paths.masterdir() / "usr/include"))
    self.LDFLAGS.append("-L" + str(paths.masterdir() / "usr/lib"))

@subpackage("acl-devel")
def _devel(self):
    self.depends = ["attr-devel", f"{pkgname}={version}-r{revision}"]
    self.short_desc = short_desc + " - development files"

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")
        self.take("usr/lib/pkgconfig")
        self.take("usr/share/man/man[235]")
        self.take("usr/share/doc")

    return install

@subpackage("acl-progs")
def _progs(self):
    self.short_desc = short_desc + " - utilities"

    def install():
        self.take("usr/bin")
        self.take("usr/share")

    return install
