pkgname = "schismtracker"
pkgver = "20250313"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-flac-linking",
    "--enable-sdl3-linking",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "flac-devel",
    "sdl3-devel",
    "utf8proc-devel",
]
pkgdesc = "Reimplementation of Impulse Tracker"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0811a1133cb7a8c4c69713a15389b6601ec909b406b9e4d7e8ca2833887f0124"
tool_flags = {
    "CFLAGS": [
        f'-DVERSION2="{pkgver}"',
        # crashes when parsing config otherwise
        "-U_FORTIFY_SOURCE",
    ],
}
