pkgname = "zam-plugins"
pkgver = "4.4"
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
license = "GPL-2.0-or-later"
url = "https://github.com/zamaudio/zam-plugins"
_dpf = "f5815166356e85a5fe244f6024c2e401f04b10fa"
_pugl = "edd13c1b952b16633861855fcdbdd164e87b3c0a"
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
    "b3601235c6769fd4c5c3390ec44ac12c429e95556768f9276fe0adac38ce2435",
    "f38c2314662bd9b310d0a2f03ca308d6dbfde35ec633dc98567684b5803e32c3",
    "eb6106c8413596bd2bd25e1a2c3766b5c46143f513713301cd2eae49cf1f3893",
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
