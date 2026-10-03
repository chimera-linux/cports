pkgname = "libkscreen"
pkgver = "6.7.91"
pkgrel = 0
build_style = "cmake"
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
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/libkscreen-{pkgver}.tar.xz"
sha256 = "f2123be8232752b8a0434405ea047a4bf120108a4fc5c6867c925748609f9eb8"
# traps on some setups?
# https://github.com/chimera-linux/cports/issues/4960
hardening = ["!int"]


@subpackage("libkscreen-devel")
def _(self):
    return self.default_devel()
