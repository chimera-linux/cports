pkgname = "mt32emu"
pkgver = "2.7.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "alsa-lib-devel",
    "glib-devel",
    "libpulse-devel",
    "pipewire-jack-devel",
    "portaudio-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Pre-GM MIDI device emulation library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-or-later AND GPL-3.0-or-later"
url = "https://munt.sourceforge.net"
source = f"https://github.com/munt/munt/archive/refs/tags/munt_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "29565cf02a213143d60e6f5c0c992eb80ce6a08874e4cc90456072c8dbcba581"


@subpackage("mt32emu-devel")
def _(self):
    return self.default_devel()


@subpackage("mt32emu-qt")
def _(self):
    self.pkgdesc = "Software synthesiser emulating pre-GM MIDI devices"

    return [
        "usr/bin/mt32emu-qt",
        "usr/share/applications/mt32emu-qt.desktop",
        "usr/share/doc/munt/mt32emu-qt",
        "usr/share/icons/hicolor/*/apps/munt.png",
    ]
