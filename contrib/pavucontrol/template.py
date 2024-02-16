pkgname = "pavucontrol"
pkgver = "5.0"
pkgrel = 1
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "intltool"]
makedepends = [
    "gtkmm3.0-devel",
    "libcanberra-devel",
    "gtk+3-devel",
    "libpulse-devel",
    "json-glib-devel",
]
pkgdesc = "PulseAudio volume control"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://freedesktop.org/software/pulseaudio/pavucontrol"
source = f"$(FREEDESKTOP_SITE)/pulseaudio/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ce2b72c3b5f1a70ad0df19dd81750f9455bd20870d1d3a36d20536af2e8f4e7a"

configure_gen = []
