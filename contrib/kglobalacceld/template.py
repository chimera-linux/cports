pkgname = "kglobalacceld"
pkgver = "6.0.5"
pkgrel = 1
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "kio-devel",
    "kservice-devel",
    "kwindowsystem-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Daemon for global keyboard shortcut functionality"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/kglobalacceld"
source = f"$(KDE_SITE)/plasma/{pkgver}/kglobalacceld-{pkgver}.tar.xz"
sha256 = "2c9b391c0e3f91bb8b320029c7b97fc8166658882106d1df9ad441600894fcae"
# FIXME: cfi breaks at least 50+ kwin tests (together with kidletime)
hardening = ["vis", "!cfi"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)


@subpackage("kglobalacceld-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
