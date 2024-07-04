pkgname = "farstream"
pkgver = "0.2.9"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"NOCONFIGURE": "1"}
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gobject-introspection",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gupnp-igd-devel",
    "gupnp-devel",
    "libnice-devel",
]
pkgdesc = "Audio/Video communications framework"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/Farstream"
source = f"https://freedesktop.org/software/farstream/releases/farstream/farstream-{pkgver}.tar.gz"
sha256 = "cb7d112433cf7c2e37a8ec918fb24f0ea5cb293cfa1002488e431de26482f47b"
tool_flags = {"CFLAGS": ["-Wno-deprecated-declarations"]}
# XXX: failing tests
options = ["!check"]
