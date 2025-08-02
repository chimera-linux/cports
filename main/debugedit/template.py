pkgname = "debugedit"
pkgver = "5.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "bash", "help2man", "pkgconf"]
makedepends = ["elfutils-devel", "musl-bsd-headers", "xxhash-devel"]
pkgdesc = "Utilities for creating debuginfo and source file distributions"
license = "GPL-3.0-or-later AND LGPL-2.0-or-later"
url = "https://sourceware.org/debugedit"
source = (
    f"https://sourceware.org/pub/debugedit/{pkgver}/debugedit-{pkgver}.tar.xz"
)
sha256 = "705296803cc4403f38764e891b4ed38f8d8d4f8a9164bd4f86c9d4bedcac68dd"
# CFI: check
hardening = ["vis", "!cfi"]
# check: most of them fail (TODO)
# cross: tries to run built binary to generate manpage
options = ["!check", "!cross"]
