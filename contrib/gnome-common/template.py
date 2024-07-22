pkgname = "gnome-common"
pkgver = "3.18.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-autoconf-archive"]
hostmakedepends = ["automake"]
depends = ["automake"]
pkgdesc = "Common scripts and macros to develop with GNOME"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "GPL-2.0-only"
url = "https://www.gnome.org"
source = (
    f"$(GNOME_SITE)/gnome-common/{pkgver[:-2]}/gnome-common-{pkgver}.tar.xz"
)
sha256 = "22569e370ae755e04527b76328befc4c73b62bfd4a572499fde116b8318af8cf"
hardening = ["vis"]
