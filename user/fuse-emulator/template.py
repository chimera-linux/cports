pkgname = "fuse-emulator"
pkgver = "1.6.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-desktop-integration",
    "--with-gtk",
    "--verbose",
]
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool", "perl"]
makedepends = [
    "alsa-lib-devel",
    "audiofile-devel",
    "glib-devel",
    "gtk+3-devel",
    "libgcrypt-devel",
    "libpng-devel",
    "libspectrum-devel",
    "libxml2-devel",
    "linux-headers",
    "sdl2-compat-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Free Unix Spectrum Emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://fuse-emulator.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/fuse-emulator/fuse-{pkgver}.tar.gz"
sha256 = "3a8fedf2ffe947c571561bac55a59adad4c59338f74e449b7e7a67d9ca047096"
