pkgname = "font-iosevka-ttf"
pkgver = "33.2.6"
pkgrel = 0
pkgdesc = "Versatile typeface for code, from code"
license = "OFL-1.1"
url = "https://typeof.net/Iosevka"
_download = f"https://github.com/be5invis/Iosevka/releases/download/v{pkgver}"
# Filled later in the template
source = [
    f"!https://github.com/be5invis/Iosevka/raw/refs/tags/v{pkgver}/LICENSE.md",
    f"{_download}/PkgTTF-Iosevka-{pkgver}.zip",
]
sha256 = [
    "52579dd4ebbda8e5a9d314e395dbfe40de82b4b7b3007ec8458876823af8dddd",
    "6063cedf00a85e635d7c2878657e284bce7699a58e4347e62f8c3583cf863f94",
    "f89811ca9eb64254f9175922cf90d1ce318f1d3af77690faecc124cf9a004976",
    "70266ce17946b9c128463afb861bf4a052651c18646e93b115fa3eb0f3533606",
    "ad4a1a271c34c2228b58c4349c95b759962cf7d70866a9400f387cd6af1fb15f",
    "bc37e2c081531b0747fe5bc3a2a550f6ba9ad2d8767a748b15507813112444f1",
    "e828f18d9a50f39fb28191fe5a58c2f57c132487ce84806c1e04cd46d096c09c",
    "85a410f1c0cf80bfe85ee9e421d40510a4ad7f8f43bbfbaa1eddf77bc5f511c4",
    "19f2a4cd6587df0785274d2656b136debfe43985e81bd533a41fe2e263716e30",
    "2bc6f41a876ae24b3e54ff70f3074583a33b62e0c16f240af6d68c284bcddfb2",
    "b571b47fb9c474b5a8f01f13aa6d72125fb853f86d667c29a575691e2dbe2682",
    "257366d1327906e2327904c47f1609f777e7fbf2df715ddd4217370e641c1cac",
    "dd4ad252d1986e5f2622ce2aef2406ba08a393c40dbe844b42889d26dc369b78",
    "a7ec24a46f4d593512afa514824d1c975d161413b30f0e4d127eb43ac4116f6e",
]

_variants = [
    "Term",
    "Aile",
    "Etoile",
    "Slab",
    "TermSlab",
    "FixedSlab",
    "CurlySlab",
    "TermCurlySlab",
    "FixedCurlySlab",
    "Curly",
    "TermCurly",
    "FixedCurly",
]


def install(self):
    self.install_file(
        "Iosevka*.ttf",
        "usr/share/fonts/iosevka",
        glob=True,
    )
    self.install_license(self.sources_path / "LICENSE.md")


def _font_subpackage(package, variant):
    @subpackage(f"font-iosevka{package}-ttf")
    def _(self):
        return [
            f"usr/share/fonts/iosevka/Iosevka{variant}-*.ttf",
        ]


for _variant in _variants:
    _package = "".join(
        ["-" + c.lower() if c.isupper() else c for c in _variant]
    )
    source.append(f"{_download}/PkgTTF-Iosevka{_variant}-{pkgver}.zip")
    _font_subpackage(_package, _variant)
