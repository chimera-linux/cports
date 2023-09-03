pkgname = "libblockdev"
pkgver = "3.0.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # TODO: ndctl
    "--without-escrow",
    "--without-nvdimm",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "bash", "pkgconf", "python", "automake", "libtool"]
makedepends = [
    "cryptsetup-devel",
    "device-mapper-devel",
    "libbytesize-devel",
    "glib-devel",
    "keyutils-devel",
    "libkmod-devel",
    "libnvme-devel",
    "parted-devel",
    "pcre2-devel",
    "libfdisk-devel",
    "e2fsprogs-devel",
    "linux-headers",
]
pkgdesc = "Library for manipulating block devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/storaged-project/libblockdev"
source = f"https://github.com/storaged-project/{pkgname}/releases/download/{pkgver}-1/{pkgname}-{pkgver}.tar.gz"
sha256 = "0f2872830293f3e222832903d80de4c38e06a9c3ea18915b3263272a72095ea8"

tool_flags = {
    "CFLAGS": ["-Wno-error=typedef-redefinition", "-Wno-error=unused-variable"]
}


@subpackage("libblockdev-devel")
def _devel(self):
    return self.default_devel()
