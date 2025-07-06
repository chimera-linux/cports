pkgname = "efivar"
pkgver = "39"
pkgrel = 0
build_style = "makefile"
make_build_target = "all"
make_build_args = ["libdir=/usr/lib", "ERRORS="]
make_install_args = ["libdir=/usr/lib"]
make_check_target = "test"
hostmakedepends = ["mandoc", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Tools and libraries to work with EFI variables"
license = "LGPL-2.1-or-later"
url = "https://github.com/rhboot/efivar"
# source = f"{url}/releases/download/{pkgver}/efivar-{pkgver}.tar.bz2"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c9edd15f2eeeea63232f3e669a48e992c7be9aff57ee22672ac31f5eca1609a6"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE", "-D_FILE_OFFSET_BITS=64"]}


def init_build(self):
    self.make_build_args += [
        "HOSTCC=" + self.get_tool("CC", target="host"),
        "HOST_CFLAGS=" + self.get_cflags(target="host", shell=True),
        "HOST_LDFLAGS=" + self.get_ldflags(target="host", shell=True),
    ]
    self.make_check_args += self.make_build_args
    self.make_install_args += self.make_install_args


@subpackage("efivar-libs")
def _(self):
    self.renames = ["libefivar"]

    return self.default_libs()


@subpackage("efivar-devel")
def _(self):
    return self.default_devel()
