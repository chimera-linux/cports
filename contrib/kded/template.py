pkgname = "kded"
pkgver = "6.2.0"
pkgrel = 1
build_style = "cmake"
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
    "kdoctools-devel",
    "kservice-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Extensible central daemon of KDE workspaces"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kded/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kded-{pkgver}.tar.xz"
)
sha256 = "ca6d6971b661b5142ede6ab9a1acbe24d4085efbc9f13988c179649b1261ab4f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)


@subpackage("kded-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
