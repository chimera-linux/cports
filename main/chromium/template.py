pkgname = "chromium"
# https://chromiumdash.appspot.com/releases?platform=Linux
pkgver = "139.0.7258.138"
pkgrel = 0
archs = ["aarch64", "ppc64le", "x86_64"]
configure_args = [
    'custom_toolchain="//build/toolchain/linux/unbundle:default"',
    'host_toolchain="//build/toolchain/linux/unbundle:default"',
    "blink_enable_generated_code_formatting=false",
    "chrome_pgo_phase=0",
    'clang_base_path="/usr"',
    "clang_use_chrome_plugins=false",
    "disable_fieldtrial_testing_config=true",
    "enable_hangout_services_extension=true",
    "enable_rust=true",
    "enable_stripping=false",
    "enable_vr=false",
    "fatal_linker_warnings=false",
    'ffmpeg_branding="Chrome"',
    'host_pkg_config="/usr/bin/pkg-config"',
    "icu_use_data_file=false",
    "is_clang=true",
    "is_component_ffmpeg=true",
    "is_debug=false",
    "is_official_build=true",
    "link_pulseaudio=true",
    'moc_qt6_path="/usr/lib/qt6/libexec"',
    "proprietary_codecs=true",
    "regenerate_x11_protos=true",
    "rtc_link_pipewire=true",
    "rtc_use_pipewire=true",
    'rust_bindgen_root="/usr"',
    'rust_sysroot_absolute="/usr"',
    # anything works
    'rustc_version="0"',
    "symbol_level=1",
    "treat_warnings_as_errors=false",
    "use_custom_libcxx=false",
    "use_dwarf5=true",
    "use_lld=true",
    "use_pulseaudio=true",
    "use_qt5=false",
    "use_qt6=true",
    "use_sysroot=false",
    "use_system_freetype=true",
    "use_system_harfbuzz=true",
    "use_system_lcms2=true",
    "use_system_libffi=true",
    "use_system_libjpeg=true",
    "use_system_zlib=true",
]
hostmakedepends = [
    "bash",
    "bison",
    "findutils",
    "git",
    "gn",
    "gperf",
    "hwdata",
    "ninja",
    "nodejs",
    "perl",
    "pkgconf",
    "python",
    "rust",
    "rust-bindgen",
]
makedepends = [
    "alsa-lib-devel",
    "brotli-devel",
    "bzip2-devel",
    "cairo-devel",
    "clang-devel",
    "cups-devel",
    "curl-devel",
    "dav1d-devel",
    "double-conversion-devel",
    "elfutils-devel",
    "ffmpeg-devel",
    "flac-devel",
    "fontconfig-devel",
    "freetype-devel",
    "glib-devel",
    "gtk+3-devel",
    "heimdal-devel",
    "highway-devel",
    "lcms2-devel",
    "libaom-devel",
    "libavif-devel",
    "libcap-devel",
    "libdrm-devel",
    "libevdev-devel",
    "libevent-devel",
    "libexif-devel",
    "libffi8-devel",
    "libgcrypt-devel",
    "libjpeg-turbo-devel",
    "libmtp-devel",
    "libpng-devel",
    "libpulse-devel",
    "libsecret-devel",
    "libucontext-devel",
    "libusb-devel",
    "libva-devel",
    "libwebp-devel",
    "libxcomposite-devel",
    "libxcursor-devel",
    "libxdamage-devel",
    "libxi-devel",
    "libxml2-devel",
    "libxrandr-devel",
    "libxscrnsaver-devel",
    "libxshmfence-devel",
    "libxslt-devel",
    "linux-headers",
    "minizip-devel",
    "musl-bsd-headers",
    "nss-devel",
    "opus-devel",
    "pciutils-devel",
    "pipewire-devel",
    "qt6-qtbase-devel",
    "rust-std",
    "snappy-devel",
    "speex-devel",
    "sqlite-devel",
    "udev-devel",
    "xcbproto",
    "zlib-ng-compat-devel",
]
depends = [
    "hwdata-usb",
    "xdg-utils",
]
pkgdesc = "Web browser"
license = "BSD-3-Clause"
url = "https://www.chromium.org"
source = f"https://commondatastorage.googleapis.com/chromium-browser-official/chromium-{pkgver}.tar.xz"
sha256 = "86db7326987a280380e35cf1e961df8d08fb1f8eb3b0ae9ee8250b5dff65e1ea"
debug_level = 1
tool_flags = {
    "CFLAGS": [
        "-Wno-unknown-warning-option",
        "-Wno-builtin-macro-redefined",
        "-Wno-deprecated-declarations",
        "-Wno-sign-compare",
        "-Wno-shorten-64-to-32",
    ],
    "CXXFLAGS": [
        "-Wno-unknown-warning-option",
        "-Wno-builtin-macro-redefined",
        "-Wno-deprecated-declarations",
        "-Wno-sign-compare",
        "-Wno-shorten-64-to-32",
    ],
}
file_modes = {
    "usr/lib/chromium/chrome-sandbox": ("root", "root", 0o4755),
}
hardening = ["!scp"]
# lol
options = ["!cross", "!check", "!scanshlibs"]

match self.profile().arch:
    case "ppc64le" | "riscv64":
        # trap in add_label_offset() (assembler-ppc.cc)
        # also crashes on riscv64
        hardening += ["!int"]


def post_patch(self):
    self.rm("third_party/node/linux/node-linux-x64/bin/node", force=True)
    self.mkdir("third_party/node/linux/node-linux-x64/bin", parents=True)
    self.ln_s("/usr/bin/node", "third_party/node/linux/node-linux-x64/bin/node")

    self.cp(self.files_path / "unbundle.sh", ".")
    self.cp(self.files_path / "pp-data.sh", ".")


def configure(self):
    # where we mess with libvpx configuration, regen the files
    if self.profile().arch == "ppc64le":
        self.do(
            self.chroot_cwd / "third_party/libvpx/generate_gni.sh",
            wrksrc="third_party/libvpx",
            env={"PATH": f"{self.chroot_cwd / 'out/Release'}:/usr/bin"},
        )

    _unbundle = [
        "brotli",
        "dav1d",
        "double-conversion",
        "ffmpeg",
        "flac",
        "fontconfig",
        "freetype",
        "harfbuzz-ng",
        "highway",
        "icu",
        "libjpeg",
        "libpng",
        "libsecret",
        "libusb",
        "libwebp",
        "libxml",
        "libxslt",
        "opus",
        "zlib",
        "zstd",
    ]

    for lib in _unbundle:
        self.do("./unbundle.sh", lib)
    self.do("./unbundle.sh", "libjpeg_turbo")
    self.do(
        "./build/linux/unbundle/replace_gn_files.py",
        "--system-libraries",
        *_unbundle,
    )
    self.do("./third_party/libaddressinput/chromium/tools/update-strings.py")

    _confargs = [*self.configure_args]

    _vaapi = "true"
    # sqlite3BtreeOpen crash
    _cfi = "false"
    _lto = "true" if self.has_lto() else "false"
    _maglev = "true"

    match self.profile().arch:
        case "aarch64":
            _confargs.append('target_cpu="arm64"')
            # _cfi = "true"
        case "x86_64":
            _confargs.append('target_cpu="x64"')
            # _cfi = "true"
        case "ppc64le":
            _confargs.append('target_cpu="ppc64"')
            _vaapi = "false"
            _maglev = "false"
        case "riscv64":
            _confargs.append('target_cpu="riscv64"')
            _vaapi = "false"
            _maglev = "false"

    _confargs += [
        f"use_vaapi={_vaapi}",
        f"is_cfi={_cfi}",
        f"use_thin_lto={_lto}",
        f"v8_enable_maglev={_maglev}",
    ]

    self.do(
        "gn",
        "gen",
        "out/Release",
        "--args=" + " ".join(_confargs),
    )


def build(self):
    self.do(
        "ninja",
        "-C",
        "out/Release",
        f"-j{self.make_jobs}",
        "chrome",
        "chrome_sandbox",
        "chromedriver.unstripped",
        "chrome_crashpad_handler",
        env={
            "CCACHE_SLOPPINESS": "include_file_mtime",
            # rather than disable working rustc -Z flags, permit them
            "RUSTC_BOOTSTRAP": "1",
        },
    )


def install(self):
    srcp = "out/Release"
    dstp = "usr/lib/chromium"

    self.install_license("LICENSE")

    self.install_file(f"{srcp}/chrome", dstp, mode=0o755, name="chromium")
    self.install_file(f"{srcp}/chrome_crashpad_handler", dstp, mode=0o755)
    self.install_file(
        f"{srcp}/chromedriver.unstripped", dstp, mode=0o755, name="chromedriver"
    )
    self.install_file(
        f"{srcp}/chrome_sandbox", dstp, mode=0o4755, name="chrome-sandbox"
    )
    self.install_file(f"{srcp}/libEGL.so", dstp, mode=0o755)
    self.install_file(f"{srcp}/libGLESv2.so", dstp, mode=0o755)
    self.install_file(f"{srcp}/libqt6_shim.so", dstp, mode=0o755)
    self.install_file(f"{srcp}/libvulkan.so.1", dstp, mode=0o755)
    self.install_file(f"{srcp}/libvk_swiftshader.so", dstp, mode=0o755)
    self.install_file(f"{srcp}/vk_swiftshader_icd.json", dstp, mode=0o755)
    self.install_file(f"{srcp}/xdg-mime", dstp, mode=0o755)
    self.install_file(f"{srcp}/xdg-settings", dstp, mode=0o755)

    self.install_file(f"{srcp}/*.bin", dstp, glob=True)
    self.install_file(f"{srcp}/*.pak", dstp, glob=True)
    self.install_file(f"{srcp}/locales/*.pak", f"{dstp}/locales", glob=True)

    for s in [24, 48, 64, 128, 256]:
        self.install_file(
            f"chrome/app/theme/chromium/product_logo_{s}.png",
            f"usr/share/icons/hicolor/{s}x{s}/apps",
            name="chromium.png",
        )
    for s in [16, 32]:
        self.install_file(
            f"chrome/app/theme/default_100_percent/chromium/product_logo_{s}.png",
            f"usr/share/icons/hicolor/{s}x{s}/apps",
            name="chromium.png",
        )

    # launcher
    self.install_file(
        self.files_path / "chromium-launcher.sh", dstp, mode=0o755
    )
    self.install_file(self.files_path / "chromium.conf", "etc/chromium")

    self.install_dir("usr/bin")
    self.install_link(
        "usr/bin/chromium-browser", "../lib/chromium/chromium-launcher.sh"
    )
    self.install_link("usr/bin/chromedriver", "../lib/chromium/chromedriver")
    self.install_link("usr/bin/chromium", "chromium-browser")

    # desktop file, manpage etc
    self.do("./pp-data.sh")
    self.install_file("chromium.desktop", "usr/share/applications")
    self.install_file("chromium.appdata.xml", "usr/share/metainfo")
    self.install_man("chromium.1")
