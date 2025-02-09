pkgname = "schismtracker"
pkgver = "20250208"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-flac-linking",
    "--enable-sdl2-linking",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "flac-devel",
    "sdl2-compat-devel",
    "utf8proc-devel",
]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b6dfa3dab4b2fabce004c08433007f84f06da8bb8f2d799dc23d2e79f29d263d"
tool_flags = {
    "CFLAGS": [
        f'-DVERSION2="{pkgver}"',
        # crashes when parsing config otherwise
        "-U_FORTIFY_SOURCE",
    ],
}
