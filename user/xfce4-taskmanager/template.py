pkgname = "xfce4-taskmanager"
pkgver = "1.6.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "gtk+3-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxmu-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce task manager"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-taskmanager/start"
source = f"$(XFCE_SITE)/apps/xfce4-taskmanager/{pkgver[:-2]}/xfce4-taskmanager-{pkgver}.tar.xz"
sha256 = "29bdc7840ab8b9025f6c0e456a83a31090d1c9fd9e26b359baa4a4010cfb0b90"
