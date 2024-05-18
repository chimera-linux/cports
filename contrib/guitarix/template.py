pkgname = "guitarix"
pkgver = "0.44.1"
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
    "eigen",
    "fftw-devel",
    "fonts-roboto-ttf",
    "glib-devel",
    "glibmm2.4-devel",
    "gtk+3-devel",
    "gtkmm3.0-devel",
    "ladspa-sdk",
    "libcurl-devel",
    "liblo-devel",
    "libsndfile-devel",
    "lilv-devel",
    "lrdf-devel",
    "pipewire-jack-devel",
    "zita-convolver-devel",
    "zita-resampler-devel",
]
pkgdesc = "Virtual guitar amplifier"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://guitarix.org"
source = f"$(SOURCEFORGE_SITE)/guitarix/guitarix/guitarix2-{pkgver}.tar.xz"
sha256 = "77e83d754f51ac38c5423f38eeb55de5b3e26128e60b511b02d2defcf36e6c18"
# no tests
options = ["!check"]


match self.profile().arch:
    case "ppc64" | "ppc":
        # vsx assumptions in altivec code
        tool_flags = {"CXXFLAGS": ["-DEIGEN_DONT_VECTORIZE"]}
    case "riscv64":
        broken = "lv2: cannot link object files with different floating-point ABI from /lib/crti.o"
