pkgname = "hotspot"
pkgver = "1.5.1"
pkgrel = 2
build_style = "cmake"
configure_args = ["-DQT6_BUILD=ON"]
# broken when building out of tree as testdata isn't found relatively
# the rest seem to be flaky in some way?
make_check_args = ["-E", "(tst_perfdata|tst_models|tst_disassemblyoutput)"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "elfutils-devel",
    "karchive-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kddockwidgets-devel",
    "kgraphviewer-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kitemviews-devel",
    "knotifications-devel",
    "kparts-devel",
    "kwindowsystem-devel",
    "qcustomplot-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "rustc-demangle-devel",
    "solid-devel",
    "syntax-highlighting-devel",
    "threadweaver-devel",
    "zstd-devel",
]
depends = [
    # gobjdump invocation for disassembly
    f"binutils-{self.profile().arch}",
    # graph kpart for callgraph
    "kgraphviewer",
    # konsole kpart for the embedded terminal that shows command output
    "konsole",
    # dlopened
    "rustc-demangle-libs",
]
checkdepends = [*depends]
pkgdesc = "Linux perf GUI for performance analysis"
license = "GPL-2.0-or-later"
url = "https://github.com/KDAB/hotspot"
source = [
    f"{url}/releases/download/v{pkgver}/hotspot-v{pkgver}.tar.gz",
    f"{url}/releases/download/v{pkgver}/hotspot-perfparser-v{pkgver}.tar.gz",
    f"{url}/releases/download/v{pkgver}/hotspot-PrefixTickLabels-v{pkgver}.tar.gz",
]
source_paths = [
    ".",
    "3rdparty/perfparser",
    "3rdparty/PrefixTickLabels",
]
sha256 = [
    "f0a611d8ed6e7c5038fb11176f047eb4fd4a670355750f154cddf015818a4087",
    "84f7014655a1cbbf751f2a6d965d33f0f99235b763dd1a768c5e2326304b069d",
    "9e25e61104bdbe73ccde056db920303ef8cf1ac632f3365e0bd099cc7fee71a1",
]
# see below
options = []


if self.profile().arch != "x86_64":
    # disas tests rely on specific matching string output, so it doesn't match
    # on other architectures
    options += ["!check"]
