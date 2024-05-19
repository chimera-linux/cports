pkgname = "libkkc"
pkgver = "0.3.5"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"MAKE": "gmake"}
make_cmd = "gmake"
hostmakedepends = [
    "autoconf",
    "automake",
    "gettext",
    "gmake",
    "gnome-common",
    "gobject-introspection",
    "intltool",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = [
    "gettext-devel",
    "json-glib-devel",
    "libgee-devel",
    "marisa-trie-devel",
]
pkgdesc = "Japanese kana-kanji conversion library"
maintainer = "Nasado <hi@nasado.name>"
license = "GPL-3.0-or-later OR custom:libkkc"
url = "https://github.com/ueno/libkkc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c106a09480f36b71854f2ffd9e11a4b882e0e2cb4a4a3d16ac472315ea04f797"


def post_install(self):
    license_dir = f"usr/share/licenses/{pkgname}"
    self.install_file("COPYING", f"{license_dir}/GPL-3.0")

    with open("README.md") as f:
        readme_lines = f.read().split("\n")
        relevant_lines = readme_lines[60:-1]
        assert relevant_lines[0] == "GPLv3+"
        assert not any(lambda x: x == "```", relevant_lines)
    with open("extra-license") as f:
        for line in relevant_lines:
            f.write(line + "\n")
    self.install_file("extra-license", f"{license_dir}/custom")
