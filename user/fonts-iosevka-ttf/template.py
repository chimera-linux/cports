pkgname = "fonts-iosevka-ttf"
pkgver = "34.9.0"
pkgrel = 0
pkgdesc = "Versatile typeface for code, from code"
license = "OFL-1.1"
url = "https://typeof.net/Iosevka"
_durl = f"https://github.com/be5invis/Iosevka/releases/download/v{pkgver}"
# Filled later in the template
source = [
    f"!https://github.com/be5invis/Iosevka/raw/refs/tags/v{pkgver}/LICENSE.md>LICENSE-{pkgver}.md",
    f"{_durl}/PkgTTF-Iosevka-{pkgver}.zip",
]
sha256 = [
    "4ba53c7c1cb39279aae5f8d7d22054c485c71169920e5a36ed098b115e2e3c5d",
    "c61a10b880bf3087f982217423fa2876a93803bd2a1901fbc52ab80c7329f716",
    "1c0b8ac68ca210cc253c1833619d37ed2227d96fbdda0a36231375828b7bd6fb",
    "88ce8445d6a05899c897596e329621b422154f4baef98bd50e3afbe4c90dcff4",
    "f25b34ffea64e2ecea90df13c075f11defd85708106128235837dfa039f446bb",
    "0d6bcb9cf59c2c9649a2cee2fa583e78392cad5719efac642308d3d289b17b46",
    "6c743634c7f5d0cde41755fc2621f14b6cfe1aae316bdc6b30a06fbbd9dbe80d",
    "0dfe9139efbad5df302c1c2be9b9493a690db39d692211218385a821bdbd0cf0",
    "beed8b476f00a7dac3c5ee53120f58106ed16678d512c8dec67ad9700c02d335",
    "689c72e664853e211e3fe68a1cd8fc0d4c4c91ab046dbdd75f07fb27284a91f5",
    "cb362f240364a98ee3dc57589c3d7ca87d6c0c92ea072cdb1947fb47a5d1c915",
    "123aa08bf337f51491c977d30c01a8e9c5a13c5cc20d2d4c5d98eb0a5c9795f8",
    "322a0b2e0f2d412dce8eaf2d4a80a728025c46f6111e447e211e83747dd05aca",
    "4c0c24174de7af4742405408f5c7abf989e54c77089e7be804314c75b6e6405a",
]


def install(self):
    self.install_file(
        "Iosevka*.ttf",
        "usr/share/fonts/iosevka",
        glob=True,
    )
    self.install_license(
        self.sources_path / f"LICENSE-{pkgver}.md", name="LICENSE.md"
    )


def _subpkg(variant):
    subpkg = "".join(["-" + c.lower() if c.isupper() else c for c in _variant])

    @subpackage(f"fonts-iosevka{subpkg}-ttf")
    def _(self):
        self.subdesc = variant
        return [
            f"usr/share/fonts/iosevka/Iosevka{variant}-*.ttf",
        ]


for _variant in [
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
]:
    source += [f"{_durl}/PkgTTF-Iosevka{_variant}-{pkgver}.zip"]
    _subpkg(_variant)
