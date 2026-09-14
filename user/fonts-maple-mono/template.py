pkgname = "fonts-maple-mono"
pkgver = "7.9"
pkgrel = 0
pkgdesc = "Monospace font with round corners and ligatures"
license = "OFL-1.1"
url = "https://font.subf.dev"
source = [
    f"https://github.com/subframe7536/maple-font/releases/download/v{pkgver}/MapleMono-OTF.zip",
    f"https://github.com/subframe7536/maple-font/releases/download/v{pkgver}/MapleMono-NF-unhinted.zip",
]
source_paths = ["maple-otf", "maple-nf"]
sha256 = [
    "ecf47b851ae4001b00564399511af8dc9615339d3ae9ded54e8547d6d1ad3da1",
    "8248d6260660be1066b5ebe90d25131582df8383f38db1c284dd1f2dc9d2b46e",
]


def install(self):
    self.install_file(
        "maple-otf/*.otf", "usr/share/fonts/maple-mono", glob=True
    )
    self.install_file(
        "maple-nf/*.ttf", "usr/share/fonts/maple-mono-nf", glob=True
    )
    self.install_license("maple-otf/LICENSE.txt")
    self.install_license("maple-nf/LICENSE.txt", pkgname="fonts-maple-mono-nf")


@subpackage("fonts-maple-mono-nf")
def _(self):
    self.pkgdesc = "Maple Mono with Nerd Font patches"
    return [
        "usr/share/fonts/maple-mono-nf",
        "?usr/share/licenses/fonts-maple-mono-nf",
    ]
