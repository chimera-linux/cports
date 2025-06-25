pkgname = "libblockdev"
pkgver = "3.3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # TODO: volume_key
    "--without-escrow",
]
hostmakedepends = ["bash", "pkgconf", "python", "automake", "libtool"]
makedepends = [
    "cryptsetup-devel",
    "e2fsprogs-devel",
    "glib-devel",
    "json-glib-devel",
    "keyutils-devel",
    "kmod-devel",
    "libatasmart-devel",
    "libbytesize-devel",
    "libnvme-devel",
    "libyaml-devel",
    "linux-headers",
    "lvm2-devel",
    "ndctl-devel",
    "parted-devel",
    "pcre2-devel",
    "util-linux-fdisk-devel",
]
pkgdesc = "Library for manipulating block devices"
license = "LGPL-2.1-or-later"
url = "https://github.com/storaged-project/libblockdev"
source = f"{url}/releases/download/{pkgver}/libblockdev-{pkgver}.tar.gz"
sha256 = "a2e2e448a19d420480b8cce5e0752197482a65cb62a9ed55d88b237da36600d1"

tool_flags = {
    "CFLAGS": ["-Wno-error=typedef-redefinition", "-Wno-error=unused-variable"]
}


@subpackage("libblockdev-devel")
def _(self):
    return self.default_devel()
