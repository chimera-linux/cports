pkgname = "fonts-monaspace"
pkgver = "1.300"
pkgrel = 0
pkgdesc = "GitHub Next Monaspace fonts"
license = "OFL-1.1"
url = "https://github.com/githubnext/monaspace"
source = f"{url}/archive/refs/tags/v{pkgver}.zip"
sha256 = "ae88b842f8a7a96eed7af964961fea5254c5f5e8d63dd1099b1b6ceb821be7d9"
options = ["empty"]

_target = "usr/share/fonts/monaspace"
_variants = (
    # (subn, subd, srcdir, destdir, ftype)
    ("frozen", "frozen ttf fonts", "Frozen Fonts/*", "frozen", "ttf"),
    (
        "nerd",
        "otf fonts with nerd patch and extra icons",
        "NerdFonts/*",
        "nerd",
        "otf",
    ),
    ("otf", "static otf fonts", "Static Fonts/*", "static", "otf"),
    ("ttf-vf", "variable ttf fonts", "Variable Fonts/*", "variable", "ttf"),
    # web .woff2 fonts are not installed
)


def _gensub(_subn, _subd, _srcdir, _destdir, _ftype):
    @subpackage(f"{pkgname}-{_subn}")
    def _(self):
        self.subdesc = _subd
        if _subn == "otf":
            self.install_if = [self.parent]

        return [f"{_target}/{_destdir}/*.{_ftype}"]


def install(self):
    for _subn, _subd, _srcdir, _destdir, _ftype in _variants:
        self.install_file(
            f"fonts/{_srcdir}/*.{_ftype}", f"{_target}/{_destdir}", glob=True
        )


def post_install(self):
    self.install_license("LICENSE")


for _item in _variants:
    _gensub(*_item)
