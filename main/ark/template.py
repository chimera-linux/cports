pkgname = "ark"
pkgver = "25.08.1"
pkgrel = 0
build_style = "cmake"
# kerfuffle-extracttest: needs arj/unar etc
# kerfuffle-loadtest: fails to open some archives
make_check_args = ["-E", "(kerfuffle-extracttest|)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "breeze-icons-devel",
    "kconfig-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kfilemetadata-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kparts-devel",
    "kpty-devel",
    "kservice-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libarchive-devel",
    "libzip-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["7zip", "xwayland-run", "zstd"]
pkgdesc = "KDE archive manager"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ark"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ark-{pkgver}.tar.xz"
sha256 = "2febbab11881e3d32f44c4107041d53b1d5353c8c95c4d6536ab57de0958f96f"


@subpackage("ark-computils")
def _(self):
    self.subdesc = "default de/compression utilities"
    self.install_if = [self.parent]
    self.depends = [
        "7zip",
        # TODO: missing deps
        # there's also arj/lzop but seems pointless
        # "lrzip",
        # "unar",
        # "unrar",
        # "unzip",  # pointless with 7z (in code), also it uses libzip anyway?
        "zstd",
    ]
    self.options = ["empty"]
    return []
