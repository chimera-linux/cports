pkgname = "gtklock"
pkgver = "4.0.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["glib-devel", "meson", "pkgconf", "scdoc"]
makedepends = [
    "gtk+3-devel",
    "gtk-session-lock-devel",
    "linux-pam-devel",
]
pkgdesc = "GTK-based lockscreen for Wayland"
license = "GPL-3.0-or-later"
url = "https://github.com/jovanlanik/gtklock"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "db20bf27bd5dd01901ea1753c89c170777dd7cf8fca19130cf90f5f4e3fb9633"


def post_install(self):
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
    self.install_files("assets/", "usr/share/gtklock")
