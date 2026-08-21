pkgname = "kfilemetadata"
pkgver = "6.29.0"
pkgrel = 0
build_style = "cmake"
# since 6.9 testMetadataSize() depends on fs specifics and fails on bldroot under f2fs/tmpfs
make_check_args = ["-E", "usermetadatawritertest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "attr-devel",
    "ebook-tools-devel",
    "exiv2-devel",
    "ffmpeg-devel",
    "karchive-devel",
    "kcodecs-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdegraphics-mobipocket-devel",
    "ki18n-devel",
    "libepubgen-devel",
    "poppler-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "taglib-devel",
]
pkgdesc = "KDE framework for file metadata"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kfilemetadata-{pkgver}.tar.xz"
sha256 = "c8a4bbbb3e6876caa9357a151afbd66e06336f7a4a27b54a94497cf4cafa96ac"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("kfilemetadata-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
