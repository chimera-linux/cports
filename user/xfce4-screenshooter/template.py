pkgname = "xfce4-screenshooter"
pkgver = "1.11.2"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "help2man",
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "exo-devel",
    "gtk+3-devel",
    "libx11-devel",
    "libxext-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxfixes-devel",
    "libxi-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce screenshot app"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-screenshooter/start"
source = f"$(XFCE_SITE)/apps/xfce4-screenshooter/{'.'.join(pkgver.split('.')[:-1])}/xfce4-screenshooter-{pkgver}.tar.xz"
sha256 = "6ae5bc4823d43e770b3a11700d048d56bdcaafdef37de7deacb8970b55fc1565"
# Tries to run built executable to generate manpage
options = ["!cross"]
