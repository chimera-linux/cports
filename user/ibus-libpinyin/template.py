pkgname = "ibus-libpinyin"
pkgver = "1.16.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-cloud-input-mode",
    "--enable-opencc",
    "--enable-boost",
]
hostmakedepends = ["intltool", "libtool", "pkgconf", "automake", "gsed"]
makedepends = [
    "boost-devel",
    "gettext-devel",
    "ibus-devel",
    "json-glib-devel",
    "libnotify-devel",
    "libpinyin-devel",
    "libsoup-devel",
    "lua5.4-devel",
    "opencc-devel",
    "python-gobject-devel",
    "sqlite-devel",
    "util-linux-uuid-devel",
]
depends = ["ibus"]
pkgdesc = "Intelligent Pinyin engine based on libpinyin for IBus"
license = "GPL-3.0-or-later"
url = "https://github.com/libpinyin/ibus-libpinyin"
source = f"{url}/releases/download/{pkgver}/ibus-libpinyin-{pkgver}.tar.gz"
sha256 = "cc652d48e68b8b03afc5e9e08509676aee89f9d492b9a3897cd028bcc800ce31"
exec_wrappers = [("/usr/bin/gsed", "sed")]
