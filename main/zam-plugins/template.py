pkgname = "zam-plugins"
pkgver = "4.3"
pkgrel = 0
build_style = "makefile"
make_build_args = ["CLANG=true"]
hostmakedepends = [
    "bash",
    "pkgconf",
]
makedepends = [
    "fftw-devel",
    "ladspa-sdk",
    "liblo-devel",
    "libsamplerate-devel",
    "lv2",
    "mesa-devel",
    "pipewire-jack-devel",
    "zita-convolver-devel",
]
pkgdesc = "Collection of audio plugins for high-quality audio processing"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/zamaudio/zam-plugins"
_dpf = "077fcf5758ed6038bfe6e7aee1e407aa02e807b2"
_pugl = "e33b2f6b0cea6d6263990aa9abe6a69fdfba5973"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/DISTRHO/DPF/archive/{_dpf}.tar.gz",
    f"https://github.com/DISTRHO/pugl/archive/{_pugl}.tar.gz",
]
source_paths = [
    ".",
    "dpf",
    "dpf/dgl/src/pugl-upstream",
]
sha256 = [
    "5c681e2830f1f5400364a4a5c7df72c95a3a5e81aa82c87a4cbf387511752857",
    "c4e8ca5ef8637dc9c6fdaa7ac88eee8227c46d91cf30f781b79e1b471fced50c",
    "7e813d35d619a0ba3e790be5e102cfd2dc7c1f7b99333c9aa0a8661ca8419e02",
]
hardening = ["vis", "!cfi"]
# no tests
options = ["!check", "linkundefver"]


@subpackage("zam-plugins-clap")
def _(self):
    return ["usr/lib/clap"]


@subpackage("zam-plugins-ladspa")
def _(self):
    return ["usr/lib/ladspa"]


@subpackage("zam-plugins-lv2")
def _(self):
    return ["usr/lib/lv2"]


@subpackage("zam-plugins-vst2")
def _(self):
    return ["usr/lib/vst"]


@subpackage("zam-plugins-vst3")
def _(self):
    return ["usr/lib/vst3"]
