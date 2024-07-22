pkgname = "mkvtoolnix"
pkgver = "86.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-optimization",
    "--disable-update-check",
    "--with-docbook-xsl-root=/usr/share/xsl/docbook",
]
make_cmd = "rake"
make_dir = "."
make_check_target = ""
make_check_args = ["tests:unit", "tests:run_unit"]
hostmakedepends = [
    "automake",
    "docbook-xsl",
    "gettext",
    "pkgconf",
    "qt6-qtbase",
    "ruby",
    "xsltproc",
]
makedepends = [
    "boost-devel",
    "cmark-devel",
    "file-devel",
    "flac-devel",
    "fmt-devel",
    "gmp-devel",
    "gtest-devel",
    "libdvdread-devel",
    "libmatroska-devel",
    "libogg-devel",
    "libvorbis-devel",
    "nlohmann-json",
    "pcre2-devel",
    "pugixml-devel",
    "qt6-qtbase-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "Tooling for editing and inspecting Matroska files"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://mkvtoolnix.download/index.html"
source = f"https://mkvtoolnix.download/sources/mkvtoolnix-{pkgver}.tar.xz"
sha256 = "29a9155fbba99f9074de2abcfbdc4e966ea38c16d9f6f547cf2d8d9a48152c97"


@subpackage("mkvtoolnix-gui")
def _gui(self):
    self.depends += [
        self.parent,
        "qt6-qtsvg",
    ]
    return [
        "usr/bin/mkvtoolnix-gui",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/man/man1/mkvtoolnix-gui.1",
        "usr/share/metainfo",
        "usr/share/mime",
        "usr/share/mkvtoolnix",
    ]
