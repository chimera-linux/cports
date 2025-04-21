pkgname = "ibus-libpinyin"
pkgver = "1.16.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-cloud-input-mode",
    "--enable-opencc",
    "--enable-boost",
]
hostmakedepends = ["intltool", "libtool", "pkgconf", "automake", "gsed"]
makedepends = [
    "gettext-devel",
    "sqlite-devel",
    "opencc-devel",
    "lua5.4-devel",
    "ibus-devel",
    "libnotify-devel",
    "libpinyin-devel",
    "libsoup-devel",
    "json-glib-devel",
    "boost-devel",
    "python-gobject-devel",
    "util-linux-uuid-devel",
]
depends = ["ibus"]
pkgdesc = "Intelligent Pinyin engine based on libpinyin for IBus"
license = "GPL-3.0-or-later"
url = "https://github.com/libpinyin/ibus-libpinyin"
source = f"{url}/releases/download/{pkgver}/ibus-libpinyin-{pkgver}.tar.gz"
sha256 = "75ab05b6b4d82f541cda8e712a2a95c50fb939b985be0060149507b07fc94249"
exec_wrappers = [("/usr/bin/gsed", "sed")]
