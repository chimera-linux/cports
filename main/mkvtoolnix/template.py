pkgname = "mkvtoolnix"
pkgver = "89.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-optimization",
    "--disable-update-check",
    "--with-docbook-xsl-root=/usr/share/xsl-nons/docbook",
]
make_cmd = "rake"
make_dir = "."
make_check_target = ""
make_check_args = ["tests:unit", "tests:run_unit"]
hostmakedepends = [
    "automake",
    "docbook-xsl-nons",
    "gettext",
    "pkgconf",
    "qt6-qtbase",
    "ruby",
    "libxslt-progs",
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://mkvtoolnix.download/index.html"
source = f"https://mkvtoolnix.download/sources/mkvtoolnix-{pkgver}.tar.xz"
sha256 = "6127b694b088e53270a946c178b6816da756200bdf672abdf65cfe0b50b260b2"


@subpackage("mkvtoolnix-gui")
def _(self):
    self.depends += [
        self.parent,
        "qt6-qtsvg",
    ]
    return [
        "cmd:mkvtoolnix-gui",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/metainfo",
        "usr/share/mime",
        "usr/share/mkvtoolnix",
    ]
