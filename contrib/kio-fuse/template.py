pkgname = "kio-fuse"
pkgver = "5.1.0"
pkgrel = 2
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://invent.kde.org/system/kio-fuse"
source = f"$(KDE_SITE)/kio-fuse/kio-fuse-{pkgver}.tar.xz"
sha256 = "7d104581227d5a19b424b33f4168d181556b1015d6df2218e01a88d64449e94b"
# CFI: check
hardening = ["vis", "!cfi"]
# needs real fuse mounted
options = ["!check"]


def post_install(self):
    # TODO: port to dinit user instead
    self.install_file(self.files_path / "kio-fuse.desktop", "etc/xdg/autostart")
    self.uninstall("usr/lib/systemd/user")
    self.install_file(
        self.files_path / "modules-load.conf",
        "usr/lib/modules-load.d",
        name="kio-fuse.conf",
    )
