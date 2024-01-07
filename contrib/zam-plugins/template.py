pkgname = "zam-plugins"
pkgver = "4.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["CLANG=true"]
hostmakedepends = [
    "bash",
    "gmake",
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/zamaudio/zam-plugins"
_dpf = "63dfb7610bc37dee69f4a303f3e3362529d95f24"
_pugl = "2e98e220b5b860c1c8cd5809fad61baf27380a37"
source = [
    f"https://github.com/zamaudio/zam-plugins/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/DISTRHO/DPF/archive/{_dpf}.tar.gz",
    f"https://github.com/DISTRHO/pugl/archive/{_pugl}.tar.gz",
]
source_paths = [
    ".",
    "dpf",
    "dpf/dgl/src/pugl-upstream",
]
sha256 = [
    "d39fa1d6c279acdae075eb789d53803707e0d7116fcc7b12a0638e2f4866dbc1",
    "499a2d27f935931cdef7e5b14e13b42adcd783cdc4e9eb13598be59570461877",
    "7bd49fec34c39d1381c22eb8a1eed20332c104ded414b8d7b4779c5cdf112fbc",
]
# FIXME: cfi
hardening = ["vis"]
# no tests
options = ["!check", "linkundefver"]


@subpackage("zam-plugins-clap")
def _clap(self):
    return ["usr/lib/clap"]


@subpackage("zam-plugins-ladspa")
def _ladspa(self):
    return ["usr/lib/ladspa"]


@subpackage("zam-plugins-lv2")
def _lv2(self):
    return ["usr/lib/lv2"]


@subpackage("zam-plugins-vst2")
def _vst2(self):
    return ["usr/lib/vst"]


@subpackage("zam-plugins-vst3")
def _vst3(self):
    return ["usr/lib/vst3"]
