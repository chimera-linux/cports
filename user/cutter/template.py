pkgname = "cutter"
pkgver = "2.3.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # default is usr/share but we don't put bins there
    "-DCUTTER_EXTRA_PLUGIN_DIRS=/usr/lib/cutter/plugins",
    "-DCUTTER_ENABLE_GRAPHVIZ=ON",
    "-DCUTTER_ENABLE_PYTHON=ON",
    "-DCUTTER_USE_ADDITIONAL_RIZIN_PATHS=OFF",
    "-DCUTTER_USE_BUNDLED_RIZIN=OFF",
    "-DCUTTER_QT6=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "graphviz-devel",
    "python-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "rizin-devel",
]
pkgdesc = "Reverse engineering UI built on Rizin"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-only"
url = "https://cutter.re"
source = f"https://github.com/rizinorg/cutter/releases/download/v{pkgver}/Cutter-v{pkgver}-src.tar.gz"
sha256 = "edc266a5f7a1f1c7f71cf5c6c9727e05008b728eae3bb42beb7d0b24ce07c5c3"
tool_flags = {"CXXFLAGS": ["-DNDEBUG"]}


@subpackage("cutter-devel")
def _(self):
    self.depends = [
        self.parent,
        "qt6-qt5compat-devel",
        "qt6-qtbase-devel",
        "qt6-qtsvg-devel",
        "rizin-devel",
    ]
    return self.default_devel()
