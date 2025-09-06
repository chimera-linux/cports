pkgname = "kfilemetadata"
pkgver = "6.17.0"
pkgrel = 1
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
url = "https://api.kde.org/frameworks/kfilemetadata/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kfilemetadata-{pkgver}.tar.xz"
sha256 = "2bb9a99846ab0f73636ec34fba244908a123591f7f7458bab91b8cfb23923044"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("kfilemetadata-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
