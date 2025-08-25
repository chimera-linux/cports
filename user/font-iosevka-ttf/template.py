pkgname = "font-iosevka-ttf"
pkgver = "33.3.1"
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
    "a101c78a578c31623da56c8a8d86427fea7ef7e3c7be9a90bb79f223c898936a",
    "5e885d68971157cb9e7e29d20d64730e04c9f20edf902383f2b32417e7610b5a",
    "773fccf06882d111fd0970fc50b2942b63b21dda62cb688b12c3a6646410d7bc",
    "ded80141a4f1cfafab2e0ae35278068cb9c047abb25919ac6f72f1a79197fbda",
    "8e9b122ebd6a7415872cdcd566f26031f3d549da1ea47e9145b5e09ee08127fd",
    "e7fa653037d88576377a91f816100415bf0fec1fa955acf63a9404e8e29dd67d",
    "d4fc4f1ca1c9ce70dcd55aba895efa411fb5ef5912e096388323d18e08e3948f",
    "71de1991981d609419d4eb0d707102a14f72d77c2c63c9101f8a17cd69c8c631",
    "ccb5d1f2ebbcc408bb45835a7af304e38d7686eeb9b8df16e4502f95af4af4d2",
    "8d329e58b547cc2409141a5368b7d48ec888aacebd5239eba47db30a5334240c",
    "5d19a42059456f7342434bc131a45a075639e2bbd727e64cbc087d18e37e1cd0",
    "2816db3e6ab1a51ab91102bdee326b57bcb0c6d4b8a113e14d86a99a3665cc34",
    "0ec1db76837fab8464ba6a91692985ef7c2d8ef130ed1410ab874fd4cbdc1779",
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
