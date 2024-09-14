pkgname = "ext4magic"
pkgver = "0.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-expert-mode",
    "--enable-file-attr",
]
hostmakedepends = ["automake", "libtool"]
makedepends = [
    "bzip2-devel",
    "e2fsprogs-devel",
    "file-devel",
    "linux-headers",
    "zlib-ng-compat-devel",
]
pkgdesc = "Ext4 recovery utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/ext4magic"
source = f"$(SOURCEFORGE_SITE)/ext4magic/ext4magic-{pkgver}.tar.gz"
sha256 = "8d9c6a594f212aecf4eb5410d277caeaea3adc03d35378257dfd017ef20ea115"
tool_flags = {"CFLAGS": ["-DHAVE_SYS_TYPES_H"]}
# no tests and from looking at the code, implicitly untrusted
hardening = ["!int"]
