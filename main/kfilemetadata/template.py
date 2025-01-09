pkgname = "kfilemetadata"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
# since 6.9 testMetadataSize() depends on fs specifics and fails on bldroot under f2fs/tmpfs
make_check_args = ["-E", "usermetadatawritertest"]
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
    "taglib-devel",
]
pkgdesc = "KDE framework for file metadata"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kfilemetadata/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kfilemetadata-{pkgver}.tar.xz"
sha256 = "d17b692ea7ac0d9baecb1dce3aa10a562db3a9ae7e92dc2b9dc6044dfa11dc0b"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("kfilemetadata-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
