pkgname = "karchive"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
# fails with zlib-ng equality on comp data
make_check_args = ["-E", "kfiltertest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "zstd-devel",
]
pkgdesc = "Qt6 addon providing access to numerous types of archives"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://develop.kde.org/docs/features/karchive"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/karchive-{pkgver}.tar.xz"
sha256 = "246ad8dd2b5fb83df1cb05ff1fd3934f8a52be94d124350f9e6b7c3420e9c474"
hardening = ["vis"]


@subpackage("karchive-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
