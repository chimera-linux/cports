pkgname = "lsp-plugins"
pkgver = "1.2.22"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gst-plugins-base-devel",
    "ladspa-sdk",
    "libsndfile-devel",
    "libxrandr-devel",
    "lv2",
    "mesa-devel",
    "pipewire-jack-devel",
]
pkgdesc = "Collection of free audio plugins"
license = "LGPL-3.0-or-later"
url = "https://lsp-plug.in"
source = f"https://github.com/sadko4u/lsp-plugins/releases/download/{pkgver}/lsp-plugins-src-{pkgver}.tar.gz"
sha256 = "bb97270482b04c1269643a8373b554255dde287b1c5ddbc567ac94de4815a75b"
hardening = ["vis", "!cfi"]
# no tests
# cross broken because of dumb uname arch detection
options = ["!check", "!cross"]

if self.profile().arch == "ppc":
    broken = "segfaults during build"


def configure(self):
    # disabling docs makes it not require php
    self.make.invoke(
        "config",
        ["ARTIFACT_EXPORT_HEADERS=1", "SUB_FEATURES=doc", "PREFIX=/usr"],
    )


@subpackage("lsp-plugins-devel")
def _(self):
    return self.default_devel()


@subpackage("lsp-plugins-xdg")
def _(self):
    self.subdesc = "icons and .desktop files"
    # these hundreds of .desktop files only really clutter launchers,
    # so place them separately
    return [
        "etc/xdg/menus",
        "usr/share/applications",
        "usr/share/desktop-directories",
        "usr/share/icons",
    ]


@subpackage("lsp-plugins-clap")
def _(self):
    self.subdesc = "clap plugins"
    return ["usr/lib/clap"]


@subpackage("lsp-plugins-lv2")
def _(self):
    self.subdesc = "lv2 plugins"
    return ["usr/lib/lv2"]


@subpackage("lsp-plugins-vst2")
def _(self):
    self.subdesc = "vst2 plugins"
    return ["usr/lib/vst"]


@subpackage("lsp-plugins-vst3")
def _(self):
    self.subdesc = "vst3 plugins"
    return ["usr/lib/vst3"]


@subpackage("lsp-plugins-gstreamer")
def _(self):
    self.subdesc = "gstreamer plugins"
    return [
        "usr/lib/gstreamer-1.0",
        "usr/lib/lsp-plugins/liblsp-plugins-gstreamer-*.so",
    ]


@subpackage("lsp-plugins-ladspa")
def _(self):
    self.subdesc = "ladspa plugins"
    return ["usr/lib/ladspa"]
