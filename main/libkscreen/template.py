pkgname = "libkscreen"
pkgver = "6.4.4"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
# testbackendloader testEnv(xrandr 1.1) 'preferred.fileName().startsWith(backend)' returned FALSE, flaky tests when parallel
make_check_args = ["-E", "testbackendloader", "-j1"]
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
sha256 = "dc9fee7a8334c24b4f94c33d9f31b093c13cd8fb7de06314e8edfa3a28cab4f6"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("libkscreen-devel")
def _(self):
    return self.default_devel()
