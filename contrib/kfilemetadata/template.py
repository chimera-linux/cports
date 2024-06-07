pkgname = "kfilemetadata"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
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
    "poppler-qt-devel",
    "qt6-qtdeclarative-devel",
    "taglib-devel",
]
pkgdesc = "KDE framework for file metadata"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kfilemetadata/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kfilemetadata-{pkgver}.tar.xz"
sha256 = "bd88e378861a03ada99c69841a81fceefd3dd220145007fbfe9113270b7d6088"
# FIXME: cfi breaks at least indexextractortest/dump_fulltext
hardening = ["vis", "!cfi"]
# TODO
options = ["!cross"]


@subpackage("kfilemetadata-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
