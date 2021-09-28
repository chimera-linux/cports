pkgname = "acl"
version = "2.3.1"
revision = 0
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
sources = [f"$(NONGNU_SITE)/acl/acl-{version}.tar.gz"]
sha256 = ["760c61c68901b37fdd5eefeeaf4c0c7a26bdfdd8ac747a1edff1ce0e243c11af"]
options = ["bootstrap", "!check"]

@subpackage("acl-devel")
def _devel(self):
    self.depends = ["attr-devel", f"{pkgname}={version}-r{revision}"]
    self.short_desc = short_desc + " - development files"

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
        "usr/share/man/man[235]",
        "usr/share/doc"
    ]

@subpackage("acl-progs")
def _progs(self):
    self.short_desc = short_desc + " - utilities"

    return [
        "usr/bin",
        "usr/share"
    ]
