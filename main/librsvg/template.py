pkgname = "librsvg"
pkgver = "2.52.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-introspection", "--enable-vala", "--disable-dependency-tracking"
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "cargo", "python", "gobject-introspection",
    "glib-devel", "gdk-pixbuf-devel", "vala"
]
makedepends = [
    "rust", "vala-devel", "cairo-devel", "pango-devel", "freetype-devel",
    "gdk-pixbuf-devel", "libglib-devel", "libxml2-devel",
]
provides = [f"gdk-pixbuf-loader-svg={pkgver}-r{pkgrel}"]
pkgdesc = "SVG library for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/LibRsvg"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "407cbbab518137ea18a3f3220bea180fbee75f3e5bd6ba10a7a862c1a6f74d82"
# sample files may differ based on pango/freetype/harfbuzz version
options = ["!check"]

def _clear_vendor_checksums(self, pkg):
    import re
    p = (self.cwd / "vendor" / pkg / ".cargo-checksum.json")
    p.write_text(re.sub(r"""("files":{)[^}]*""", r"\1", p.read_text()))

def post_patch(self):
    # needed mainly for cross builds
    with open(self.cwd / ".cargo/config", "a") as cf:
        cf.write(f"""
[target.{self.profile().triplet}]
linker = "{self.get_tool("CC")}"
""")

    _clear_vendor_checksums(self, "system-deps")

@subpackage("librsvg-static")
def _static(self):
    return self.default_static()

@subpackage("librsvg-devel")
def _devel(self):
    return self.default_devel(man = True)

@subpackage("librsvg-progs")
def _progs(self):
    return self.default_progs(man = True)
