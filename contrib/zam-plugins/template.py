pkgname = "zam-plugins"
pkgver = "4.1"
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
_dpf = "88180608a206b529fcb660d406ddf6f934002806"
_pugl = "844528e197c51603f6cef3238b4a48d23bf60eb7"
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
    "14fdf13e4f72e2b158c1b8db3d5c7e4a2740977acc1738c998507e0139d8ba15",
    "859ab3eb2c04b393841d8ca0cec9ce33c41140edc2920da754625bc2b9cd6dfd",
    "d7548b38dc4cfab3e04f32ce048b5721ff27f8facb84f6fcd488ab9216691ea4",
]
# FIXME: cfi
hardening = ["vis"]
# no tests
options = ["!check"]


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
