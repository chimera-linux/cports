pkgname = "debugedit"
pkgver = "5.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "bash", "help2man", "pkgconf"]
makedepends = ["elfutils-devel", "musl-bsd-headers"]
pkgdesc = "Utilities for creating debuginfo and source file distributions"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later AND LGPL-2.0-or-later"
url = "https://sourceware.org/debugedit"
source = (
    f"https://sourceware.org/pub/debugedit/{pkgver}/debugedit-{pkgver}.tar.xz"
)
sha256 = "e9ecd7d350bebae1f178ce6776ca19a648b6fe8fa22f5b3044b38d7899aa553e"
# CFI: check
hardening = ["vis", "!cfi"]
# check: most of them fail (TODO)
# cross: tries to run built binary to generate manpage
options = ["!check", "!cross"]
