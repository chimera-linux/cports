pkgname = "fuse-emulator"
pkgver = "1.5.7"
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
    "sdl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Free Unix Spectrum Emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://fuse-emulator.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/fuse-emulator/fuse-{pkgver}.tar.gz"
sha256 = "f0e2583f2642cdc3b2a737910d24e289d46e4f7e151805e3b0827024b2b45e4d"
