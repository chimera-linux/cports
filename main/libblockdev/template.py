pkgname = "libblockdev"
pkgver = "2.26"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # TODO: ndctl
    "--without-escrow", "--without-nvdimm",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "bash", "pkgconf", "python"]
makedepends = [
    "cryptsetup-devel", "device-mapper-devel", "dmraid-devel",
    "libbytesize-devel", "libglib-devel", "libkmod-devel",
    "libyaml-devel", "parted-devel", "pcre2-devel", "linux-headers"
]
pkgdesc = "Library for manipulating block devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/storaged-project/libblockdev"
source = f"https://github.com/storaged-project/{pkgname}/releases/download/{pkgver}-1/{pkgname}-{pkgver}.tar.gz"
sha256 = "c4c0e10b35ac632bda8ce6d200b5601184984dec387fe59185921eb42432e069"

@subpackage("libblockdev-devel")
def _devel(self):
    return self.default_devel()
