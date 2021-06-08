pkgname = "gmp"
version = "6.2.1"
revision = 1
bootstrap = True
build_style = "gnu_configure"
configure_args = ["--enable-cxx"]
hostmakedepends = ["m4"]
makedepends = ["zlib-devel"]
short_desc = "Library for arbitrary precision arithmetic"
maintainer = "Orphaned <orphan@voidlinux.org>"
license = "LGPL-3.0-or-later"
homepage = "http://gmplib.org/"
distfiles = [f"https://gmplib.org/download/gmp/gmp-{version}.tar.xz"]
checksum = ["fd4829912cddd12f84181c3451cc752be224643e87fac497b69edddadc49b4f2"]

@subpackage("gmpxx")
def _gmpxx(self):
    self.short_desc = short_desc + " - C++ support"

    def install():
        self.take("usr/lib/libgmpxx.so.*")

    return install

@subpackage("gmpxx-devel")
def _develxx(self):
    self.short_desc = short_desc + " - C++ development files"
    self.depends = [
        f"gmp-devel-{version}_{revision}", f"gmpxx-{version}_{revision}"
    ]

    def install():
        self.take("usr/include/gmpxx.h")
        self.take("usr/lib/libgmpxx.a")
        self.take("usr/lib/libgmpxx.so")
        self.take("usr/lib/pkgconfig/gmpxx.pc")

    return install

@subpackage("gmp-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [f"gmp-{version}_{revision}"]

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")
        self.take("usr/lib/pkgconfig")
        self.take("usr/share")

    return install
