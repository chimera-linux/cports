pkgname = "libburn"
pkgver = "1.5.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Library for reading, mastering and writing optical discs"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://dev.lovelyhq.com/libburnia/libburn"
source = f"http://files.libburnia-project.org/releases/libburn-{pkgver}.tar.gz"
sha256 = "7295491b4be5eeac5e7a3fb2067e236e2955ffdc6bbd45f546466edee321644b"


@subpackage("libburn-devel")
def _(self):
    return self.default_devel()
