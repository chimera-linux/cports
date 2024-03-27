pkgname = "libblockdev"
pkgver = "3.1.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # TODO: volume_key
    "--without-escrow",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "bash", "pkgconf", "python", "automake", "libtool"]
makedepends = [
    "cryptsetup-devel",
    "device-mapper-devel",
    "e2fsprogs-devel",
    "glib-devel",
    "keyutils-devel",
    "libbytesize-devel",
    "libfdisk-devel",
    "libkmod-devel",
    "libnvme-devel",
    "linux-headers",
    "ndctl-devel",
    "parted-devel",
    "pcre2-devel",
]
pkgdesc = "Library for manipulating block devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/storaged-project/libblockdev"
source = f"{url}/releases/download/{pkgver}-1/{pkgname}-{pkgver}.tar.gz"
sha256 = "a5cb33a53ff5969067982704f45399d02555fdb2313ed0c56eac9555397dc2db"

tool_flags = {
    "CFLAGS": ["-Wno-error=typedef-redefinition", "-Wno-error=unused-variable"]
}


@subpackage("libblockdev-devel")
def _devel(self):
    return self.default_devel()
