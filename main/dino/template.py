pkgname = "dino"
pkgver = "0.4.2"
pkgrel = 1
build_style = "cmake"
# TODO: openpgp maybe
configure_args = [
    "-DDINO_PLUGIN_ENABLED_notification-sound=ON",
    "-DUSE_SOUP3=ON",
    # TODO
    "-DBUILD_TESTS=OFF",
]
hostmakedepends = [
    "cmake", "pkgconf", "ninja", "gettext-tiny", "unzip", "vala", "glib-devel",
]
makedepends = [
    "gtk4-devel", "libadwaita-devel", "glib-devel", "libsoup-devel",
    "qrencode-devel", "libgee-devel", "libgcrypt-devel", "sqlite-devel",
    "libcanberra-devel", "gspell-devel", "libsrtp-devel", "libnice-devel",
    "gnutls-devel", "libsignal-protocol-c-devel", "gst-plugins-base-devel",
    "gpgme-devel",
]
depends = ["desktop-file-utils"]
pkgdesc = "Modern XMPP client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/dino/dino"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "59cbe1b90f947a38609c48633e32b4090d7da44dfae1bee2a741f65251e1488e"
# TODO
options = ["!check"]

# generates errors with llvm 16
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
