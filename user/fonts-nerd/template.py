pkgname = "fonts-nerd"
pkgver = "3.3.0"
pkgrel = 1
provides = [self.with_pkgver("fonts-nerd-fonts")]
pkgdesc = "Nerd Fonts"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "custom:meta"
url = "https://www.nerdfonts.com"
# Filled later in the template
source = []
source_paths = []
sha256 = [
    "d72bdd83f02a9071d4bb0acd38a37fe687a47bd29189e838edf847ed39b87e10",
    "304010729a11da9bea9f2f1e35e84f4f2240cd8b0ec2a315ef3c1af0ba3af185",
    "2f7939592934ac02ed74e90556a7e13e95ca621b6e44df31db729ae6930f9cb4",
    "85798dd957cb18837c387ca7fd43044a62830a58860d24e7bd315fc10b5b94f6",
    "4abbf467968a0f31bb3ad8da7ecd15117cdc8265a67a793e5b9ded6437654ce7",
    "b1898e9bbfa1cbea8fd514b151ff4bb572d2562234e942408a9ef90dfb14075f",
    "44bf48101c6c31f6777a42430021681cf54c2f0699f1357a33c73c8788c5aa35",
    "0e5c4ed24358be59a8f7268f3b7352d92f5f19894cdbc62e3c0d91af16250d95",
    "f7b420dae1361d347858c78d6d48e385bc644e32781cc21eb7dcc483c3682eb1",
    "86ac1e16199fe9c3448a7882e4f3e90c11c27396fd4771c552661648e3d18f96",
    "29e494f00c6ec0bbbeba031cb69f30ebbe4cf46945d341e0347aab7073049bf0",
    "b032b5521c070076148f986d861708ed142fe19f2014a9f248ca4d0a43e9cc8e",
    "cb3667e107e265010566d05e544170b57eec3808f33b0c1790b3b1bd069690aa",
    "aa7f15a591374a04379223a0c224cd66a7c98938e52cda306311681cc51a1c22",
    "c7ee3224ff34c69fadfe947d5a9bf349952206cf8e0708564f7cf3d49095d4d8",
    "cad0abe4898b6d9aa12d28c4383ea7260eadba951b6ed9d347a524efc234dd1b",
    "8a4b6f1fda69bad7dbf102059416998caa5a870fb413c49e88d64ac2912a93e5",
    "45dca8cadd11f6eb289c13f66be3ad7fbd525504168d3c0931d57c8ad56be909",
    "e02d9dcf740b6fe72288ece5ea235a78cdc3763502b2682d7659c7618d4400c5",
    "1e2b79f888e4d07617857ddae0f82ffe07b65328fc0664e9a94bc0fac1aef888",
    "be99355fc93e9c351a4c70d7713c8f4fe038a65ac72f7ac9cc5550bc52734b70",
    "947166571476762b8e9b87a6b0532f9eab29147dc9e5d15aad1b7983229328d7",
    "7c64c44d7e530b25faf23904e135e9d1ff0339a92ee64e35e7da9116aa48af67",
    "d23c8db9d53397606bcfe6593f576abb12dd8e3d0605062231e391e2719e92c0",
    "8c5cacfa8a1fe276ea4ebdbe3b542ce71a7144c04a811c9f210faa401b436b3b",
    "d3d2a8ec7f30513e52412f8907ec4838fd5843323b9e2a5a841de6531aff9a3a",
    "da43efcf1eb53dc1773938861a9f3fcb19b71065a6a5bb0295e6038e90545027",
    "f797524e4b99191a5f35614c6fe48e96f7b8872712e2943a2aaf59cda086e909",
    "9cb2f02337782dd5eb1711f9890edaeea3d59eca00dd7ea3810c237336883fe3",
    "fddd0ada8ab3266042d4f6ddb3dd7a9c652c15ac80eda35097c3914281e14db0",
    "50d885c7f03931323c5ea232c677b8963f8d1a196cfd8f2935e2ddcf535b5971",
    "d843486d7bab95ccf06c6c17ef03773b2dc5b284602b3926356a668c49be565f",
    "105963a2025b4cb96798d1538f38aa65bd13a856cda9941ce25c139959eccd03",
    "442501cffb407e11539fa9fb4714253d779dd0508c0257c42eec187f11a18b13",
    "0a5287b9e24a9adce148daea25c04242ae65f9bb04e3610c8374eaca7379ec20",
    "01b352cd732b36d24fb7b0f2b331ddc34c2a39155af6e7a42bddf2ee279bb25d",
    "5ca2a43d1ed2a0098fbc9f87e7dc89c6a13d0399bcb82f09359fa141f9afb70b",
    "c8e7e72b6652adb34e4f0af20e22d1eda06368db3a6ebab5194d1078944ea31a",
    "7d171ea3884be22fc08bf1a1aee640a3dc93f031989c27f6f9ceb30a6a668de1",
    "2f83aabdf69d1ae28e9b60ef3777e572aafc359f32c8eae7a6278337f1364014",
    "cc2d9a78c88c91875d8fee10d7d5d67ee9f0687ef004fd61bee4e7a1ecef700b",
    "1f4d1c13252f12e9b09e09f881ea21a77645e1eac3472604990b3a11deea78c1",
    "7cad96ae914fecff010fa438276a99daf984044ade8b473049b3b63f771a5603",
    "6ad716ed719e2c97794abd5856a90c6131c406606b249debdc83b04ae11f4cb7",
    "faeb907827a2a07ae64c8fa1a5ca48cd9e60c9084a24c48d779a30cf6bd0693a",
    "51765143936c5c5078249eb77f2dc862f0d9436328c4c698918b276637d5caee",
    "b9bff1032796daffef71610639685d28a4a5baf31cb4ca43dd53f3d14820f5cf",
    "55d7390e8b45fc19a028dd93d42aebf0fe55fd85321940d1be13a5f6fa592e76",
    "556a30d1dcdbf565946605f50657fa77105d95d150413492cfa7065263f56427",
    "5cd679c82f992f4140f2ab4f6cb77b0080f71a3d7152fb8c91fe0c07f4dcce83",
    "6dc50cddca27afa51bd2cce334d6b451d6ce56e6f955c06518ae5b9b1f99e9fc",
    "960a9f36ea58ab07c2955b8cb37b4386626ae19b23d026095ef896a05842dadb",
    "70e91ef90a6d6230f6870a978b856e6138dcff0b98efa9ba3e84c447dda638a2",
    "2c9d0b6db82ef6acf71b235b5bd7b16f33cfbbba5ce08bfb1278f7dc6ec1eb20",
    "fad79b182e2c27454276b45d9633c0800302da996168bc5cee0109fda2181ed3",
    "0f7fb196b3700caeee85ddad56efde174416d73afc651a79d38bd319c1587d43",
    "87834bca780558bbe3ff808e51c89e1c3d98140a2c1a0d3100e10e944456a63c",
    "a2058cfc43eee5a170208c6e90fa77d8f0aa755e0d213e795f70781f7d807942",
    "8b5ecbe2612cb37d75e2645f7644876bc38960574909b1c01c002d0e8d33deb3",
    "88b17b50aab7ee284f9a1ed395f96c20ab4d22640fde1fe0f80a31f1eacd6585",
    "f763b82e01f06ebce5830c475306598734d2fc91ded1760fe925a826b3cba8ef",
    "f61229287e333e575f134923fd46da32fe4e01120a2a74a17d2d9b7591a9b87e",
    "fa29af2373bbf6edda1c3c9a42655227748d1a9f7b2563bf4b79253618768318",
]
options = ["empty"]

# curl https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/bin/scripts/lib/fonts.json | jq '[.fonts[] | {"package": .caskName, "name": .unpatchedName, "folder": .folderName, "spdx": (.licenseId | sub("OFL-1.1-no-RFN"; "OFL-1.1") | sub("OFL-1.1-RFN"; "OFL-1.1") | sub(" or "; " OR "))} | select(.spdx | test("LicenseRef") | not) | "(\'\(.package)\', \'\(.name)\', \'\(.folder)\', \'\(.spdx)\')"]' | sed -e 's/  "/  /g' -e 's/)"/)/g'
_fonts = [
    ("0xproto", "0xProto", "0xProto", "OFL-1.1"),
    ("3270", "IBM 3270", "3270", "BSD-3-Clause"),
    ("agave", "Agave", "Agave", "MIT"),
    ("anonymice", "Anonymous Pro", "AnonymousPro", "OFL-1.1"),
    ("arimo", "Arimo", "Arimo", "Apache-2.0"),
    ("aurulent-sans-mono", "Aurulent Sans Mono", "AurulentSansMono", "OFL-1.1"),
    ("bigblue-terminal", "BigBlue Terminal", "BigBlueTerminal", "CC-BY-SA-4.0"),
    (
        "bitstream-vera-sans-mono",
        "Bitstream Vera Sans Mono",
        "BitstreamVeraSansMono",
        "Bitstream-Vera",
    ),
    ("blex-mono", "IBM Plex Mono", "IBMPlexMono", "OFL-1.1"),
    ("caskaydia-cove", "Cascadia Code", "CascadiaCode", "OFL-1.1"),
    ("caskaydia-mono", "Cascadia Mono", "CascadiaMono", "OFL-1.1"),
    ("code-new-roman", "Code New Roman", "CodeNewRoman", "OFL-1.1"),
    ("comic-shanns-mono", "Comic Shanns Mono", "ComicShannsMono", "MIT"),
    ("commit-mono", "Commit Mono", "CommitMono", "OFL-1.1"),
    ("cousine", "Cousine", "Cousine", "Apache-2.0"),
    ("d2coding", "D2Coding", "D2Coding", "OFL-1.1"),
    ("daddy-time-mono", "DaddyTimeMono", "DaddyTimeMono", "OFL-1.1"),
    ("departure-mono", "Departure Mono", "DepartureMono", "OFL-1.1"),
    (
        "dejavu-sans-mono",
        "DejaVu Sans Mono",
        "DejaVuSansMono",
        "Bitstream-Vera",
    ),
    ("droid-sans-mono", "Droid Sans Mono", "DroidSansMono", "Apache-2.0"),
    ("envy-code-r", "Envy Code R", "EnvyCodeR", "OFL-1.1"),
    (
        "fantasque-sans-mono",
        "Fantasque Sans Mono",
        "FantasqueSansMono",
        "OFL-1.1",
    ),
    ("fira-code", "Fira Code", "FiraCode", "OFL-1.1"),
    ("fira-mono", "Fira", "FiraMono", "OFL-1.1"),
    ("geist-mono", "Geist Mono", "GeistMono", "OFL-1.1"),
    ("go-mono", "Go Mono", "Go-Mono", "BSD-3-Clause-Clear"),
    ("gohufont", "Gohu", "Gohu", "WTFPL"),
    ("hack", "Hack", "Hack", "Bitstream-Vera AND MIT"),
    ("hasklug", "Hasklig", "Hasklig", "OFL-1.1"),
    ("hurmit", "Hermit", "Hermit", "OFL-1.1"),
    ("im-writing", "iA Writer", "iA-Writer", "OFL-1.1"),
    ("inconsolata", "Inconsolata", "Inconsolata", "OFL-1.1"),
    ("inconsolata-go", "InconsolataGo", "InconsolataGo", "OFL-1.1"),
    ("inconsolata-lgc", "Inconsolata LGC", "InconsolataLGC", "OFL-1.1"),
    ("intone-mono", "Intel One Mono", "IntelOneMono", "OFL-1.1"),
    ("iosevka", "Iosevka", "Iosevka", "OFL-1.1"),
    ("iosevka-term", "Iosevka Term", "IosevkaTerm", "OFL-1.1"),
    ("iosevka-term-slab", "Iosevka Term Slab", "IosevkaTermSlab", "OFL-1.1"),
    ("jetbrains-mono", "JetBrains Mono", "JetBrainsMono", "OFL-1.1"),
    ("lekton", "Lekton", "Lekton", "OFL-1.1"),
    ("liberation", "Liberation Mono", "LiberationMono", "OFL-1.1"),
    ("lilex", "Lilex", "Lilex", "OFL-1.1"),
    ("martian-mono", "MartianMono", "MartianMono", "OFL-1.1"),
    ("meslo-lg", "Meslo LG", "Meslo", "Apache-2.0"),
    ("monaspace", "Monaspace", "Monaspace", "OFL-1.1"),
    ("monoid", "Monoid", "Monoid", "MIT OR OFL-1.1"),
    ("mononoki", "Mononoki", "Mononoki", "OFL-1.1"),
    ("m+", "MPlus", "MPlus", "OFL-1.1"),
    ("noto", "Noto", "Noto", "OFL-1.1"),
    ("open-dyslexic", "OpenDyslexic", "OpenDyslexic", "Bitstream-Vera"),
    ("overpass", "Overpass", "Overpass", "OFL-1.1 OR LGPL-2.1-only"),
    ("profont", "ProFont", "ProFont", "MIT"),
    ("proggy-clean-tt", "ProggyCleanTT", "ProggyClean", "MIT"),
    ("recursive-mono", "Recursive Mono", "Recursive", "OFL-1.1"),
    ("roboto-mono", "Roboto Mono", "RobotoMono", "Apache-2.0"),
    ("shure-tech-mono", "Share Tech Mono", "ShareTechMono", "OFL-1.1"),
    ("sauce-code-pro", "Source Code Pro", "SourceCodePro", "OFL-1.1"),
    ("space-mono", "Space Mono", "SpaceMono", "OFL-1.1"),
    ("symbols-only", "Symbols Only", "NerdFontsSymbolsOnly", "MIT"),
    ("terminess-ttf", "Terminus", "Terminus", "OFL-1.1"),
    ("tinos", "Tinos", "Tinos", "Apache-2.0"),
    ("victor-mono", "Victor Mono", "VictorMono", "OFL-1.1"),
    ("zed-mono", "Zed Mono", "ZedMono", "OFL-1.1"),
]


def install(self):
    for package, name, folder, spdx in _fonts:
        self.install_file(
            f"{folder}/*.*tf",
            f"usr/share/fonts/nerd-{package}",
            glob=True,
        )
        for file in [
            "Apache License.txt",
            "Bitstream Vera License.txt",
            "COPYING-LICENSE",
            "LICENCE.md",
            "LICENSE",
            "LICENSE.TXT",
            "LICENSE.md",
            "LICENSE.txt",
            "LICENSE_OFL.txt",
            "Licence.txt",
            "OFL.txt",
            "SIL Open Font License.txt",
            "license.txt",
        ]:
            if (self.cwd / folder / file).exists():
                self.install_license(
                    f"{folder}/{file}", pkgname=f"fonts-nerd-{package}"
                )


def _font_subpackage(package, name, folder, spdx):
    @subpackage(f"fonts-nerd-{package}")
    def _(self):
        self.pkgdesc = f"{name} with Nerd Font patches"
        self.license = spdx
        self.install_if = [self.parent]
        return [
            f"usr/share/fonts/nerd-{package}",
            f"usr/share/licenses/fonts-nerd-{package}",
        ]


for _package, _name, _folder, _spdx in _fonts:
    _download_name = _folder.replace(" ", "")
    source.append(
        f"https://github.com/ryanoasis/nerd-fonts/releases/download/v{pkgver}/{_download_name}.tar.xz"
    )
    source_paths.append(_folder)
    _font_subpackage(_package, _name, _folder, _spdx)
