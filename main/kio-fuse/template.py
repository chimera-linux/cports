pkgname = "kio-fuse"
pkgver = "5.1.1"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DBUILD_WITH_QT6=ON", "-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "fuse-devel",
    "kcoreaddons-devel",
    "kio-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE KIO fuse interface"
license = "GPL-3.0-or-later"
url = "https://invent.kde.org/system/kio-fuse"
source = f"$(KDE_SITE)/kio-fuse/kio-fuse-{pkgver}.tar.xz"
sha256 = "adf6aa7ce055c0987e716a93ac01f3c0a97c1280421443cd6b21e0e71d763d14"
hardening = ["vis"]
# needs real fuse mounted
options = ["!check"]


def post_install(self):
    # TODO: port to dinit user instead
    self.install_file("^/kio-fuse.desktop", "etc/xdg/autostart")
    self.uninstall("usr/lib/systemd/user")
    self.install_file(
        "^/modules-load.conf",
        "usr/lib/modules-load.d",
        name="kio-fuse.conf",
    )
