pkgname = "wlr-which-key"
pkgver = "1.3.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "libxkbcommon-devel",
    "pango-devel",
    "rust-std",
]
pkgdesc = "Keymap manager for wlroots-based compositors"
license = "GPL-3.0-or-later"
url = "https://github.com/MaxVerevkin/wlr-which-key"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "50fc06f60e67dc678ffe7bb167d662910d98085e185d2030c09ebd5793bf2794"
