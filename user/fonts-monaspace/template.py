pkgname = "fonts-monaspace"
pkgver = "1.301"
pkgrel = 0
pkgdesc = "GitHub Next Monaspace fonts"
license = "OFL-1.1"
url = "https://github.com/githubnext/monaspace"
sha256 = [
    "e82c1a0dc52f88f935b3b46ce4b4e50f811517186c86e183e05b1f1d396797d7",
    "e201697c8ef3cfd4559fbfb4b5f60bf7425113729bca28e33b0a9112db1ca579",
    "255d7101e6fefc9d4bb7df844c79b7f4e11c61e62387a13c4bd0a5970c3f6674",
    "0e84e5f7dd6f05e74a00f2fb828ca43e489d954f5509ff0fa439ea18c0d35fe9",
]
options = ["empty"]

_target = "usr/share/fonts/monaspace"
_variants = (
    # (subn, subd, srcname/dirname)
    ("ttf-frozen", "frozen ttf fonts", "frozen"),
    ("otf", "static otf fonts", "static"),
    ("ttf-vf", "variable ttf fonts", "variable"),
    # nerd and web fonts are not installed
)


def _gensub(_subn, _subd, _dirname):
    @subpackage(f"{pkgname}-{_subn}")
    def _(self):
        self.subdesc = _subd
        if _subn == "otf":
            self.install_if = [self.parent]

        return [f"{_target}/{_dirname}"]


source = [
    f"{url}/releases/download/v{pkgver}/monaspace-{_srcname}-v{pkgver}.zip"
    for (_subn, _subd, _srcname) in _variants
] + [f"!{url}/raw/v{pkgver}/LICENSE"]
source_paths = [_dirname for (_subn, _subd, _dirname) in _variants] + [""]


def install(self):
    for _subn, _subd, _dirname in _variants:
        self.install_file(f"{_dirname}/*/*", f"{_target}/{_dirname}", glob=True)


def post_install(self):
    self.install_license(f"{self.sources_path}/LICENSE")


for _item in _variants:
    _gensub(*_item)
