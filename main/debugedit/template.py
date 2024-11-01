pkgname = "debugedit"
pkgver = "5.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "bash", "help2man", "pkgconf"]
makedepends = ["elfutils-devel", "musl-bsd-headers", "xxhash-devel"]
pkgdesc = "Utilities for creating debuginfo and source file distributions"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later AND LGPL-2.0-or-later"
url = "https://sourceware.org/debugedit"
source = (
    f"https://sourceware.org/pub/debugedit/{pkgver}/debugedit-{pkgver}.tar.xz"
)
sha256 = "ee9b688b2ed8fa62551c54cb5dc31aaa05853e7dedbd9e1237c77894ea5e3626"
# CFI: check
hardening = ["vis", "!cfi"]
# check: most of them fail (TODO)
# cross: tries to run built binary to generate manpage
options = ["!check", "!cross"]
