pkgname = "lsp-plugins"
pkgver = "1.2.15"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_use_env = True
hostmakedepends = [
    "gmake",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "ladspa-sdk",
    "libsndfile-devel",
    "libxrandr-devel",
    "lv2",
    "mesa-devel",
    "pipewire-jack-devel",
]
pkgdesc = "Collection of free audio plugins"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later"
url = "https://lsp-plug.in"
source = f"https://github.com/sadko4u/lsp-plugins/releases/download/{pkgver}/lsp-plugins-src-{pkgver}.tar.gz"
sha256 = "92b92efa31463af2f08b134677ed2307313fd7b93f394d3301e3cb867c5df3ae"
# FIXME cfi
hardening = ["vis", "!cfi"]
# no tests
# cross broken because of dumb uname arch detection
options = ["!check", "!cross"]


def do_configure(self):
    # disabling docs makes it not require php
    self.make.invoke(
        "config",
        ["ARTIFACT_EXPORT_HEADERS=1", "SUB_FEATURES=doc", "PREFIX=/usr"],
    )


@subpackage("lsp-plugins-devel")
def _devel(self):
    return self.default_devel()


@subpackage("lsp-plugins-xdg")
def _xdg(self):
    self.pkgdesc = f"{pkgdesc} (icons and .desktop files)"
    # these hundreds of .desktop files only really clutter launchers,
    # so place them separately
    return [
        "etc/xdg/menus",
        "usr/share/applications",
        "usr/share/desktop-directories",
        "usr/share/icons",
    ]


@subpackage("lsp-plugins-clap")
def _clap(self):
    self.pkgdesc = f"{pkgdesc} (clap plugins)"
    return ["usr/lib/clap"]


@subpackage("lsp-plugins-lv2")
def _lv2(self):
    self.pkgdesc = f"{pkgdesc} (lv2 plugins)"
    return ["usr/lib/lv2"]


@subpackage("lsp-plugins-vst2")
def _vst2(self):
    self.pkgdesc = f"{pkgdesc} (vst2 plugins)"
    return ["usr/lib/vst"]


@subpackage("lsp-plugins-ladspa")
def _ladspa(self):
    self.pkgdesc = f"{pkgdesc} (ladspa plugins)"
    return ["usr/lib/ladspa"]
