pkgname = "efivar"
pkgver = "37"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "all"
make_build_args = ["libdir=/usr/lib", "ERRORS="]
make_install_args = ["libdir=/usr/lib"]
make_check_target = "test"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["linux-headers"]
pkgdesc = "Tools and libraries to work with EFI variables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/rhboot/efivar"
source = f"{url}/releases/download/{pkgver}/efivar-{pkgver}.tar.bz2"
sha256 = "3c67feb93f901b98fbb897d5ca82931a6698b5bcd6ac34f0815f670d77747b9f"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE", "-D_FILE_OFFSET_BITS=64"]}


@subpackage("libefivar")
def _lib(self):
    self.subdesc = "runtime library"
    return self.default_libs()


@subpackage("efivar-devel")
def _devel(self):
    return self.default_devel()
