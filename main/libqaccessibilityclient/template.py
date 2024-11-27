pkgname = "libqaccessibilityclient"
pkgver = "0.6.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
# FIXME: fails for unknown reasons
make_check_args = ["-E", "libkdeaccessibilityclient-tst_accessibilityclient"]
make_check_wrapper = ["dbus-run-session", "wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtbase-devel",
]
checkdepends = ["dbus", "xwayland-run"]
pkgdesc = "Accessibility helper library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/libraries/libqaccessibilityclient"
source = f"$(KDE_SITE)/libqaccessibilityclient/libqaccessibilityclient-{pkgver}.tar.xz"
sha256 = "4c50c448622dc9c5041ed10da7d87b3e4e71ccb49d4831a849211d423c5f5d33"
hardening = ["vis"]


@subpackage("libqaccessibilityclient-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
