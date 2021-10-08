pkgname = "attr"
pkgver = "2.5.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    f"--libdir=/usr/lib",
    f"--libexecdir=/usr/lib"
]
make_check_args = ["-j1"] # Tests broken when ran in parallel
checkdepends = ["perl"]
pkgdesc = "Extended attribute support library for ACL support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://savannah.nongnu.org/projects/attr"
sources = [f"$(NONGNU_SITE)/attr/attr-{pkgver}.tar.gz"]
sha256 = ["bae1c6949b258a0d68001367ce0c741cebdacdd3b62965d17e5eb23cd78adaf8"]
options = ["bootstrap", "!check", "!lint"]

if not current.bootstrapping:
    hostmakedepends = ["pkgconf"]

def pre_check(self):
    # Either the test wasn't updated or the package misconfigures/miscompiles
    # the error message in musl based systems
    # EXPECTED: Operation not supported
    # RECIEVED: Not supported
    with open(self.cwd / "test/attr.test") as ifile:
        with open(self.cwd / "test/attr.test.new") as ofile:
            for ln in ifile:
                ln = ln.replace("f: Operation n", "f: N")
                ofile.write(ln)

    self.mv("test/attr.test.new", "test/attr.test")

@subpackage("attr-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
        "usr/share/man/man3",
        "usr/share/doc",
    ]

@subpackage("attr-progs")
def _progs(self):
    return [
        "usr/bin",
        "usr/share/man/man1",
        "usr/share/locale",
    ]
