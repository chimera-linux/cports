pkgname = "xfce4-windowck-plugin-unityx"
pkgver = "0.5.1"
pkgrel = 0
# Vendored dependency
build_wrksrc = "unityx/windowck-plugin"
build_style = "gnu_configure"
# UnityX's version embeds the configure.ac file into ./autogen.sh
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "intltool",
    "libtool",
    "pkgconf",
    "python",
    "xfce4-dev-tools",
]
makedepends = [
    "gtk+3-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce window controls/title bar panel plugin"
subdesc = "UnityX version"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-windowck-plugin/start"
source = "https://gitlab.com/ubuntu-unity/unity-x/unityx/-/archive//main/unityx-main.tar.gz?path=unityx/windowck-plugin>windowck-plugin.tgz"
sha256 = "ac3b8b4b40310f9971afcc6a04703d6b6cf5260102deb2167180c5e5bc060a21"
