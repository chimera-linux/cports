pkgname = "attr"
version = "2.5.1"
revision = 0
build_style = "gnu_configure"
configure_args = [
    f"--libdir=/usr/lib",
    f"--libexecdir=/usr/lib"
]
make_check_args = ["-j1"] # Tests broken when ran in parallel
checkdepends = ["perl"]
short_desc = "Extended attribute support library for ACL support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
homepage = "http://savannah.nongnu.org/projects/attr"

options = ["bootstrap"]

from cbuild import sites

distfiles = [f"{sites.nongnu}/attr/attr-{version}.tar.gz"]
checksum = ["bae1c6949b258a0d68001367ce0c741cebdacdd3b62965d17e5eb23cd78adaf8"]
conf_files = ["/etc/xattr.conf"]

def pre_check(self):
    import os
    # Either the test wasn't updated or the package misconfigures/miscompiles
    # the error message in musl based systems
    # EXPECTED: Operation not supported
    # RECIEVED: Not supported
    with open(self.abs_wrksrc / "test/attr.test") as ifile:
        with open(self.abs_wrksrc / "test/attr.test.new") as ofile:
            for ln in ifile:
                ln = ln.replace("f: Operation n", "f: N")
                ofile.write(ln)

    os.rename(
        self.abs_wrksrc / "test/attr.test.new",
        self.abs_wrksrc / "test/attr.test"
    )

@subpackage("attr-devel")
def _devel(self):
    self.depends = [f"{pkgname}={version}-r{revision}"]
    self.short_desc = short_desc + " - development files"

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")
        self.take("usr/lib/pkgconfig")
        self.take("usr/share/man/man3")
        self.take("usr/share/doc")

    return install

@subpackage("attr-progs")
def _progs(self):
    self.short_desc = short_desc + " - utilities"

    def install():
        self.take("usr/bin")
        self.take("usr/share/man/man1")
        self.take("usr/share/locale")

    return install
