pkgname = "kfilemetadata"
pkgver = "6.28.0"
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
url = "https://api.kde.org/frameworks/kfilemetadata/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kfilemetadata-{pkgver}.tar.xz"
sha256 = "015be4aa6986642d3f13903b47c1aae7183d3218888dc4353afe1b1e9dd64c1e"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("kfilemetadata-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
