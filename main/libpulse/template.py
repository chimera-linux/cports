pkgname = "libpulse"
pkgver = "16.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddaemon=false",
    "-Ddoxygen=false",
    "-Dtests=false",
    "-Ddatabase=simple",
    "-Dman=true",
    "-Dbashcompletiondir=/usr/share/bash-completion/completions",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "cmake",
    "perl",
    "perl-xml-parser",
]
makedepends = [
    "dbus-devel",
    "udev-devel",
    "glib-devel",
    "libsndfile-devel",
    "libsamplerate-devel",
    "orc-devel",
    "libcap-devel",
    "linux-headers",
]
# not in a standard path and therefore not picked up by shlib scanner
provides = [f"so:libpulsecommon-{pkgver}.so=0"]
pkgdesc = "PulseAudio library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/PulseAudio"
source = f"$(FREEDESKTOP_SITE)/pulseaudio/releases/pulseaudio-{pkgver}.tar.xz"
sha256 = "8eef32ce91d47979f95fd9a935e738cd7eb7463430dabc72863251751e504ae4"
options = ["linkundefver"]


@subpackage("libpulse-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libpulse-progs")
def _progs(self):
    self.pkgdesc = "PulseAudio utilities"
    return self.default_progs()
