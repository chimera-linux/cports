pkgname = "guitarix"
pkgver = "0.47.0"
pkgrel = 0
build_style = "waf"
hostmakedepends = [
    "binutils",
    "faust",
    "gettext",
    "gperf",
    "intltool",
    "perl",
    "pkgconf",
    "python",
    "sassc",
]
makedepends = [
    "avahi-glib-devel",
    "bluez-devel",
    "boost-devel",
    "curl-devel",
    "eigen",
    "fftw-devel",
    "fonts-roboto-ttf",
    "glib-devel",
    "glibmm2.4-devel",
    "gtk+3-devel",
    "gtkmm3.0-devel",
    "ladspa-sdk",
    "liblo-devel",
    "libsndfile-devel",
    "lilv-devel",
    "lrdf-devel",
    "pipewire-jack-devel",
    "zita-convolver-devel",
    "zita-resampler-devel",
]
pkgdesc = "Virtual guitar amplifier"
license = "GPL-2.0-or-later"
url = "https://guitarix.org"
source = f"https://github.com/brummer10/guitarix/releases/download/V{pkgver}/guitarix2-{pkgver}.tar.xz"
sha256 = "f18abd3bd2cb05960d00f15f36c63f97eb1759f9571977e3e42191ff16b9b467"
# no tests
# FIXME lintpixmaps
options = ["!check", "!lintpixmaps"]


match self.profile().arch:
    case "ppc64" | "ppc":
        # vsx assumptions in altivec code
        tool_flags = {"CXXFLAGS": ["-DEIGEN_DONT_VECTORIZE"]}
    case "riscv64":
        broken = "lv2: cannot link object files with different floating-point ABI from /lib/crti.o"
