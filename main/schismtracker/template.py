pkgname = "schismtracker"
pkgver = "20241226"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-flac-linking",
    "--enable-sdl2-linking",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "flac-devel",
    "sdl-devel",
    "utf8proc-devel",
]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "32b9e5f3cab7648c89b23449fb7ca2ab77abd9e67e120ced70770710b1e06a58"
tool_flags = {
    "CFLAGS": [
        f'-DVERSION2="{pkgver}"',
        # crashes when parsing config otherwise
        "-U_FORTIFY_SOURCE",
    ],
}
