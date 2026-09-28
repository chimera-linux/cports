# run testsuites for python-cffi and gjs on all archs on updates
pkgname = "libffi8"
pkgver = "3.5.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--includedir=/usr/include",
    "--disable-multi-os-directory",
    "--with-pic",
    # https://github.com/libffi/libffi/pull/647
    # some stuff (notably gobject-introspection) uses
    # libffi incorrectly, prevent them from being broken for now
    "--disable-exec-static-tramp",
]
# regen causes lost symvers which is a build abi break
#
# correct:
#
# $ nm -D /usr/lib/libffi.so.8.1.4|grep ffi_type_double
# 0000000000001558 R ffi_type_double@@LIBFFI_BASE_8.0
#
# bad:
#
# 0000000000001568 R ffi_type_double
#
configure_gen = []
hostmakedepends = ["pkgconf"]
# actually only on x86 and arm (tramp.c code) but it does not hurt
makedepends = ["linux-headers"]
pkgdesc = "Library supporting Foreign Function Interfaces"
license = "MIT"
url = "http://sourceware.org/libffi"
source = f"https://github.com/libffi/libffi/releases/download/v{pkgver}/libffi-{pkgver}.tar.gz"
sha256 = "f3a3082a23b37c293a4fcd1053147b371f2ff91fa7ea1b2a52e335676bac82dc"
# dejagnu
options = ["!check", "linkundefver"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libffi8-devel")
def _(self):
    self.provides = [self.with_pkgver("libffi-devel")]

    return self.default_devel(extra=["usr/share/info"])
