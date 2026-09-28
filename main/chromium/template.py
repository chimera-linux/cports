pkgname = "chromium"
# https://chromiumdash.appspot.com/releases?platform=Linux
pkgver = "154.0.8037.57"
# tools/rust/update_rust.py -> CRUBIT_REVISION
_crubit_ver = "69b85cba43f85a6439dc0be86a6fe424bb07a100"
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
    # anything works
    'rustc_version="0"',
    "symbol_level=1",
    "treat_warnings_as_errors=false",
    "safe_browsing_use_unrar=false",
    "use_clang_modules=false",
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
    "cargo",
    "esbuild",
    "findutils",
    "git",
    "gn",
    "go",
    "gperf",
    "hwdata",
    "ninja",
    "nodejs",
    "perl",
    "pkgconf",
    "python",
    "rust",
    "rust-bindgen",
    "rust-rustfmt",
    "rust-src",
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
source = [
    f"https://github.com/chromium-linux-tarballs/chromium-tarballs/releases/download/{pkgver}/chromium-{pkgver}-linux.tar.xz",
    f"https://github.com/google/crubit/archive/{_crubit_ver}/crubit-{_crubit_ver}.tar.gz",
    "https://registry.npmjs.org/@rollup/wasm-node/-/wasm-node-4.22.4.tgz",
]
source_paths = [".", "crubit", "rollup", "typescript"]
sha256 = [
    "2b2c55e73cbf9ce4103f8f87829d0b9ce61916152e3deb1596d451d5e291deae",
    "af8910353d7694c2a97231b7ce346f8cf7a27912dd4fe52bf631bb82a99f4bcd",
    "ee49bf67bd9bee869405af78162d028e2af0fcfca80497404f56b1b99f272717",
]
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
options = ["!ci", "etcfiles", "!cross", "!check", "!scanshlibs"]

match self.profile.arch:
    case "aarch64":
        source += [
            "https://github.com/microsoft/TypeScript/releases/download/v7.0.2/typescript-linux-arm64.tgz"
        ]
        sha256 += [
            "c83d931ac9dd7549cde6e71246aa9d6a9812843023df3e277fe3b5dcf41dd0ea"
        ]
    case "ppc64le":
        source += [
            "https://github.com/microsoft/TypeScript/releases/download/v7.0.2/typescript-linux-ppc64.tgz"
        ]
        sha256 += [
            "8c30ad95ff40cff8bba2ab294abde3bfee6fa12b2b649f80ec90ef3188842db1"
        ]
    case "x86_64":
        source += [
            "https://github.com/microsoft/TypeScript/releases/download/v7.0.2/typescript-linux-x64.tgz"
        ]
        sha256 += [
            "7ecad6f67377e831856367ab062ef394f21506a611405bf8ac0ff039348637d3"
        ]

match self.profile.arch:
    case "ppc64le" | "riscv64":
        # trap in add_label_offset() (assembler-ppc.cc)
        # also crashes on riscv64
        hardening += ["!int"]


def post_patch(self):
    from cbuild.util import patch

    # replace wrong node with a working one
    self.rm("third_party/node/linux/node-linux-x64/bin/node", force=True)
    self.mkdir("third_party/node/linux/node-linux-x64/bin", parents=True)
    self.ln_s("/usr/bin/node", "third_party/node/linux/node-linux-x64/bin/node")

    # replace wrong esbuild with a working one
    self.rm(
        "third_party/devtools-frontend/src/third_party/esbuild/esbuild",
        force=True,
    )
    self.ln_s(
        "/usr/bin/esbuild",
        "third_party/devtools-frontend/src/third_party/esbuild/esbuild",
    )
    self.rm(
        "third_party/devtools-frontend/src/node_modules/esbuild",
        recursive=True,
        force=True,
    )
    self.ln_s(
        "/usr/lib/node_modules/esbuild",
        "third_party/devtools-frontend/src/node_modules/esbuild",
    )

    # replace wrong gperf with a working one
    self.rm("third_party/gperf/cipd/bin/gperf", force=True)
    self.ln_s("/usr/bin/gperf", "third_party/gperf/cipd/bin/gperf")

    # lol
    self.mkdir("third_party/dawn/tools/golang/linux-unknown/bin", parents=True)
    self.ln_s(
        "/usr/bin/go", "third_party/dawn/tools/golang/linux-unknown/bin/go"
    )

    # replace x64 typescript with the one for our correct platform
    # and patch the library to suit whatever google is doing
    self.rm("third_party/typescript/linux-amd64/src", recursive=True)
    patch.patch(
        self,
        list(
            (self.cwd / "third_party/typescript/linux-amd64/3pp/patches").glob(
                "*.patch"
            )
        ),
        wrksrc="typescript",
    )
    self.mv("typescript", "third_party/typescript/linux-amd64/src")

    # uh oh
    # thanks lnl for figuring this out
    self.rm("buildtools/linux64-format/clang-format")
    self.ln_s("/usr/bin/clang-format", "buildtools/linux64-format/clang-format")
    self.mkdir("third_party/rust-toolchain/bin", parents=True)
    self.mkdir("third_party/rust-toolchain/lib", parents=True)
    self.ln_s("/usr/bin/cargo", "third_party/rust-toolchain/bin/cargo")
    self.ln_s("/usr/bin/rustc", "third_party/rust-toolchain/bin/rustc")
    self.ln_s("/usr/bin/rustfmt", "third_party/rust-toolchain/bin/rustfmt")
    self.ln_s("/usr/lib/rustlib", "third_party/rust-toolchain/lib/rustlib")
    self.mkdir("third_party/rust-toolchain-intermediate", parents=True)
    self.ln_s("../../crubit", "third_party/rust-toolchain-intermediate/crubit")
    self.do(
        "python",
        "./tools/rust/build_crubit.py",
        "--skip-checkout",
        allow_network=True,
        env={"RUSTC_BOOTSTRAP": "1"},
    )
    self.mkdir("third_party/rust-toolchain/lib/third_party", parents=True)
    self.ln_s(
        "../../../../crubit",
        "third_party/rust-toolchain/lib/third_party/crubit",
    )
    with (self.cwd / "third_party/rust-toolchain/VERSION").open("w") as outf:
        self.do("rustc", "-V", stdout=outf)
    self.cp(
        "third_party/rust-toolchain/VERSION",
        "third_party/rust-toolchain/INSTALLED_VERSION",
    )
    self.do(
        "cargo",
        "build",
        "--locked",
        "--release",
        wrksrc="tools/crates/gnrt",
        allow_network=True,
    )
    self.do(
        "./tools/crates/gnrt/target/release/gnrt",
        "gen",
        "--for-std",
        "third_party/rust-toolchain/lib/rustlib/src/rust",
    )

    self.cp(self.files_path / "unbundle.sh", ".")
    self.cp(self.files_path / "pp-data.sh", ".")

    self.rm(
        "third_party/devtools-frontend/src/node_modules/rollup", recursive=True
    )
    self.mv("rollup", "third_party/devtools-frontend/src/node_modules")


def configure(self):
    # where we mess with libvpx configuration, regen the files
    if self.profile.arch == "ppc64le":
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
        "harfbuzz",
        "highway",
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

    match self.profile.arch:
        case "aarch64":
            _confargs.append('target_cpu="arm64"')
            # _cfi = "true"
        case "x86_64":
            _confargs.append('target_cpu="x64"')
            # _cfi = "true"
        case "ppc64le":
            _confargs.append('target_cpu="ppc64"')
            _vaapi = "false"
        case "riscv64":
            _confargs.append('target_cpu="riscv64"')
            _vaapi = "false"

    _confargs += [
        f"use_vaapi={_vaapi}",
        f"is_cfi={_cfi}",
        f"use_thin_lto={_lto}",
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
