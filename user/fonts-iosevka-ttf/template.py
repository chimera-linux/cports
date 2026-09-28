pkgname = "fonts-iosevka-ttf"
pkgver = "34.8.1"
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
    "0ea6f8a7d37444a974b45d24995b3a58f80924b71e8c51f0d91a879fa87c36be",
    "c9929ef8c27e5469906468e378e11d3023690ae9cd411a4af3de78190b901075",
    "07f44a9dada3155eb1fab4ffa6a8e7805ecee257e0180360d044c07f091ca1c3",
    "bb43009284889960b04f662276bd27b5212cf2cd851aee49e54955d9af7b980d",
    "187fd2a335ccdef3cbf2fca29e4b266ed5b1919e61332ca28c5607715f6f14f0",
    "8ec08b0d1eca0fbba4ebf95b2efc00af325c50240d588913d351ce2838dc9e6a",
    "24bc2e3e591a4f638873d9dea632aacc5bc1b3d4054335fd9274544a6e03aa1a",
    "cf66d6ff568c019e8200993703bb76acdb313e720d0b91a00af4bac8e72e4c81",
    "c21a7d84771322cefd4177d59c7dbae29ecf719ead5848d6b5a81e46cf54ea66",
    "79eba25d4fcf03c3b90b92cb52e3e703e757b94d4d3c77ec852e3d4d99d5a2cc",
    "882660083c794a0d36f503c522adcb82f488fcc2ea87ec2e776f5ecb407da598",
    "8644ed89feb43d632f48255e6445d6512e68fd77850d650e30c69607e9e3dba5",
    "9671f1b49df5ce1a08236ab6381664a533944889593dad9b4c8cf151c4afd8ea",
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
