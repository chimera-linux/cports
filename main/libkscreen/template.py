pkgname = "libkscreen"
pkgver = "6.2.4"
pkgrel = 1
build_style = "cmake"
# testbackendloader testEnv(xrandr 1.1) 'preferred.fileName().startsWith(backend)' returned FALSE, flaky tests when parallel
make_check_args = ["-E", "testbackendloader", "-j1"]
# kscreen-testqscreenbackend needs X11
make_check_wrapper = ["xwfb-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "plasma-wayland-protocols",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h/qtguiglobal_p.h
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
]
checkdepends = [
    "dbus-x11",
    "hwdata",
    "xwayland-run",
]
# depends = ["jq"] for zsh completions to work at their full capacity
pkgdesc = "KDE screen management library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = (
    "LGPL-2.1-or-later AND GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)"
)
url = "https://invent.kde.org/plasma/libkscreen"
source = f"$(KDE_SITE)/plasma/{pkgver}/libkscreen-{pkgver}.tar.xz"
sha256 = "3cc06d5c561ab4dbedbc548a4655119e861c4ac29e565ff5846273f0c76e9cb4"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("libkscreen-devel")
def _(self):
    return self.default_devel()
