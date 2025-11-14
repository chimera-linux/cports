pkgname = "libkscreen"
pkgver = "6.5.2"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
# testbackendloader testEnv(xrandr 1.1) 'preferred.fileName().startsWith(backend)' returned FALSE, flaky tests when parallel
# testqscreenbackend & testinprocess broken (even on upstream CI) since v6.5.0 / e394a4c ("Drop QScreen backend")
make_check_args = ["-E", "test(backendloader|qscreenbackend|inprocess)", "-j1"]
# kscreen-testqscreenbackend needs X11
make_check_wrapper = ["xwfb-run", "--"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "plasma-wayland-protocols",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h/qtguiglobal_p.h
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
]
checkdepends = ["dbus-x11", "hwdata", "xwayland-run"]
# depends = ["jq"] for zsh completions to work at their full capacity
pkgdesc = "KDE screen management library"
license = (
    "LGPL-2.1-or-later AND GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)"
)
url = "https://invent.kde.org/plasma/libkscreen"
source = f"$(KDE_SITE)/plasma/{pkgver}/libkscreen-{pkgver}.tar.xz"
sha256 = "28099754348a7d3af74d79b443d7fde8e6a2b32c6e5491b520180d65d1e1ba61"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("libkscreen-devel")
def _(self):
    return self.default_devel()
