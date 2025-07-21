pkgname = "gnome-disk-utility"
pkgver = "46.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dlogind=libelogind"]
hostmakedepends = [
    "desktop-file-utils",
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "elogind-devel",
    "glib-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libdvdread-devel",
    "libhandy-devel",
    "libnotify-devel",
    "libpwquality-devel",
    "libsecret-devel",
    "udisks-devel",
    "xz-devel",
]
depends = ["udisks"]
pkgdesc = "GNOME disk drive and media management"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Disks"
source = f"$(GNOME_SITE)/gnome-disk-utility/{pkgver[:-2]}/gnome-disk-utility-{pkgver}.tar.xz"
sha256 = "c24e9439a04d70bcfae349ca134c7005435fe2b6f452114df878bff0b89bbffe"
