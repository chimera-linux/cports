pkgname = "libisofs"
pkgver = "1.5.6.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
# TODO: libjte (if it's actually worth it)
makedepends = ["acl-devel", "zlib-ng-compat-devel"]
pkgdesc = "Library to create ISO 9660 images"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://dev.lovelyhq.com/libburnia/libisofs"
source = f"http://files.libburnia-project.org/releases/libisofs-{pkgver[:-2]}.pl0{pkgver[-1]}.tar.gz"
sha256 = "ac1fd338d641744ca1fb1567917188b79bc8c2506832dd56885fec98656b9f25"


@subpackage("libisofs-devel")
def _(self):
    return self.default_devel()
