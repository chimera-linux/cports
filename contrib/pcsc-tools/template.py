pkgname = "pcsc-tools"
pkgver = "1.7.1"
pkgrel = 1
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "gmake",
    "pkgconf",
]
makedepends = ["pcsc-lite-devel"]
depends = [
    "pcsc-perl",
    # TODO: perl-gtk3
    "perl-glib",
    "perl-libintl-perl",
]
pkgdesc = "Tools for PCSC"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://pcsc-tools.apdu.fr"
source = f"{url}/pcsc-tools-{pkgver}.tar.bz2"
sha256 = "0d024b589e15d79eac8506cd67df7b53cf91e9e6a493c8319f33cd29b5f36426"
