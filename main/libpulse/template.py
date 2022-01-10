pkgname = "libpulse"
pkgver = "15.0"
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
    "meson", "pkgconf", "cmake", "perl", "perl-xml-parser", "bsdm4"
]
makedepends = [
    "dbus-devel", "eudev-devel", "libglib-devel", "libsndfile-devel",
    "libsamplerate-devel", "orc-devel", "libcap-devel", "libcap-progs",
    "linux-headers"
]
pkgdesc = "PulseAudio library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/PulseAudio"
source = f"$(FREEDESKTOP_SITE)/pulseaudio/releases/pulseaudio-{pkgver}.tar.xz"
sha256 = "a40b887a3ba98cc26976eb11bdb6613988f145b19024d1b6555c6a03c9cba1a0"

@subpackage("libpulse-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libpulse-progs")
def _progs(self):
    self.pkgdesc = "PulseAudio utilities"
    return self.default_progs()
