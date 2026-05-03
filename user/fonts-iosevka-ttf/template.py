pkgname = "fonts-iosevka-ttf"
pkgver = "34.7.0"
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
    "049c0ea7c1ba2b28091ba73adacdd2968253b9f86e010d4491752b2926d2a95b",
    "cb75046a641a2a2fb27fc556b44183b4745792ab0f0a9dc450864f7983764321",
    "14f3a16f5ebbafb438d3bd15bb8398e6267d2590f1091b2df1ba74e8e4dabc4b",
    "a1986b1329e192ac1a1829b873b6492078cbdde30c682e549563d07fe2dac93d",
    "05abdedfd668b0aeffe689db39fc1a95022fd14b786a7f4659fb23d00a0560ef",
    "c53ba6198351a497dea46b99be38780114177247840dd2ebca6d8630af26fe00",
    "3c2823a090677037bec16b4bc0344335553d04d5236ed4ce24932cd08bb2b8d5",
    "97d10cd3052cf30a3bc5bac4434d2937220e3343c4304eca9bd5c2259b10f5bc",
    "f657549a1a572d826c0789a5592872b1c7563e91ba3f0a0603b5501b1cbb4202",
    "3b369116fd8de2d032ab2bf7b647f0008f3012ba8828f6fc9dd0244c0bb88f2b",
    "2d3cd9eded068b54e494babd3b6d57e0f5114368e0eae3aaf2ff648001faf6bf",
    "05535ad382a9b8d43ce776274a7869cb3a6753ff0ef1e56a8392ccd7f46b3183",
    "6b23bfc95232a4e1a37b17d7153cb55cf68938c0be1b77217559beaa902d8b51",
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
