pkgname = "xfce4-notes-plugin"
pkgver = "1.11.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "slibtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "gtk+3-devel",
    "gtksourceview4-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce notes panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-notes-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-notes-plugin/{pkgver[:-2]}/xfce4-notes-plugin-{pkgver}.tar.bz2"
sha256 = "ef410999c9dafc5cf13fdcfd62ae49728508c0d37510f006971d5291061524aa"
