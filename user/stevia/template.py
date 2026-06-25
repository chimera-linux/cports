pkgname = "stevia"
pkgver = "0.51.0"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "elogind-devel",
    "feedbackd-devel",
    "glib-devel",
    "gmobile-devel",
    "gnome-desktop-devel",
    "hunspell-devel",
    "libhandy-devel",
    "wayland-devel",
    "wayland-protocols",
]
checkdepends = ["xwayland-run"]
provides = ["phosh-keyboard=0"]
pkgdesc = "Phosh OSK"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/Phosh/stevia"
source = f"https://sources.phosh.mobi/releases/phosh-osk-stevia/phosh-osk-stevia-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "85b7e94509f7619bf0c693b27b1c39bdb109a967f76aac582a44c545c04ec7e2"
# assertion 'GDK_IS_SEAT (seat)' failed (same as in main/libhandy)
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
