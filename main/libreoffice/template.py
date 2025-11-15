pkgname = "libreoffice"
pkgver = "25.8.2.2"
pkgrel = 0
# riscv64: no handling of libcxxabi + likely too slow
archs = ["x86_64", "ppc64le", "ppc64", "aarch64"]
build_style = "gnu_configure"
configure_args = [
    "--with-vendor=Chimera Linux",
    "--with-help",
    "--disable-ccache",  # automatic
    "--disable-fetch-external",
    "--disable-odk",
    "--disable-online-update",
    "--disable-dependency-tracking",
    "--disable-qt5",
    "--disable-kf5",
    "--disable-gtk3-kde5",
    "--disable-dconf",
    "--disable-epm",
    "--disable-lpsolve",
    "--disable-coinmp",
    "--disable-firebird-sdbc",
    "--disable-mariadb-sdbc",
    "--disable-postgresql-sdbc",
    "--enable-release-build",
    "--enable-split-app-modules",
    "--enable-python=system",
    "--enable-introspection",
    "--enable-gtk3",
    "--enable-gtk4",
    "--enable-kf6",
    "--enable-qt6",
    "--enable-build-opensymbol",
    "--with-external-dict-dir=/usr/share/hunspell",
    "--with-external-hyph-dir=/usr/share/hyphen",
    "--with-system-libs",
    "--with-system-headers",
    "--with-tls=nss",
    "--with-myspell-dicts",
    "--without-java",
    "--without-fonts",
    "--without-system-box2d",
    "--without-system-libcmis",
    "--without-system-libeot",
    "--without-system-libzmf",
    "--without-system-libstaroffice",
    "--without-system-dragonbox",
    "--without-system-frozen",
    "--without-system-libfixmath",
    "--without-system-zxcvbn",
]
configure_env = {"NOCONFIGURE": "1", "QT6DIR": "/usr/lib/qt6"}
configure_gen = ["perl", "autogen.sh"]
make_dir = "."
make_build_target = "build"
make_use_env = True
hostmakedepends = [
    "automake",
    "bash",
    "bison",
    "flex",
    "fontforge-cli",
    "gettext",
    "gnupg",
    "gobject-introspection",
    "gperf",
    "gtk4-devel",
    "hyphen",
    "icu",
    "libtool",
    "libxml2-progs",
    "libxslt-progs",
    "pkgconf",
    "python-lxml",
    "python-setuptools",
    "qt6-qtbase",
    "sane-backends",
    "unzip",
    "xz",
    "zip",
]
makedepends = [
    "abseil-cpp-devel",
    "argon2-devel",
    "avahi-devel",
    "bluez-devel",
    "boost-devel",
    "cairo-devel",
    "clucene-devel",
    "cppunit-devel",
    "curl-devel",
    "fontconfig-devel",
    "freetype-devel",
    "glm",
    "gobject-introspection-devel",
    "gpgme-devel",
    "graphite2-devel",
    "gst-plugins-base-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "harfbuzz-devel",
    "hunspell-devel",
    "hyphen-devel",
    "icu-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kwindowsystem-devel",
    "lcms2-devel",
    "libabw-devel",
    "libatomic_ops-devel",
    "libcdr-devel",
    "libe-book-devel",
    "libepoxy-devel",
    "libepubgen-devel",
    "libetonyek-devel",
    "libexpat-devel",
    "libexttextcat-devel",
    "libfreehand-devel",
    "libgcrypt-devel",
    "libjpeg-turbo-devel",
    "liblangtag-devel",
    "libmspub-devel",
    "libmwaw-devel",
    "libnumbertext-devel",
    "libodfgen-devel",
    "liborcus-devel",
    "libpagemaker-devel",
    "libpng-devel",
    "libqxp-devel",
    "librevenge-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libtool-devel",
    "libvisio-devel",
    "libwebp-devel",
    "libwpg-devel",
    "libwps-devel",
    "libxml2-devel",
    "libxslt-devel",
    "libxt-devel",
    "mdds",
    "mythes-devel",
    "neon-devel",
    "nspr-devel",
    "nss-devel",
    "openjpeg-devel",
    "openldap-devel",
    "openssl3-devel",
    "poppler-devel",
    "python-devel",
    "qt6-qtbase-devel",
    "qt6-qtmultimedia-devel",
    "redland-devel",
    "sane-backends-devel",
    "unixodbc-devel",
    "xmlsec1-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
    "zxing-cpp-devel",
]
pkgdesc = "Free office suite"
license = "GPL-3.0-or-later"
url = "https://www.libreoffice.org"
# big and not particularly useful testsuite
# FIXME: lto breaks LO with clang 17
options = ["!lto", "!cross", "!check", "linkundefver", "empty"]

_surl = f"https://download.documentfoundation.org/libreoffice/src/{pkgver[:-2]}"
_aurl = "!https://dev-www.libreoffice.org/src"
_eurl = "!https://dev-www.libreoffice.org/extern"

source = [
    f"{_surl}/libreoffice-{pkgver}.tar.xz",
    f"{_surl}/libreoffice-dictionaries-{pkgver}.tar.xz",
    f"{_surl}/libreoffice-help-{pkgver}.tar.xz",
    f"{_surl}/libreoffice-translations-{pkgver}.tar.xz",
    f"{_aurl}/rhino-1.7.15.zip",
    f"{_aurl}/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip",
    f"{_aurl}/ace6ab49184e329db254e454a010f56d-libxml-1.1.7.zip",
    f"{_aurl}/language-subtag-registry-2025-08-25.tar.bz2",
    f"{_aurl}/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip",
    f"{_aurl}/d8bd5eed178db6e2b18eeed243f85aa8-flute-1.1.6.zip",
    f"{_aurl}/ba2930200c9f019c2d93a8c88c651a0f-flow-engine-0.9.4.zip",
    f"{_aurl}/box2d-2.4.1.tar.gz",
    f"{_aurl}/libcmis-0.6.2.tar.xz",
    f"{_aurl}/libeot-0.01.tar.bz2",
    f"{_aurl}/libstaroffice-0.0.7.tar.xz",
    f"{_aurl}/libzmf-0.0.2.tar.xz",
    f"{_aurl}/pdfium-7012.tar.bz2",
    f"{_eurl}/8249374c274932a21846fa7629c2aa9b-officeotron-0.7.4-master.jar",
    f"{_eurl}/odfvalidator-0.9.0-RC2-SNAPSHOT-jar-with-dependencies-2726ab578664434a545f8379a01a9faffac0ae73.jar",
    f"{_aurl}/dtoa-20180411.tgz",
    f"{_aurl}/bsh-2.1.1-src.zip",
    f"{_aurl}/libnumbertext-1.0.11.tar.xz",
    f"{_aurl}/eeb2c7ddf0d302fba4bfc6e97eac9624-libbase-1.1.6.zip",
    f"{_aurl}/3bdf40c0d199af31923e900d082ca2dd-libfonts-1.1.6.zip",
    f"{_aurl}/3404ab6b1792ae5f16bbd603bd1e1d03-libformula-1.1.7.zip",
    f"{_aurl}/db60e4fde8dd6d6807523deb71ee34dc-liblayout-0.2.10.zip",
    f"{_aurl}/97b2d4dba862397f446b217e2b623e71-libloader-1.1.6.zip",
    f"{_aurl}/8ce2fcd72becf06c41f7201d15373ed9-librepository-1.1.6.zip",
    f"{_aurl}/f94d9870737518e3b597f9265f4e9803-libserializer-1.1.6.zip",
    f"{_aurl}/39bb3fcea1514f1369fcfc87542390fd-sacjava-1.3.zip",
    f"{_aurl}/skia-m136-28685d899b0a35894743e2cedad4c9f525e90e1e.tar.xz",
    f"{_aurl}/dragonbox-1.1.3.tar.gz",
    f"{_aurl}/frozen-1.2.0.tar.gz",
    f"{_aurl}/zxcvbn-c-2.6.tar.gz",
]
sha256 = [
    "002ca2eec3df818d3655bc5ab5702263194febc0212f02e12df1eee11bd7c15e",
    "1fc67d410c48c8215562d9fd84d27b1cab67b1fb2502a457e6fbbd91c3298516",
    "bb9fde2c035c757581f49545ccbfb046fc31f72968b53b28d0987f1c5547eb5f",
    "fb01188fd7258b4da36782618d790e4073769097c0597e103eb814963e272830",
    "42fce6baf1bf789b62bf938b8e8ec18a1ac92c989dd6e7221e9531454cbd97fa",
    "75823776fb51a9c526af904f1503a7afaaab900fba83eda64f8a41073724c870",
    "7d2797fe9f79a77009721e3f14fa4a1dec17a6d706bdc93f85f1f01d124fab66",
    "9b008d21f97bbf37c5aefd07805ff5500524bccbe8c39d623e184b1ed425ff39",
    "d30b13f4ba2e3b6a2d4f020c0dee0a9fb9fc6fbcc2d561f36b78da4bf3802370",
    "1b5b24f7bc543c0362b667692f78db8bab4ed6dafc6172f104d0bd3757d8a133",
    "233f66e8d25c5dd971716d4200203a612a407649686ef3b52075d04b4c9df0dd",
    "d6b4650ff897ee1ead27cf77a5933ea197cbeef6705638dd181adc2e816b23c2",
    "1b5c2d7258ff93eb5f9958ff0e4dfd7332dc75a071bb717dde2217a26602a644",
    "cf5091fa8e7dcdbe667335eb90a2cfdd0a3fe8f8c7c8d1ece44d9d055736a06a",
    "f94fb0ad8216f97127bedef163a45886b43c62deac5e5b0f5e628e234220c8db",
    "27051a30cb057fdb5d5de65a1f165c7153dc76e27fe62251cbb86639eb2caf22",
    "e647ca4fcc2c91d9dca717452e1b1be1ab6155ac4977dca716041652c7b10bdd",
    "f2443f27561af52324eee03a1892d9f569adc8db9e7bca55614898bc2a13a770",
    "d55495ab3a86544650587de2a72180ddf8bfc6376d14ddfa923992dbc86a06e0",
    "0082d0684f7db6f62361b76c4b7faba19e0c7ce5cb8e36c4b65fea8281e711b4",
    "2248387ceaa319840434a3547a8b2fec12f95a8418ee039ce5ff5726053a139c",
    "5dcb4db3b2340f81f601ce86d8d76b69e34d70f84f804192c901e4b7f84d5fb0",
    "75c80359c9ce343c20aab8a36a45cb3b9ee7c61cf92c13ae45399d854423a9ba",
    "e0531091787c0f16c83965fdcbc49162c059d7f0c64669e7f119699321549743",
    "5826d1551bf599b85742545f6e01a0079b93c1b2c8434bf409eddb3a29e4726b",
    "e1fb87f3f7b980d33414473279615c4644027e013012d156efa538bc2b031772",
    "3d853b19b1d94a6efa69e7af90f7f2b09ecf302913bee3da796c15ecfebcfac8",
    "abe2c57ac12ba45d83563b02e240fa95d973376de2f720aab8fe11f2e621c095",
    "05640a1f6805b2b2d7e2cb9c50db9a5cb084e3c52ab1a71ce015239b4a1d4343",
    "085f2112c51fa8c1783fac12fbd452650596415121348393bb51f0f7e85a9045",
    "2384f5f44a0b714d8dc78923fdf17453ab5a1808ca638154e3e27b361531db25",
    "09d63b05e9c594ec423778ab59b7a5aa1d76fdd71d25c7048b0258c4ec9c3384",
    "ed8339c017d7c5fe019ac2c642477f435278f0dc643c1d69d3f3b1e95915e823",
    "11e39f6776f9c82c68b2acb94336e32697d4ab6cdb4ac16f9583ccbdd735113a",
]
tool_flags = {
    "CXXFLAGS": ["-DGLM_ENABLE_EXPERIMENTAL", "-DU_USING_ICU_NAMESPACE=1"]
}


_langs = []


def post_extract(self):
    # copy the files over
    for s in source[1:]:
        if s.startswith("!"):
            s = s[1:]
        self.cp(self.sources_path / s[s.rfind("/") + 1 :], self.cwd)

    # copy over patches
    self.cp("^/libcmis-libxml2.patch.1", "external/libcmis")


def init_configure(self):
    if self.profile().endian == "big":
        self.configure_args += ["--disable-skia"]
    if self.has_lto():
        self.configure_args += ["--enable-lto"]
    self.configure_args += [
        "--with-parallelism=" + str(self.conf_jobs),
        "--with-lang=" + " ".join(_langs),
        "--with-external-tar=" + str(self.chroot_cwd),
    ]


def post_build(self):
    self.make.invoke(["-C", "libreofficekit"])


def install(self):
    self.make.invoke(
        [
            f"DESTDIR={self.chroot_destdir / 'all'}",
            "PREFIXDIR=/usr",
            "distro-pack-install",
        ]
    )
    # move stuff out
    self.mv(self.destdir / "all/usr", self.destdir)


def _take_list(self, listn):
    lcwd = self.parent.cwd
    with open(lcwd / f"file-lists/{listn}_list.txt") as fl:
        for f in fl:
            if f.startswith("%"):
                continue
            self.take(f.strip().removeprefix("/"))
    # also take appdata file if there is one
    self.take(
        f"usr/share/metainfo/libreoffice-{listn}.appdata.xml", missing_ok=True
    )


def _add_lang(langc, langd, langs):
    _langs.append(langc.replace("_", "-"))

    @subpackage(f"libreoffice-lang_{langc.lower()}")
    def _(self):
        self.subdesc = f"{langd} language pack"

        # soft-install at least one langpack by default
        if langc == "en_US":
            self.install_if = [self.with_pkgver(f"{pkgname}-common")]

        def inst():
            _take_list(self, f"lang_{langc}")

        return inst


for _langc, _langd in [
    ("af", "Afrikaans"),
    ("am", "Amharic"),
    ("ar", "Arabic"),
    ("as", "Assamese"),
    ("ast", "Asturian"),
    ("be", "Belarusian"),
    ("bg", "Bulgarian"),
    ("bn", "Bengali"),
    ("bn_IN", "Bengali (India)"),
    ("bo", "Tibetan"),
    ("br", "Breton"),
    ("brx", "Bodo"),
    ("bs", "Bosnian"),
    ("ca", "CatCalan"),
    ("ca_valencia", "Catalan (Valencian)"),
    ("ckb", "Central Kurdish"),
    ("cs", "Czech"),
    ("cy", "Welsh (Cymraeg)"),
    ("da", "Danish"),
    ("de", "German"),
    ("dgo", "Dogri proper"),
    ("dsb", "Lower Sorbian"),
    ("dz", "Dzongkha"),
    ("el", "Greek"),
    ("en_GB", "English (UK)"),
    ("en_US", "English (US)"),
    ("en_ZA", "English (South Africa)"),
    ("eo", "Esperanto"),
    ("es", "Spanish"),
    ("et", "Estonian"),
    ("eu", "Basque"),
    ("fa", "Persian (Farsi)"),
    ("fi", "Finnish"),
    ("fr", "French"),
    ("fur", "Friulian"),
    ("fy", "Frisian"),
    ("ga", "Irish"),
    ("gd", "Scottish Gaelic"),
    ("gl", "Galician"),
    ("gu", "Gujarati"),
    ("gug", "Guaraní (Paraguay)"),
    ("he", "Hebrew"),
    ("hi", "Hindi"),
    ("hr", "Croatian"),
    ("hsb", "Upper Sorbian"),
    ("hu", "Hungarian"),
    ("hy", "Armenian"),
    ("id", "Indonesian"),
    ("is", "Icelandic"),
    ("it", "Italian"),
    ("ja", "Japanese"),
    ("ka", "Georgian"),
    ("kab", "Kabyle"),
    ("kk", "Kazakh"),
    ("km", "Khmer"),
    ("kmr_Latn", "Kurmanji Kurdish (Latin)"),
    ("kn", "Kannada"),
    ("ko", "Korean"),
    ("kok", "Konkani"),
    ("ks", "Kashmiri"),
    ("lb", "Luxembourgish"),
    ("lo", "Lao"),
    ("lt", "Lithuanian"),
    ("lv", "Latvian"),
    ("mai", "Maithili"),
    ("mk", "Macedonian"),
    ("ml", "Malayalam"),
    ("mn", "Mongolian"),
    ("mni", "Meithei (Manipuri)"),
    ("mr", "Marathi"),
    ("my", "Burmese"),
    ("nb", "Norwegian (Bokmal)"),
    ("ne", "Nepali"),
    ("nl", "Dutch"),
    ("nn", "Nynorsk"),
    ("nr", "Ndebele (South)"),
    ("nso", "Northern Sotho"),
    ("oc", "Occitan"),
    ("om", "Oromo"),
    ("or", "Oriya"),
    ("pa_IN", "Punjabi (India)"),
    ("pl", "Polish"),
    ("pt", "Portuguese"),
    ("pt_BR", "Portuguese (Brazil)"),
    ("ro", "Romanian"),
    ("ru", "Russian"),
    ("rw", "Kinyarwanda"),
    ("sa_IN", "Sanskrit (India)"),
    ("sat", "Santali"),
    ("sd", "Sindhi"),
    ("si", "Sinhala"),
    ("sid", "Sidamo"),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("sq", "Albanian"),
    ("sr", "Serbian"),
    ("sr_Latn", "Serbian (Latin)"),
    ("ss", "Swati"),
    ("st", "Southern, Sotho"),
    ("sv", "Swedish"),
    ("sw_TZ", "Swahili (Tanzania)"),
    ("szl", "Silesian"),
    ("ta", "Tamil"),
    ("te", "Telugu"),
    ("tg", "Tajik"),
    ("th", "Thai"),
    ("tn", "Tswana"),
    ("tr", "Turkish"),
    ("ts", "Tsonga"),
    ("tt", "Tatar"),
    ("ug", "Uyghur"),
    ("uk", "Ukrainian"),
    ("uz", "Uzbek"),
    ("ve", "Venda"),
    ("vec", "Venetian"),
    ("vi", "Vietnamese"),
    ("xh", "Xhosa"),
    ("zh_CN", "Simplified Chinese (People's Republic of China)"),
    ("zh_TW", "Traditional Chinese (Taiwan)"),
    ("zu", "Zulu"),
]:
    _add_lang(_langc, _langd, _langs)


def _gensub(subn, subd):
    @subpackage(f"libreoffice-{subn}")
    def _(self):
        self.subdesc = f"{subd}"
        if subn == "writer" or subn == "gnome":
            self.depends = [self.with_pkgver(f"{pkgname}-common")]
        else:
            # the other apps can't launch without writer being present
            self.depends = [self.with_pkgver(f"{pkgname}-writer")]

        # we install gtk integration always by default, to give people
        # a decent UI out of box, but make it a softdep (removable)
        # other stuff is soft-installed by the full metapackage
        if subn == "gnome":
            self.install_if = [self.with_pkgver(f"{pkgname}-common")]
        else:
            self.install_if = [self.parent]

        def inst():
            _take_list(self, subn)

        return inst


for _subn, _subd in [
    ("base", "database"),
    ("calc", "spreadsheet"),
    ("draw", "graphics"),
    ("gnome", "GTK integration"),
    ("impress", "presentations"),
    ("math", "equation editor"),
    ("writer", "word processor"),
]:
    _gensub(_subn, _subd)


@subpackage("libreoffice-qt6")
def _(self):
    self.subdesc = "Qt6 integration"
    self.depends = [self.with_pkgver(f"{pkgname}-common")]
    # qt6 integration for those who already have qt
    self.install_if = [self.with_pkgver(f"{pkgname}-common"), "qt6-qtbase-gui"]

    return ["usr/lib/libreoffice/program/libvclplug_qt6lo.so"]


@subpackage("libreoffice-kf6")
def _(self):
    self.subdesc = "KF6 integration"
    self.depends = [self.with_pkgver(f"{pkgname}-common")]
    # KDE integration for those with plasma
    # TODO: what package actually?
    self.install_if = [
        self.with_pkgver(f"{pkgname}-common"),
        "plasma-workspace",
    ]

    return ["usr/lib/libreoffice/program/libvclplug_kf6lo.so"]


@subpackage("libreoffice-common")
def _(self):
    self.subdesc = "common files"
    self.options = ["!lintcomp"]

    # we don't use the list, just take all remaining files at the end
    return ["usr"]
