pkgname = "testdisk"
pkgver = "7.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "e2fsprogs-devel",
    "libjpeg-turbo-devel",
    "ncurses-devel",
    "ntfs-3g-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Data recovery suite"
license = "GPL-2.0-or-later"
url = "https://www.cgsecurity.org"
source = f"{url}/testdisk-{pkgver}.tar.bz2"
sha256 = "f8343be20cb4001c5d91a2e3bcd918398f00ae6d8310894a5a9f2feb813c283f"
