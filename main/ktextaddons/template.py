pkgname = "ktextaddons"
pkgver = "1.7.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
make_check_args = [
    "-E",
    "(texttospeechwidgettest"  # hangs
    + "|texttospeechactionstest"  # fail in headless
    + "|grammalecteresultwidgettest"
    + "|grammalecteconfigwidgettest"
    + "|languagetoolconfigwidgettest"
    + "|texttospeechactionstest"  # need translator plugins
    + "|translatorwidgettest"
    + "|translatorengineloadertest"
    + ")",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "karchive-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "ktextwidgets-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtspeech-devel",
    "qt6-qttools-devel",
    "qtkeychain-devel",
    "sonnet-devel",
    "syntax-highlighting-devel",
]
pkgdesc = "KDE text handling addons library"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/libraries/ktextaddons"
source = f"$(KDE_SITE)/ktextaddons/ktextaddons-{pkgver}.tar.xz"
sha256 = "90cf25e298e095c40b3286a7153d04f961ef4e6598321bdeb00f2be7e998ae7e"


@subpackage("ktextaddons-devel")
def _(self):
    self.depends += ["kconfigwidgets-devel"]
    return self.default_devel()
